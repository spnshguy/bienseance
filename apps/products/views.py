import random

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View
from django.views.decorators.http import require_POST

from apps.cart.cart import Cart
from apps.products.constants import ASCENDING, DESCENDING
from apps.products.forms import ProductFilterForm, ProductOrderingForm, MagazineFilterForm
from apps.products.models import Product, Magazine, Item, Designer

from django.conf import settings

import uuid

from apps.quotes.models import Quote
from libs.squareconnect import CheckoutApi
from libs.squareconnect.models import CreateCheckoutRequest, CreateOrderRequestTax, CreateOrderRequest, CreateOrderRequestLineItem


class ProductList(View):
    def get(self, request):
        return redirect('/coming-soon/');

        # Disabled until we have a store again.
        designer = request.GET.get('designer', None)
        products = Product.objects.prefetch_related('product_images').filter(published=True)
        product_list = list()
        columns = 0
        max_id_quote = Quote.objects.all().count()
        if designer:
            try:
                designer = Designer.objects.get(name=designer)
            except Designer.DoesNotExist:
                pass
            else:
                products = products.filter(designer=designer)

        for product in products:
            if product.product_images.first() and product.product_images.first().image.width > \
                    product.product_images.first().image.height:
                columns += 2
                if columns > 4 and max_id_quote:
                    quote_id = random.randint(1, max_id_quote)
                    quote = Quote.objects.get(id=quote_id)
                    product_list.append(quote)
                product_list.append(product)
            else:
                columns += 1
                product_list.append(product)
            if columns >= 4 or len(product_list) % 24 == 0:
                columns = 0
        paginator = Paginator(product_list, 24)

        page = request.GET.get('page')

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        index = products.number - 1
        max_index = len(paginator.page_range)
        start_index = index - 2 if index >= 2 else 0
        end_index = index + 2 if index <= max_index - 2 else max_index
        page_range = list(paginator.page_range)[start_index:end_index]

        if designer:
            product_filter_form = ProductFilterForm(initial={'designer': designer})
        else:
            product_filter_form = ProductFilterForm()

        return render(request, 'products/list.html', {
            'products': products,
            'page_range': page_range,
            'product_filter_form': product_filter_form,
        })


class ProductSingle(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        related_products = Product.objects.filter(published=True).exclude(id=product.id).distinct()
        if len(product.tags.all()):
            related_products = related_products.filter(tags__in=product.tags.all())
        related_products = related_products[:3]

        columns = 0
        count = 0
        for related_product in related_products:
            if related_product.product_images.all() and related_product.product_images.first().image.width > related_product.product_images.first().image.height:
                columns += 6
            else:
                columns += 3
            if columns <= 12:
                count += 1
        related_products = related_products[:count]
        order_form = ProductOrderingForm(instance=product)

        return render(request, 'products/single.html', {
            'product': product,
            'related_products': related_products,
            'order_form': order_form,
        })


class MagazineList(View):
    def get(self, request):
        magazines = Magazine.objects.all()
        paginator = Paginator(magazines, 6)

        page = request.GET.get('page')

        try:
            magazines = paginator.page(page)
        except PageNotAnInteger:
            magazines = paginator.page(1)
        except EmptyPage:
            magazines = paginator.page(paginator.num_pages)

        index = magazines.number - 1
        max_index = len(paginator.page_range)
        start_index = index - 2 if index >= 2 else 0
        end_index = index + 2 if index <= max_index - 2 else max_index
        page_range = list(paginator.page_range)[start_index:end_index]
        magazine_filter_form = MagazineFilterForm()

        return render(request, 'products/magazine_list.html', {
            'magazines': magazines,
            'page_range': page_range,
            'magazine_filter_form': magazine_filter_form,
        })


class MagazineSingle(View):
    def get(self, request, slug):
        magazine = get_object_or_404(Magazine, slug=slug)
        # order_form = ProductOrderingForm(instance=magazine)
        return render(request, 'products/magazine_single.html', {
            'magazine': magazine,
            # 'order_form': order_form,
        })


def ajax_validation_order_form(request, product_id):
    item = get_object_or_404(Item, id=product_id)

    order_form = ProductOrderingForm(data=request.POST, instance=item)

    if order_form.is_valid():
        cart = Cart(request)

        size = order_form.cleaned_data.get('available_sizes', None)
        cart.add(item, size.price, order_form.cleaned_data['amount'],
                 size)
        success_url = reverse('products:get_cart')
        return JsonResponse({'success': True, 'success_url': success_url})
    return JsonResponse(order_form.errors.as_json(), status=400, safe=False)


def ajax_validation_magazine_order_form(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order_form = ProductOrderingForm(data=request.POST, instance=product)

    if order_form.is_valid():
        cart = Cart(request)
        cart.add(product, product.available_sizes().first().price, order_form.cleaned_data['amount'])
        return JsonResponse({'success': True})

    return JsonResponse(order_form.errors.as_json(), status=400, safe=False)


def get_cart(request):
    return render(request, 'products/cart.html', {
        'cart': Cart(request),
    })


def cart_checkout(request):
    checkout_api = CheckoutApi()
    checkout_api.api_client.configuration.access_token = settings.BIEN_SQR_ACCESS_TOKEN

    cart = Cart(request)

    line_items = []
    for item in cart:
        top_size = item.get_product().available_sizes.first()
        line_items.append(CreateOrderRequestLineItem(
            catalog_object_id=top_size.square_item_id,
            quantity=str(item.quantity),
            modifiers=[],
            discounts=[]
        ))

    result = checkout_api.create_checkout(settings.BIEN_SQR_LOCATION_ID, CreateCheckoutRequest(
        idempotency_key=str(uuid.uuid1()),
        order=CreateOrderRequest(
            idempotency_key=str(uuid.uuid1()),
            reference_id=str(uuid.uuid1()),
            line_items=line_items,
            taxes=[
                CreateOrderRequestTax(catalog_object_id='FI5RZJJEJM3HERAYKIOEAJA5'),
                CreateOrderRequestTax(catalog_object_id='RLOQ34QJMS7GPEYZV6VUBGXY')
            ],
            discounts=[]
        ),
        ask_for_shipping_address=True,
        merchant_support_email=settings.ADMIN_EMAIL,
        redirect_url=settings.BIEN_SQR_REDIRECT_URL
    ))

    return redirect(result.checkout.checkout_page_url)


@require_POST
def ajax_product_filter(request):
    if not request.is_ajax():
        return HttpResponseBadRequest()
    products = Product.objects.all()
    order = request.POST.get('order', None)
    designer = request.POST.get('designer', None)
    tag = request.POST.get('tag', None)
    if designer:
        products = products.filter(designer=designer)
    if tag:
        products = products.filter(tags=designer)
    if order:
        if order == str(ASCENDING):
            products = products.order_by('title')
        elif order == str(DESCENDING):
            products = products.order_by('-title')
        else:
            products = products.order_by('-nb_views')

    context = {
        'products': products
    }
    if not designer and not tag and not order:
        paginator = Paginator(products, 6)

        page = request.GET.get('page')

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        index = products.number - 1
        max_index = len(paginator.page_range)
        start_index = index - 2 if index >= 2 else 0
        end_index = index + 2 if index <= max_index - 2 else max_index
        page_range = list(paginator.page_range)[start_index:end_index]
        context.update({
            'products': products,
            'page_range': page_range,
        })

    template = render_to_string('products/_product_card_container.html', context)
    return JsonResponse({'success': True, 'template': template})
