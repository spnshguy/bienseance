from django.conf.urls import url

from .views import BlogList, BlogSingle

urlpatterns = [
    url(r'^$', BlogList.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', BlogSingle.as_view(), name='single'),
]
