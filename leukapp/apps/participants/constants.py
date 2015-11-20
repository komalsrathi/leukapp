# -*- coding: utf-8 -*-
"""
individuals app constants
"""

# leukapp
from leukapp.apps.core import constants as coreconstants

# APP INFO
# -----------------------------------------------------------------------------
APP_NAME = 'participants'

# URLS
# -----------------------------------------------------------------------------
PARTICIPANT_CREATE_URL = APP_NAME + ':create'
PARTICIPANT_LIST_URL = APP_NAME + ':list'

# FIELDS
# -----------------------------------------------------------------------------
PARTICIPANT_CREATE_FIELDS = (
    'first_name',
    'last_name',
    'email',
    'phone',
    )

PARTICIPANT_UPDATE_FIELDS = (
    'first_name',
    'last_name',
    'phone',
    )

PARTICIPANT_UNIQUE_TOGETHER = (
    'email',
    )

# PERMISSIONS
# -----------------------------------------------------------------------------
PARTICIPANT_CREATE_PERMISSIONS = ('participants.add_participant',)
PARTICIPANT_UPDATE_PERMISSIONS = ('participants.change_participant',)

# MESSAGES
# -----------------------------------------------------------------------------
SUCCESS_MESSAGE = coreconstants.SUCCESS_MESSAGE
PERMISSION_DENIED_MESSAGE = coreconstants.PERMISSION_DENIED_MESSAGE
