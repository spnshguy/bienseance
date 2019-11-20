from django.contrib import admin
from parler.admin import TranslatableAdmin

from apps.blogs.forms import BlogAdminForm
from apps.blogs.models import Blog, Category, Tag, BlogImage


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = 'name', 'slug', 'language_column'
    search_fields = 'translations__name',


@admin.register(Tag)
class TagAdmin(TranslatableAdmin):
    list_display = 'name', 'slug', 'language_column'
    search_fields = 'translations__name',


@admin.register(BlogImage)
class BlogImageAdmin(admin.ModelAdmin):
    list_display = 'image',


@admin.register(Blog)
class BlogAdmin(TranslatableAdmin):
    list_display = 'title', 'slug', 'publication_date', 'language_column'
    search_fields = 'translations__title',
    form = BlogAdminForm
    filter_vertical = 'tags', 'images'
    fieldsets = (
        (None, {
            'fields': (
            'title', 'short_description', 'content', 'category', 'tags', 'author', 'images', 'publication_date', 'is_active', 'order'),
        }),
    )
