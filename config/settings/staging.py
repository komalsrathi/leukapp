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
# -----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Raises ImproperlyConfigured exception if DJANGO_SECRET_KEY not in os.environ
SECRET_KEY = env("DJANGO_SECRET_KEY")

# This ensures that Django will be able to detect a secure connection
# properly on Heroku.


# MIDDLEWARE SECURITY
# -----------------------------------------------------------------------------
SECURITY_MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
)

MIDDLEWARE_CLASSES = SECURITY_MIDDLEWARE + MIDDLEWARE_CLASSES
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')


# changes suggested by python manage.py check --deploy
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'SAMEORIGIN'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)


"""
# SecurityMiddleware settings
# set this to 60 seconds and then to 518400 when you can prove it works
SECURE_HSTS_SECONDS = 60
SECURE_BROWSER_XSS_FILTER = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True)
SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    "DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True)
"""

# SITE CONFIGURATION
# -----------------------------------------------------------------------------
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['leukgen.mskcc.org'])

# APP CONFIGURATION
# -----------------------------------------------------------------------------
INSTALLED_APPS += ("gunicorn", )

# STATIC FILES
# -----------------------------------------------------------------------------
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# EMAIL
# -----------------------------------------------------------------------------
DEFAULT_FROM_EMAIL = env('DJANGO_DEFAULT_FROM_EMAIL',
                         default='leukapp <noreply@leukgen.mskcc.org>')
EMAIL_SUBJECT_PREFIX = env("DJANGO_EMAIL_SUBJECT_PREFIX", default='[leukapp] ')

# TEMPLATE CONFIGURATION
# -----------------------------------------------------------------------------
# See:
# https://docs.djangoproject.com/en/dev/ref/templates/api/#django.template.loaders.cached.Loader
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader',
        ['django.template.loaders.filesystem.Loader',
         'django.template.loaders.app_directories.Loader']),
]

# DATABASE CONFIGURATION
# -----------------------------------------------------------------------------
# Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
DATABASES['default'] = env.db("DATABASE_URL")

# CACHING
# -----------------------------------------------------------------------------
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
