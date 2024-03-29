# -*- coding: utf-8 -*-
"""
Django settings for leukapp project.
For more information on this file, see `Django settings`_.
For the full list of settings and their values, see `settings reference`_:

.. _Django settings: https://docs.djangoproject.com/en/dev/topics/settings/
.. _settings reference: https://docs.djangoproject.com/en/dev/ref/settings/
"""

# python
from __future__ import absolute_import, unicode_literals
import sys

# third party
import environ

env = environ.Env()

# SET FUNDAMENTAL DIRECTORIES
# =============================================================================

ROOT_DIR = environ.Path(__file__) - 3  # (/a/b/myfile.py - 3 = /)
"""

.. autoclass:: django.core.exceptions.FieldDoesNotExist

Project Root directory.

``ROOT_DIR`` includes::

    .
    ├── config              # Global app settings
    ├── deploy              # Deploy scripts and templates
    ├── docs                # Documentation
    ├── leukapp             # Django applications
    ├── requirements        # Python  environment requirements
    └── tests               # Project level tests
"""

PROJECT_DIR = ROOT_DIR.path('leukapp')  #: Leukapp project directory
APPS_DIR = PROJECT_DIR.path('apps')     #: Leukapp APPs directory

# DETECT TESTING ENVIRONMENT
# =============================================================================

#: ``True`` if testing environment is active.
TESTING = len(sys.argv) > 1 and sys.argv[1] == 'test'

# APP CONFIGURATION
# =============================================================================
DJANGO_APPS = (
    'django.contrib.auth',          # Django auth
    'django.contrib.contenttypes',  # Django Content Tyes
    'django.contrib.sessions',      # Django sessions
    'django.contrib.messages',      # Django Messages
    'django.contrib.staticfiles',   # Static Files
    'django.contrib.admin',         # Django Default Admin suit
    'django.contrib.humanize',      # Useful template tags
    'django.contrib.sites',         # Django Sites required by allauth
    )

THIRD_PARTY_APPS = (
    'crispy_forms',                 # Form layouts
    'allauth',                      # Registration
    'allauth.account',              # Registration
    'allauth.socialaccount',        # Registration
    'django_modalview',             # Modals CBV
    'rest_framework',               # API rest framework
    'django_filters',               # Filters for API
    'autocomplete_light',           # Autocomplete
    )
"""
Leukapp third party applications.

See for full documentation at:

    * `crispy_forms`_: Form layouts
    * `allauth`_: Registration
    * `django_modalview`_: Modals CBV
    * `rest_framework`_: API rest framework
    * `django_filters`_: Filters for API
    * `autocomplete_light`_: Autocomplete

.. _crispy_forms: http://django-crispy-forms.readthedocs.org/en/latest/
.. _allauth: http://django-allauth.readthedocs.org/en/latest/
.. _django_modalview: https://github.com/optiflows/django-modalview
.. _rest_framework: http://www.django-rest-framework.org/
.. _django_filters: http://django-filter.readthedocs.org/en/latest/usage.html
.. _autocomplete_light:
    https://django-autocomplete-light.readthedocs.org/en/master/
"""

LOCAL_APPS = (
    'leukapp.apps.users',  # custom users app
    'leukapp.apps.lists',
    'leukapp.apps.projects',
    'leukapp.apps.individuals',
    'leukapp.apps.specimens',
    'leukapp.apps.aliquots',
    'leukapp.apps.participants',
    'leukapp.apps.core',
    'leukapp.apps.extractions',
    'leukapp.apps.workflows',
    'leukapp.apps.leukforms',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE CONFIGURATION
# =============================================================================
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# MIGRATIONS CONFIGURATION
# =============================================================================
MIGRATION_MODULES = {
    'sites': 'leukapp.contrib.sites.migrations'
}

# DEBUG
# =============================================================================
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", False)

# FIXTURE CONFIGURATION
# =============================================================================
# See:
# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    str(PROJECT_DIR.path('fixtures')),
)

# EMAIL CONFIGURATION
# =============================================================================
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
                    default='django.core.mail.backends.smtp.EmailBackend')

# MANAGER CONFIGURATION
# =============================================================================
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ("""Juan Medina""", 'medinaj@mskcc.org'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# DATABASE CONFIGURATION
# =============================================================================
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
    'default': env.db("DATABASE_URL", default="postgres:///leukapp"),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True


# GENERAL CONFIGURATION
# =============================================================================

TIME_ZONE = 'America/New_York'
"""
Local time zone for this installation. Choices can be found `here`_.
although not all choices may be available on all operating systems.
In a Windows environment this must be set to your system time zone.

.. _here: http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
"""

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

# TEMPLATE CONFIGURATION
# =============================================================================

# See: http://django-crispy-forms.readthedocs.org/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        'DIRS': [
            str(PROJECT_DIR.path('templates')),
        ],
        'OPTIONS': {

            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            'debug': DEBUG,

            # See:
            #https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],

            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',

                # Your stuff: custom template context processors go here
            ],
        },
    },
]

# STATIC FILE CONFIGURATION
# =============================================================================

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATIC_ROOT = str(ROOT_DIR('staticfiles'))
"""
Static files root directory.

Directory where static files will be saved during production.
For more information, see: `STATIC_ROOT`_.

.. _STATIC_ROOT:
    https://docs.djangoproject.com/en/dev/ref/settings/#static-root
"""

STATICFILES_DIRS = (
    str(PROJECT_DIR.path('static')),
)
"""
Static files directory.

This is where the template tag {% static %} will look for static files during
local development. For more information, see: `STATICFILES_DIRS`_.

.. _STATICFILES_DIRS:
    https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
"""

# MEDIA CONFIGURATION
# =============================================================================

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

MEDIA_ROOT = str(PROJECT_DIR('media'))
"""
Media root directory.

Media files are saved here. For more information, see: `MEDIA_ROOT`_.

.. _MEDIA_ROOT: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
"""

# URL Configuration
# =============================================================================
ROOT_URLCONF = 'config.urls'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'

# AUTHENTICATION CONFIGURATION
# =============================================================================
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Some really nice defaults
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_FORM_CLASS = 'leukapp.apps.users.forms.SignupForm'

# Custom user app defaults
# Select the correct user model
AUTH_USER_MODEL = 'users.User'
LOGIN_REDIRECT_URL = 'users:redirect'
LOGIN_URL = 'account_login'

# SLUGLIFIER
AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify'


# LOGGING CONFIGURATION
# =============================================================================
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'loggers': {
            'django.security.DisallowedHost': {
                'level': 'ERROR',
                'handlers': ['console', 'mail_admins'],
                'propagate': True,
            },
        },
    }
}

# Your common stuff: Below this line define 3rd party library settings

# DJANGO REST FRAMEWORK
# =============================================================================

# See: http://www.django-rest-framework.org/api-guide/authentication/
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
}

# ROUTINE PROTECTION
# =============================================================================

if __name__ == '__main__':
    pass
