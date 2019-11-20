from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class HomeApp(CMSApp):
    name = _('Home App')
    app_name = "home"


    def get_urls(self, page=None, language=None, **kwargs):
        return ["apps.front.urls"]


apphook_pool.register(HomeApp)
