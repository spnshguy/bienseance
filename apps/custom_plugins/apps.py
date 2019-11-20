from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CustomPluginsConfig(AppConfig):
    name = 'apps.custom_plugins'
    verbose_name = _("Custom Plugins")
