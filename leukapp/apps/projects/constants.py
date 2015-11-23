# -*- coding: utf-8 -*-

"""
This module contains the :mod:`~leukapp.apps.projects` app constants.
Information that isn't likely to change and that is used across the
:mod:`~leukapp.apps.projects` app and the :mod:`~leukapp` project
should be stored here.

.. important::
    **DO NOT** change any constant unless you know what you are doing.
"""

# leukapp
from leukapp.apps.core import constants as coreconstants

# APP INFO
# -----------------------------------------------------------------------------
APP_NAME = 'projects'  #: Application's name.

# URLS
# -----------------------------------------------------------------------------
PROJECT_CREATE_URL = APP_NAME + ':create'  #: Create URL reverse string.
PROJECT_LIST_URL = APP_NAME + ':list'      #: List URL reverse string.

# FIELDS
# -----------------------------------------------------------------------------

#: Fields required to create a new instance.
PROJECT_CREATE_FIELDS = (
    'title',
    'description',
    'pi',
    'analyst',
    'requestor',
    'participants',
    'cost_center_no',
    'fund_no',
    'protocol_no',
    )

#: Enabled fields to update an existing instance.
PROJECT_UPDATE_FIELDS = (
    'title',
    'description',
    'pi',
    'analyst',
    'requestor',
    'participants',
    'cost_center_no',
    'fund_no',
    'protocol_no',
    )

#: Fields that are required to be unique together.
PROJECT_UNIQUE_TOGETHER = (
    'title',
    )

# PERMISSIONS
# -----------------------------------------------------------------------------

#: Tuple of permissions required to create a new instance.
PROJECT_CREATE_PERMISSIONS = ('projects.add_project',)

#: Tuple of permissions required to update an existing instance.
PROJECT_UPDATE_PERMISSIONS = ('projects.change_project',)

# MESSAGES
# -----------------------------------------------------------------------------

#: Sucess message.
SUCCESS_MESSAGE = coreconstants.SUCCESS_MESSAGE

#: Permission denied message.
PERMISSION_DENIED_MESSAGE = coreconstants.PERMISSION_DENIED_MESSAGE
