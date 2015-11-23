# -*- coding: utf-8 -*-

"""
This module contains the :mod:`~leukapp.apps.participants` app constants.
Information that isn't likely to change and that is used across the
:mod:`~leukapp.apps.participants` app and the :mod:`~leukapp` project
should be stored here.

.. important::
    **DO NOT** change any constant unless you know what you are doing.
"""

# leukapp
from leukapp.apps.core import constants as coreconstants

# APP INFO
# -----------------------------------------------------------------------------
APP_NAME = 'participants'  #: Application's name.

# URLS
# -----------------------------------------------------------------------------
PARTICIPANT_CREATE_URL = APP_NAME + ':create'  #: Create URL reverse string.
PARTICIPANT_LIST_URL = APP_NAME + ':list'      #: List URL reverse string.

# FIELDS
# -----------------------------------------------------------------------------

#: Fields required to create a new instance.
PARTICIPANT_CREATE_FIELDS = (
    'first_name',
    'last_name',
    'email',
    'phone',
    )

#: Enabled fields to update an existing instance.
PARTICIPANT_UPDATE_FIELDS = (
    'first_name',
    'last_name',
    'phone',
    )

#: Fields that are required to be unique together.
PARTICIPANT_UNIQUE_TOGETHER = (
    'email',
    )

# PERMISSIONS
# -----------------------------------------------------------------------------

#: Tuple of permissions required to create a new instance.
PARTICIPANT_CREATE_PERMISSIONS = ('participants.add_participant',)

#: Tuple of permissions required to update an existing instance.
PARTICIPANT_UPDATE_PERMISSIONS = ('participants.change_participant',)

# MESSAGES
# -----------------------------------------------------------------------------

#: Sucess message.
SUCCESS_MESSAGE = coreconstants.SUCCESS_MESSAGE

#: Permission denied message.
PERMISSION_DENIED_MESSAGE = coreconstants.PERMISSION_DENIED_MESSAGE
