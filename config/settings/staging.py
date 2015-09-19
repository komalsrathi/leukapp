# -*- coding: utf-8 -*-
'''
Staging Configurations
'''
from __future__ import absolute_import, unicode_literals

from django.utils import six

from .common import *  # noqa

# SECRET CONFIGURATION
# -----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env("DJANGO_SECRET_KEY",
    default='CHANGEME!!!lp#7%-y6+lsk0yv$9d-22=n^ab8x5hkb!(#d$u2vi5+2-2w&@@')

# STATIC FILE CONFIGURATION
# -----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR('../static'))

# DATABASE CONFIGURATION
# -----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
# Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
DATABASES['default'] = env.db("DATABASE_URL", default="postgres:///staging")

# SITE CONFIGURATION
# -----------------------------------------------------------------------------
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS',
                         default=['172.22.232.109:8000', '172.22.232.109'])
# END SITE CONFIGURATION
