# -*- coding: utf-8 -*-

"""
specimens app constants
"""

# leukapp
from leukapp.apps.core import constants as coreconstants

# APP INFO
# -----------------------------------------------------------------------------
APP_NAME = 'aliquots'

# URLS
# -----------------------------------------------------------------------------
ALIQUOT_CREATE_URL = APP_NAME + ':create'
ALIQUOT_LIST_URL = APP_NAME + ':list'

# FIELDS
# -----------------------------------------------------------------------------
ALIQUOT_CREATE_FIELDS = (
    'specimen',
    'ext_id',
    )

ALIQUOT_UPDATE_FIELDS = (
    )

ALIQUOT_UNIQUE_TOGETHER = (
    'specimen',
    'ext_id',
    )

# CHOICES
# -----------------------------------------------------------------------------
ALIQUOT_CHOICES = {
    }

# PERMISSIONS
# -----------------------------------------------------------------------------
ALIQUOT_CREATE_PERMISSIONS = ('aliquots.add_aliquot',)
ALIQUOT_UPDATE_PERMISSIONS = ('aliquots.change_aliquot',)

# MESSAGES
# -----------------------------------------------------------------------------
SUCCESS_MESSAGE = coreconstants.SUCCESS_MESSAGE
PERMISSION_DENIED_MESSAGE = coreconstants.PERMISSION_DENIED_MESSAGE
