from django.conf.urls import url

from .views import ajax_update_cart_item, ajax_remove_item, ajax_add_cart_item_by_sku, mk_cart_magazine

urlpatterns = [
    url(r'^ajax_add_cart_item_by_sku/$', ajax_add_cart_item_by_sku, name='ajax_add_cart_item_by_sku'),
    url(r'^mk_cart_magazine/$', mk_cart_magazine, name='mk_cart_magazine'),
    url(r'^ajax_update_cart_item/$', ajax_update_cart_item, name='ajax_update_cart_item'),
    url(r'^ajax_remove_item/(?P<item_id>[\d-]+)/$', ajax_remove_item, name='ajax_remove_item'),
]
