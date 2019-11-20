import importlib
import warnings

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from .exceptions import MailchimpWarning


def get_callable(string_to_callable):
    module_name, object_name = string_to_callable.rsplit('.', 1)
    module = importlib.import_module(module_name)
    return getattr(module, object_name)


API_KEY = getattr(settings, 'MAILCHIMP_API_KEY', None)

if API_KEY is None:
    raise ImproperlyConfigured('django-mailchimp requires the MAILCHIMP_API_KEY setting')

SECURE = getattr(settings, 'MAILCHIMP_SECURE', True)

REAL_CACHE = False
CACHE_TIMEOUT = getattr(settings, 'MAILCHIMP_CACHE_TIMEOUT', 300)

WEBHOOK_KEY = getattr(settings, 'MAILCHIMP_WEBHOOK_KEY', '')
if not WEBHOOK_KEY:
    warnings.warn("you did not define a MAILCHIMP_WEBHOOK_KEY setting. "
        "django-mailchimp will create a random one by itself", MailchimpWarning)
    import string
    import random
    alphanum = string.ascii_letters + string.digits
    for x in range(50):
        WEBHOOK_KEY += random.choice(alphanum)
