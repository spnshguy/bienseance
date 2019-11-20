# coding: UTF-8
from os import path
import os

from distutils.util import strtobool


INSTALLED_APPS = (

    'apps.cms_named_menus',
    'apps.accounts',

    'parler',
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    # SITE-PACKAGE
    'debug_toolbar',
    'crispy_forms',
    'cms',
    'menus',
    'treebeard',
    'sekizai',
    'imagekit',
    'sortedm2m',
    'ckeditor',
    'ckeditor_uploader',
    'djangocms_picture',
    'easy_thumbnails',
    'filer',
    'mptt',
    'nested_admin',
    'compat',
    'hijack',
    'hijack_admin',
    'django_instagram',
    'constance',
    'constance.backends.database',

    # LIBS
    'libs.startup',
    'libs.mailchimp',

    # APPS
    'apps.custom_admin',
    'apps.custom_plugins',
    'apps.blogs',
    'apps.front',
    'apps.products',
    'apps.quotes',
    'apps.cart',

)
from django.utils.translation import ugettext_lazy as _

ALLOWED_HOSTS = os.environ.get('BIEN_ALLOWED_HOSTS', '127.0.0.1,0.0.0.0,localhost,192.168.2.27,192.168.2.22,192.168.0.118')
ALLOWED_HOSTS = ALLOWED_HOSTS.split(',')

ADMINS = (
    ('Dev', 'dev@bienseance.ca'),
)

PROJECT_PROTOCOL = '//'
PROJECT_DOMAIN = '127.0.0.1:8000'
PROJECT_URI = "".join((PROJECT_PROTOCOL, PROJECT_DOMAIN))
PROJECT_TITLE = "Bienseance"
PROJECT_CONTACT = "contact@bienseance.com"
PROJECT_SETTINGS = path.dirname(__file__)
BASE_DIR = path.dirname(PROJECT_SETTINGS)
PROJECT_NAME = path.basename(PROJECT_SETTINGS)
SITE_ID = 1

# Send insecure requests to https
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = bool(strtobool(os.environ.get('BIEN_SSL_REDIRECT', 'False')))

DEBUG = bool(strtobool(os.environ.get('BIEN_DEBUG', 'True')))

LANGUAGE_CODE = "fr"
LANGUAGES = (
    ('fr', 'Français'),
    ('en', 'English'),
)

TIME_ZONE = 'US/Eastern'
USE_I18N = True
USE_L10N = True
USE_TZ = True

WSGI_APPLICATION = '%s.wsgi.application' % PROJECT_NAME

ROOT_URLCONF = '%s.urls' % PROJECT_NAME
STATIC_URL = '/static/'
STATIC_ROOT = path.normpath(path.join(BASE_DIR, 'static'))
MEDIA_URL = '/media/'
MEDIA_ROOT = path.join(BASE_DIR, 'media')
FIXTURE_DIRS = 'fixtures/',
LOCALE_PATHS = 'locale/',
CRISPY_TEMPLATE_PACK = 'bootstrap3'

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'solid_i18n.middleware.SolidLocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',

)

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bienseance',
        'USER': os.environ.get('BIEN_DATABASE_USER', 'postgres'),
        'PASSWORD': os.environ.get('BIEN_DATABASE_PASSWORD', 'a'),
        'HOST': os.environ.get('BIEN_DATABASE_HOST', '127.0.0.1'),
        'PORT': os.environ.get('BIEN_DATABASE_PORT', '5432'),
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ('templates/',),
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'apps.products.context_processors.ga_tracking_id',
                'apps.products.context_processors.latest_magazine',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
                'django.template.context_processors.static',
                'constance.context_processors.config',

            ]
        },
    },
]

# CACHES = {
#     "default": {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         "LOCATION": "redis://redis:6379/0",
#         'TIMEOUT': 300,
#         'KEY_PREFIX': 'django-%s-' % PROJECT_NAME,
#     }
# }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {'()': 'django.utils.log.RequireDebugFalse'},
    },
    'formatters': {
        'simple': {'format': '[%(asctime)s] %(levelname)s: %(message)s'},
        'exhaustive': {'format': '[%(asctime)s] %(pathname)s (L: %(lineno)d); %(levelname)s: %(message)s'},
    },
    'loggers': {
        'django.security.DisallowedHost': {
            'handlers': ['null', ],
            'propagate': False,
        },
        'main': {
            'level': 'DEBUG',
            'propagate': True,
            'handlers': os.environ.get('BIEN_LOG_DEBUG_HANDLERS', 'console,main_file,mail_admins').split(','),
        },
        'django.request': {
            'level': 'ERROR',
            'propagate': True,
            'handlers': os.environ.get('BIEN_LOG_ERROR_HANDLERS', 'main_file,mail_admins').split(','),
        },
        'celery': {
            'level': 'INFO',
            'propagate': True,
            'handlers': os.environ.get('BIEN_LOG_INFO_HANDLERS', 'console,mail_admins').split(','),
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false', ],
        },
        'main_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.environ.get('BIEN_MAIN_LOG', 'logs/main.log'),
            'maxBytes': 1024 * 1024 * 2,
            'backupCount': 2,
            'formatter': 'simple',
        },
    },
}

# EMAIL SETTINGS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'AKIAIDBWOXGJMXPPA4BQ'
EMAIL_HOST_PASSWORD = 'AhAzHCUY4+lzXlAlcs/rGlKHa5LCdN0glgf0OxhCJJde'
EMAIL_USE_TLS = True

ADMIN_EMAIL = 'info@bienseance.ca'

COLOR_BG_HEADER = '#6cb33f'
COLOR_BG_FOOTER = '#171923'
COLOR_TEXT_HEADER = '#fff'
COLOR_TEXT_FOOTER = '#fff'
COLOR_TEXT_LINKS = '#6cb33f'
COLOR_BORDER_HEADER = '#6cb33f'
COLOR_BORDER_BODY = '#AFB6CC'
################


BROKER_URL = 'redis://redis:6379/1'
CELERYD_HIJACK_ROOT_LOGGER = False

show_toolbar = lambda r: False

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": '%s.settings.show_toolbar' % PROJECT_NAME,
}

######################
# Project specific  #
######################


HIJACK_USE_BOOTSTRAP = True
HIJACK_ALLOW_GET_REQUESTS = True
HIJACK_REGISTER_ADMIN = False

HIJACK_LOGIN_REDIRECT_URL = '/?edit=true'  # Where admins are redirected to after hijacking a user
HIJACK_LOGOUT_REDIRECT_URL = '/admin/users/user/'  # Where admins are redirected to after releasing a user

SECRET_KEY = 'thisisasupersecretkey'
STARTUP_INITIAL_FIXTURES = [
    # Respect the order
    'cms',
    'custom_plugins',
]

CMS_TEMPLATES = [
    ('default.html', 'Default page template'),
    ('home.html', 'Home page template'),
    ('about.html', 'About page template'),
    ('blogs/list.html', 'Blog List page template'),
    ('products/list.html', 'Product List page template'),
    ('contact.html', 'Contact page template'),
    ('coming-soon.html', 'Coming Soon page template'),
]

CMS_PERMISSION = True
CMS_MODERATOR = True

CMS_ENABLE_UPDATE_CHECK = False
CMS_LANGUAGES = {
    1: [
        {
            'code': 'fr',
            'name': _('Français'),
            'public': True,
        },
        {
            'code': 'en',
            'name': 'English',
            'fallbacks': ['fr'],
            'public': True,
            'hide_untranslated': True,
            'redirect_on_fallback': True,
        },

    ],
    'default': {
        'fallbacks': ['fr', 'en'],
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    }
}

PARLER_LANGUAGES = {

    1: (
        {'code': 'fr', },
        {'code': 'en', },
    ),
    'default': {
        'fallbacks': ['fr', 'en'],  # defaults to PARLER_DEFAULT_LANGUAGE_CODE
        'hide_untranslated': False,  # the default; let .active_translations() return fallbacks too.
    }
}

CKEDITOR_UPLOAD_PATH = "upload"

CKEDITOR_CONFIGS = {
    'default': {
        'enterMode': 2,
        'shiftEnterMode': 1,
        'forcePasteAsPlainText': True,
        'height': 400,
        'width': 500,
        'toolbar': 'Custom',
        'entities_latin': False,
        'entities': False,
        'format_tags': 'p;h3;h4',
        'toolbar_Custom': [
            ['Source'],
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', 'Undo', 'Redo'],
            ['Find', 'Replace', 'SelectAll'],
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['TextColor', 'lineheight', 'dialog', 'dialogui', 'widget', 'lineutils', 'widget', 'image2'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Table', 'HorizontalRule'],
            ['Format', 'FontSize'],
            ['Maximize'],
        ],
        'extraPlugins': ','.join(
            []
        ),
    },
}

AUTH_USER_MODEL = 'accounts.User'

MAX_UPLOAD_SIZE = 20971520
CONTENT_TYPES = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif']

CMS_PAGE_CACHE = False
CMS_PLACEHOLDER_CACHE = False
CMS_PLACEHOLDER_CONF = {}
DJANGOCMS_PICTURE_RESPONSIVE_IMAGES = False

CMS_PLUGIN_CACHE = False

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    # 'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

MAILCHIMP_API_KEY = 'f637d721205d7dafb0436a2133bc17fa-us19'
MAILCHIMP_SUBSCRIBE_LIST_ID = 'c3a7b2f52c'

USE_THOUSAND_SEPARATOR = True


CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

CONSTANCE_CONFIG = {
    'SHIPPING_COST': (float(0), 'The shipping cost for deliveries'),
    'SHIPPING_EXTRA': (float(0), 'The amount that will be charged for magazine only purchases'),
}

if os.environ.get('BIEN_S3_USE_S3_STORAGE',False):
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    # STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    AWS_ACCESS_KEY_ID = os.environ.get('BIEN_S3_ACCESS_KEY_ID',None)
    AWS_SECRET_ACCESS_KEY = os.environ.get('BIEN_S3_SECRET_ACCESS_KEY',None)
    AWS_STORAGE_BUCKET_NAME = os.environ.get('BIEN_S3_MEDIA_BUCKET_NAME',None)
    AWS_S3_REGION_NAME = os.environ.get('BIEN_S3_REGION_NAME','us-east-2')

    # These are required values for the way the system currently works.
    AWS_DEFAULT_ACL = None
    AWS_S3_SIGNATURE_VERSION = 's3v4'

try:
    from .local_settings import *
except ImportError as e:
    if 'local_settings' not in str(e):
        raise

# Configure the SquareAPI Access keys  Default to the Sandbox values.
BIEN_SQR_ACCESS_TOKEN = os.environ.get('BIEN_SQR_ACCESS_TOKEN', 'sandbox-sq0atb-dc3kN3VLW2G0Lkm_bCtcHA')
BIEN_SQR_LOCATION_ID = os.environ.get('BIEN_SQR_LOCATION_ID', '12tDMXN2yonV07EUiJT2gQfzTG7YY')
BIEN_SQR_REDIRECT_URL = os.environ.get('BIEN_SQR_REDIRECT_URL', 'http://127.0.0.1:8000/payment/success/')

# Hardcoded Projects
BIEN_SLUG_MAG_001 = 'BIE-MAGA-0040-AR'
# BIEN_SLUG_MAG_001 = 'magasine-automne-2018'

BIEN_GA_TRACKING_ID = os.environ.get('BIEN_GA_TRACKING_ID', '')

