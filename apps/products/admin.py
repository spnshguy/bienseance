from django.contrib import admin

from apps.products.forms import ProductAdminForm
from apps.products.models import Color, Size, Image, Product, Magazine, Designer, Tag


@admin.register(Size)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name', 'price', 'current_stock'
    search_fields = 'name', 'price', 'current_stock'


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = 'name',
    search_fields = 'name',


@admin.register(Designer)
class DesignerAdmin(admin.ModelAdmin):
    list_display = 'name', 'link',
    search_fields = 'name', 'link',


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = 'image',
    search_fields = 'image',


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = 'name',
    search_fields = 'name',


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'title',
    search_fields = 'title',
    form = ProductAdminForm
    filter_vertical = 'available_sizes', 'tags'


class SizeInline(admin.TabularInline):
    model = Magazine.available_sizes.through
    extra = 1
    verbose_name = "Available Size"
    verbose_name_plural = "Available Sizes"


@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    list_display = 'title',
    search_fields = 'title',
    filter_vertical = 'product_images', 'available_sizes',
    inlines = SizeInline,
    exclude = 'available_sizes',
