from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from django.views.i18n import javascript_catalog
from solid_i18n.urls import solid_i18n_patterns

from apps.front.views import custom_404, custom_500
from .sitemaps import sitemaps

js_info_dict = {
    'domain': 'djangojs',
    'packages': ('apps.custom_admin', 'apps.front', 'apps.user_profile',)
}

urlpatterns = [
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain'),
        {'PROJECT_URI': settings.PROJECT_URI
         }),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

]

urlpatterns += solid_i18n_patterns(
    url(r'^accounts/', include('apps.accounts.urls', namespace='accounts')),
    url(r'^products/', include('apps.products.urls', namespace='custom_products')),
    url(r'^cart/', include('apps.cart.urls', namespace='cart')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^jsi18n/$', javascript_catalog, js_info_dict, name='javascript-catalog'),
    url(r'^filer/', include('filer.urls')),
    url(r'^404/', custom_404, name='404'),
    url(r'^500/', custom_500, name='404'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)

handler404 = custom_404
handler500 = custom_500

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
