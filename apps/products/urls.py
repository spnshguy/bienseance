from django.conf.urls import url

from .views import ProductList, ProductSingle, ajax_product_filter, ajax_validation_order_form, get_cart, MagazineList, \
    MagazineSingle, ajax_validation_magazine_order_form, cart_checkout

urlpatterns = [
    url(r'^$', ProductList.as_view(), name='list'),
    url(r'^magazines/$', MagazineList.as_view(), name='magazine_list'),
    url(r'^magazines/(?P<slug>[\w-]+)/$', MagazineSingle.as_view(), name='magazine_single'),
    url(r'^get_cart/$', get_cart, name='get_cart'),
    url(r'^cart_checkout/$', cart_checkout, name='cart_checkout'),
    url(r'^ajax_product_filter/$', ajax_product_filter, name='ajax_product_filter'),
    url(r'^ajax_validation_order_form/(?P<product_id>[\d-]+)/$', ajax_validation_order_form, name='ajax_validation_order_form'),
    url(r'^ajax_validation_magazine_order_form/(?P<magazine_id>[\d-]+)/$', ajax_validation_magazine_order_form, name='ajax_validation_magazine_order_form'),
    url(r'^(?P<slug>[\w-]+)/$', ProductSingle.as_view(), name='single'),
]
