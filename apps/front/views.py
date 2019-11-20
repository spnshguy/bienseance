from datetime import datetime
import time

from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.utils.translation import ugettext

from apps.blogs.models import Blog
from apps.cart.cart import Cart
from apps.front.forms import NewsletterForm, ContactForm
from apps.products.models import Product

from django.conf import settings

from libs import squareconnect


def home(request):
    today = datetime.now()
    featured_blogs = Blog.objects.translated(publication_date__lte=today).filter(is_active=True).order_by(
        '-translations__publication_date')[
                     :3]
    featured_products = Product.objects.filter(is_featured=True, published=True)[:8]

    return render(request, 'home.html', {
        'featured_blogs': featured_blogs,
        'featured_products': featured_products,
    })


def ajax_validate_newsletter_form(request):
    if not request.is_ajax():
        return HttpResponseBadRequest()
    newsletter_form = NewsletterForm(data=request.POST, prefix='newsletter')
    if newsletter_form.is_valid():
        return JsonResponse({'success': True, 'message': ugettext('Merci de vous être abonné à notre infolettre!')})
    return JsonResponse(newsletter_form.errors.as_json(), status=400, safe=False)


def ajax_validate_contact_form(request):
    if not request.is_ajax():
        return HttpResponseBadRequest()
    contact_form = ContactForm(data=request.POST, prefix='contact')
    if contact_form.is_valid():
        message = 'from: ' + contact_form.cleaned_data.get('name') + '\n' + 'email: ' + contact_form.cleaned_data.get(
            'email') + '\n' + 'message: ' + contact_form.cleaned_data.get('message')
        send_mail('New message from Bienseance', message, settings.ADMIN_EMAIL,
                  [settings.ADMIN_EMAIL])

        return JsonResponse(
            {'success': True, 'message': ugettext('Merci de nos avoir contacté. Votre message a été reçu.')})
    return JsonResponse(contact_form.errors.as_json(), status=400, safe=False)



def purchase_success(request):
    # Sample URL:
    # http://127.0.0.1:8000/success/?checkoutId=CBASEDGudSOD2DXxMx1KwaQWwbI&referenceId=api-order-002&transactionId=12tDMXN2yonV07EUiJT2gQfzTG7YY

    passed_transaction_id = request.GET.get('transactionId', None)
    if not passed_transaction_id:
        return render(request, 'purchase_failed.html', {'error_info': {'message': 'No transactionId'}})

    # Get the customer's id
    try:
        transaction_api = squareconnect.apis.transactions_api.TransactionsApi()
        transaction_api.api_client.configuration.access_token = settings.BIEN_SQR_ACCESS_TOKEN
        transaction_result = transaction_api.retrieve_transaction(settings.BIEN_SQR_LOCATION_ID, passed_transaction_id)
        customer_id = transaction_result.transaction.tenders.pop().customer_id
    except:
        return render(request, 'purchase_failed.html',
                      {'error_info': {'message': 'Failed to load transaction: ' + passed_transaction_id}})

    # There are replication delays which can cause the customer to not be available here.
    # try to get the value, try several times before failing.
    keep_retrying = 8
    while True:
        try:
            # And now the customer email
            customers_api = squareconnect.apis.customers_api.CustomersApi()
            customers_api.api_client.configuration.access_token = settings.BIEN_SQR_ACCESS_TOKEN
            customer_result = customers_api.retrieve_customer(customer_id)
            customer_email = customer_result.customer.email_address

        except:
            if keep_retrying == 0:
                return render(request, 'purchase_failed.html',
                              {'error_info': {'message': 'Failed to load customer.'}})
            else:
                keep_retrying = keep_retrying - 1
                time.sleep(1.5)
                continue

        break


    # Build the results
    order_info = {
        'customer_id': customer_id,
        'transaction_id': passed_transaction_id,
        'customer_email': customer_email
    }
    cart = Cart(request)
    cart.clear()
    return render(request, 'success.html', order_info)


def custom_404(request):
    return render(request, 'custom-404.html', {

    })


def custom_500(request):
    return render(request, 'custom-500.html', {

    })
