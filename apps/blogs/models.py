from autoslug import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField

from django.db import models
from django.utils.translation import ugettext_lazy as _
from imagekit.models import ImageSpecField
from parler.models import TranslatableModel, TranslatedFields
from pilkit.processors import ResizeToFit

from apps.custom_plugins.validation import ValidateImageFile


class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_('Name'), max_length=100),
        slug=AutoSlugField(populate_from='name')
    )

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class Tag(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_('Name'), max_length=100),
        slug=AutoSlugField(populate_from='name')
    )
    icon = ValidateImageFile(processors=[ResizeToFit(25, 25)],
                             format='PNG',
                             options={'quality': 60},
                             )

    def __str__(self):
        return self.name


class BlogImage(models.Model):
    image = ValidateImageFile(format='PNG', options={'quality': 90})
    image_card = ImageSpecField(source='image',
                                processors=[ResizeToFit(600, 300)],
                                format='PNG',
                                options={'quality': 60})
    order = models.PositiveIntegerField(_('Order'), default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.image.name


class Blog(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_('Title'), max_length=200),
        slug=AutoSlugField(populate_from='title', unique=True),
        author=models.ForeignKey('accounts.User', related_name='author_blogs'),
        content=RichTextUploadingField(verbose_name=_('Content')),
        short_description=RichTextUploadingField(verbose_name=_('Short Description')),
        publication_date=models.DateField(_('Publication Date')),
    )
    category = models.ForeignKey('Category', verbose_name=_('Category'))
    tags = models.ManyToManyField('Tag', )
    images = models.ManyToManyField('BlogImage', )
    order = models.PositiveIntegerField(_('Order'), default=0)
    is_active = models.BooleanField(_('Is Active'), default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
