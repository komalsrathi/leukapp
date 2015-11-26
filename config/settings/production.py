# -*- coding: utf-8 -*-
"""
Production Configurations
    - Use djangosecure
"""

# python
from __future__ import absolute_import, unicode_literals

# local
from .common import *  # noqa

# SECRET CONFIGURATION
# =============================================================================

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default='CHANGEME!!!lp#7%-y6+lsk0yv$9d-22=n^ab8x5hkb!(#d$u2vi5+2-2w&@@'
    )
"""
Raises ImproperlyConfigured exception if DJANGO_SECRET_KEY not in os.environ.
For more information, see `secret key`.
.. _secret key: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
"""

# MIDDLEWARE SECURITY
# =============================================================================
SECURITY_MIDDLEWARE = ('django.middleware.security.SecurityMiddleware', )
MIDDLEWARE_CLASSES = SECURITY_MIDDLEWARE + MIDDLEWARE_CLASSES


# SECURITY SETTINGS
# =============================================================================
SECURE_HSTS_SECONDS = 60
"""
Set to 60 seconds, then to 518400 when you are sure that everything works.
"""

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
"""
.. todo: Please describe this setting
"""

SECURE_SSL_REDIRECT = env.bool(
    "DJANGO_SECURE_SSL_REDIRECT", default=True)
"""
See this `question`_.

.. _question: http://stackoverflow.com/questions/33792940/django-application-crash-with-secure-ssl-redirect-using-nginx
"""

SECURE_FRAME_DENY = env.bool(
    "DJANGO_SECURE_FRAME_DENY", default=True)
"""
.. todo: Please describe this setting
"""

SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True)
"""
.. todo: Please describe this setting
"""

SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    "DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True)
"""
.. todo: Please describe this setting
"""

SECURE_BROWSER_XSS_FILTER = env.bool(
    "DJANGO_SECURE_BROWSER_XSS_FILTER", default=True)
"""
.. todo: Please describe this setting
"""

SESSION_COOKIE_SECURE = env.bool(
    "DJANGO_SESSION_COOKIE_SECURE", default=True)
"""
.. todo: Please describe this setting
"""

SESSION_COOKIE_HTTPONLY = env.bool(
    "DJANGO_SESSION_COOKIE_HTTPONLY", default=True)
"""
.. todo: Please describe this setting
"""

CSRF_COOKIE_SECURE = env.bool(
    "DJANGO_CSRF_COOKIE_SECURE", default=False)
"""
.. todo: Please describe this setting
"""

CSRF_COOKIE_HTTPONLY = env.bool(
    "DJANGO_CSRF_COOKIE_HTTPONLY", default=True)
"""
.. todo: Please describe this setting
"""

X_FRAME_OPTIONS = env(
    "DJANGO_X_FRAME_OPTIONS", default='DENY')
"""
.. todo: Please describe this setting
"""

# SITE CONFIGURATION
# =============================================================================

ALLOWED_HOSTS = env.list(
    'DJANGO_ALLOWED_HOSTS', default=['leukgen.mskcc.org'])
"""
Hosts/domain names that are valid for this site
See `allowed hosts`_

.. _allowed hosts:
    https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
"""

# APP CONFIGURATION
# =============================================================================
INSTALLED_APPS += ("gunicorn", )

# STATIC FILES
# =============================================================================
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# EMAIL
# =============================================================================

DEFAULT_FROM_EMAIL = env(
    'DJANGO_DEFAULT_FROM_EMAIL', default='leukapp <noreply@leukgen.mskcc.org>')
"""
.. todo: Please describe this setting
"""

EMAIL_SUBJECT_PREFIX = env(
    "DJANGO_EMAIL_SUBJECT_PREFIX", default='[leukapp] ')
"""
.. todo: Please describe this setting
"""

SERVER_EMAIL = env(
    'DJANGO_SERVER_EMAIL', default=DEFAULT_FROM_EMAIL)
"""
.. todo: Please describe this setting
"""

# TEMPLATE CONFIGURATION
# =============================================================================
# See:
# https://docs.djangoproject.com/en/dev/ref/templates/api/#django.template.loaders.cached.Loader
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader',
        ['django.template.loaders.filesystem.Loader',
         'django.template.loaders.app_directories.Loader']),
]

# DATABASE CONFIGURATION
# =============================================================================

DATABASES['default'] = env.db(
    "DATABASE_URL", default="postgres:///production")
"""
Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
"""

# CACHING
# =============================================================================
# Heroku URL does not pass the DB number, so we parse it in
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "{0}/{1}".format(
            env.cache_url('REDIS_URL', default="redis://127.0.0.1:6379"), 0),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "IGNORE_EXCEPTIONS": True,  # mimics memcache behavior.
                                        # http://niwinz.github.io/django-redis/latest/#_memcached_exceptions_behavior
        }
    }
}

# Your production stuff: Below this line define 3rd party library settings
