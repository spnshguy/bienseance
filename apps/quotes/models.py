from django.db import models
from django.utils.translation import ugettext_lazy as _


class Quote(models.Model):
    title = models.CharField(_('Title'), max_length=200)
    author = models.CharField(_('Author'), max_length=200, blank=True)

    def __str__(self):
        return self.title

    @property
    def is_quote(self):
        return True