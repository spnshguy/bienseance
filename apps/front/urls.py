from django.conf.urls import url

from .views import home, ajax_validate_newsletter_form, ajax_validate_contact_form, purchase_success

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^payment/success/$', purchase_success, name='purchase_success'),
    url(r'^ajax_validate_newsletter_form/$', ajax_validate_newsletter_form, name='ajax_validate_newsletter_form'),
    url(r'^ajax_validate_contact_form/$', ajax_validate_contact_form, name='ajax_validate_contact_form'),
]
