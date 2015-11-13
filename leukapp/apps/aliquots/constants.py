# -*- coding: utf-8 -*-

"""
specimens app constants
"""

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
SUCCESS_MESSAGE = "Looking good"
PERMISSION_DENIED_MESSAGE = \
    '''
    You don't have permission to perform this action, please contact a Leukgen
    Administrator
    '''
