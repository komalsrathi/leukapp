# -*- coding: utf-8 -*-
'''
Local test configuration

'''
from __future__ import absolute_import, unicode_literals
from .common import *  # noqa


# DATABASE CONFIGURATION
# =============================================================================
# Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
DATABASES['default'] = env.db("DATABASE_TEST_URL", default="test")

# SECRET CONFIGURATION
# =============================================================================
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env("DJANGO_SECRET_KEY",
    default='CHANGEME!!!lp#7%-y6+lsk0yv$9d-22=n^ab8x5hkb!(#d$u2vi5+2-2w&@@')
