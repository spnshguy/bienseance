from django.contrib import admin

from apps.cart.models import Cart


@admin.register(Cart)
class TagAdmin(admin.ModelAdmin):
    list_display = 'creation_date',
    search_fields = 'creation_date',