from django.contrib import admin
from cms.models import GlobalPagePermission, PageUser, PageType

admin.site.unregister(PageUser)
admin.site.unregister(GlobalPagePermission)
