from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from sortedm2m.fields import SortedManyToManyField


class Size(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    sku = models.CharField(_('SKU'), max_length=64, unique=True, null=True)
    square_item_id = models.CharField(_('Square Item ID'), max_length=64, unique=True, null=True)
    price = models.FloatField(_('Price'))
    current_stock = models.PositiveIntegerField(_('Current Stock'), default=0)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(_('Name'), max_length=50)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField()
    order = models.PositiveIntegerField(_('Order'), default=0)

    def __str__(self):
        return self.image.name

    class Meta:
        ordering = 'order',


class Designer(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    link = models.URLField(_('Link'))

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(_('Name'), max_length=30)
    icon = models.ImageField(upload_to='product_icons')

    def __str__(self):
        return self.name


class Item(models.Model):
    title = models.CharField(_('Title'), max_length=100)
    slug = AutoSlugField(populate_from='title', unique=True)
    short_description = RichTextField(blank=True)
    description = RichTextUploadingField(blank=True)

    tags = models.ManyToManyField('Tag', verbose_name=_('Tags'), blank=True)
    product_images = SortedManyToManyField('Image')
    nb_purchase = models.PositiveIntegerField(_('Number of purchases'), default=0)
    available_sizes = models.ManyToManyField('Size', verbose_name=_('Available sizes'), related_name='size_products',
                                             blank=True)
    order = models.PositiveIntegerField(_('Order'), default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


class Product(Item):
    # available_colors = models.ManyToManyField('Color', verbose_name=_('Available colors'),
    #                                           related_name='color_products')
    is_featured = models.BooleanField(_('Is Featured'), default=False)
    designer = models.ForeignKey('Designer', verbose_name=_('Designer'))
    published = models.BooleanField(_('Is Published'), default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Magazine(Item):
    file = models.FileField(_('File'), blank=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
