from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from apps.custom_plugins.models import SocialNetwork, TextField, HeroBackgroundImage, ButtonField, EventCard


class SocialNetworkPlugin(CMSPluginBase):
    model = SocialNetwork
    name = _("Social Network")
    render_template = "custom_plugins/_social_network.html"


class TextFieldPlugin(CMSPluginBase):
    model = TextField
    name = _("Text field")
    render_template = "custom_plugins/_text_field_plugin.html"


class HeroBackgroundImagePlugin(CMSPluginBase):
    model = HeroBackgroundImage
    name = _("Hero Background Image")
    render_template = "custom_plugins/_hero_background_image.html"

class PageImagePlugin(CMSPluginBase):
    model = HeroBackgroundImage
    name = _("Page Image")
    render_template = "custom_plugins/_hero_background_image.html"


class ButtonPlugin(CMSPluginBase):
    model = ButtonField
    name = _("Button Field")
    render_template = "custom_plugins/_button.html"


class EventCardPlugin(CMSPluginBase):
    model = EventCard
    name = _("Event Card")
    render_template = "custom_plugins/_event_card.html"


plugin_pool.register_plugin(SocialNetworkPlugin)
plugin_pool.register_plugin(TextFieldPlugin)
plugin_pool.register_plugin(HeroBackgroundImagePlugin)
plugin_pool.register_plugin(ButtonPlugin)
plugin_pool.register_plugin(EventCardPlugin)
plugin_pool.register_plugin(PageImagePlugin)
