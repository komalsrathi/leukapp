# -*- coding: utf-8 -*-

"""
This module contains the :mod:`~leukapp.apps.aliquots` app constants.
Information that isn't likely to change and that is used across the
:mod:`~leukapp.apps.aliquots` app and the :mod:`~leukapp` project
should be stored here.

.. important::
    **DO NOT** change any constant unless you know what you are doing.
"""

# leukapp
from leukapp.apps.core import constants as coreconstants

# APP INFO
# -----------------------------------------------------------------------------
APP_NAME = 'aliquots'  #: Application's name.

# URLS
# -----------------------------------------------------------------------------
ALIQUOT_CREATE_URL = APP_NAME + ':create'  #: Create URL reverse string.
ALIQUOT_LIST_URL = APP_NAME + ':list'      #: List URL reverse string.

# FIELDS
# -----------------------------------------------------------------------------

#: Fields required to create a new instance.
ALIQUOT_CREATE_FIELDS = (
    'specimen',
    'ext_id',
    )

#: Enabled fields to update an existing instance.
ALIQUOT_UPDATE_FIELDS = (
    )

#: Fields that are required to be unique together.
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

#: Tuple of permissions required to create a new instance.
ALIQUOT_CREATE_PERMISSIONS = ('aliquots.add_aliquot',)

#: Tuple of permissions required to update an existing instance.
ALIQUOT_UPDATE_PERMISSIONS = ('aliquots.change_aliquot',)


# MESSAGES
# -----------------------------------------------------------------------------

#: Sucess message.
SUCCESS_MESSAGE = coreconstants.SUCCESS_MESSAGE

#: Permission denied message.
PERMISSION_DENIED_MESSAGE = coreconstants.PERMISSION_DENIED_MESSAGE
