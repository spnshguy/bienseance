import uuid

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from cms.models import CMSPlugin, Title
from django.db import models
from django.utils.html import strip_tags
from django.utils.text import Truncator
from django.utils.translation import ugettext_lazy as _
from imagekit.processors import ResizeToFit

from apps.custom_plugins.validation import ValidateImageFile


class SocialNetwork(CMSPlugin):
    FACEBOOK, INSTAGRAM, LINKEDIN, TWITTER = range(4)
    SOCIAL_NETWORKS_CHOICES = (
        (FACEBOOK, _('Facebook')),
        (INSTAGRAM, _('Instagram')),
        (LINKEDIN, _('LinkedIn')),
        (TWITTER, _('Twitter')),
    )
    social_network = models.IntegerField(_('Social Network'), choices=SOCIAL_NETWORKS_CHOICES)
    url = models.URLField(_('URL'))

    def __str__(self):
        return self.get_social_network_display()


class HeroBackgroundImage(CMSPlugin):
    photo = ValidateImageFile(
        verbose_name=_('Image'),
        upload_to='cms', processors=[
            ResizeToFit(1600, None, False)],
        format='JPEG',
        options={
            'quality': 100})

    def __str__(self):
        return self.photo.name

    @property
    def get_url(self):
        return self.photo.url


class ButtonField(CMSPlugin):
    link = models.URLField(_('Url'))
    text = models.CharField(_('Text'), max_length=30)

    def __str__(self):
        return self.link


class EventCard(CMSPlugin):
    title = models.CharField(_('Title'), max_length=20)
    date_range = models.CharField(_('Dates'), max_length=20)
    location = RichTextField()
    time = models.CharField(_('Time'), max_length=100)

    def __str__(self):
        return self.title


class TextField(CMSPlugin):
    body = RichTextUploadingField()

    def __str__(self):
        if self.body:
            return Truncator(strip_tags(self.body).replace('&shy;', '')).words(3, truncate="...")
