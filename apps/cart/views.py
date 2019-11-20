# Create your views here.
from constance import config
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse

from apps.cart.cart import Cart, ItemDoesNotExist
from apps.products.models import Item, Size, Magazine

from django.conf import settings

from django.shortcuts import redirect


def mk_cart_magazine(request):
    size = Size.objects.get(sku=request.GET.get('sku'))

    mag = Item.objects.get(available_sizes__id=size.id, id=request.GET.get('id'))
    # print(mag.available_sizes.first())
    cart = Cart(request)
    try:
        cart.remove(mag)

    except ItemDoesNotExist:
        pass

    cart.add(product=mag, unit_price=size.price, size=size)

    return redirect(reverse('products:get_cart'))


def ajax_add_cart_item_by_sku(request):
    size = Size.objects.get(sku=settings.BIEN_SLUG_MAG_001)
    product = Item.objects.get(available_sizes__id=size.id)

    cart = Cart(request)
    cart.add(product, size.price)

    return JsonResponse({'success': True, 'template': "New size %d" % cart.count()})


def ajax_update_cart_item(request):
    cart = Cart(request)
    product = Item.objects.get(id=request.POST.get('item_product'))
    cart.update(product, request.POST.get('item_quantity'), product.available_sizes.first().price,
                request.POST.get('item_size'))

    template = render_to_string('cart/cart_item_container.html', {
        'cart': cart,
        'config': config
    })

    return JsonResponse({'success': True, 'template': template})


def ajax_remove_item(request, item_id):
    cart = Cart(request)
    product = Item.objects.get(id=item_id)
    cart.remove(product, request.GET.get('item_size'))
    if cart.count():
        template = render_to_string('cart/cart_item_container.html', {
            'cart': cart,
            'config': config
        })
    else:
        template = render_to_string('cart/empty.html', {
        })

    return JsonResponse({'success': True, 'template': template})
