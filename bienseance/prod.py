import os
from .settings import *

ALLOWED_HOSTS = ['']  # TODO add allowed hosts
PROJECT_PROTOCOL = 'http://'
PROJECT_DOMAIN = ''  # TODO add production domain
PROJECT_URI = "".join((PROJECT_PROTOCOL, PROJECT_DOMAIN))
SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'stderr': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['stderr'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

# removes debug context processor in production.
try:
    TEMPLATES[0]['OPTIONS']['context_processors'].remove('django.template.context_processors.debug')
except ValueError:
    pass
