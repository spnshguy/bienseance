from django.contrib import admin
from hijack_admin.admin import HijackUserAdminMixin

from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin, HijackUserAdminMixin):
    model = User
    list_display = ['email', 'username', ]
