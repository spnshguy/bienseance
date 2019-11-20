from django.contrib import admin

from apps.quotes.models import Quote


@admin.register(Quote)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'title', 'author'
    search_fields = 'title', 'author'
