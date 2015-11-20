# -*- coding: utf-8 -*-
"""
projects app constants
"""

# leukapp
from leukapp.apps.core import constants as coreconstants

# APP INFO
# -----------------------------------------------------------------------------
APP_NAME = 'projects'

# URLS
# -----------------------------------------------------------------------------
PROJECT_CREATE_URL = APP_NAME + ':create'
PROJECT_LIST_URL = APP_NAME + ':list'

# FIELDS
# -----------------------------------------------------------------------------
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

PROJECT_UNIQUE_TOGETHER = (
    'title',
    )

# PERMISSIONS
# -----------------------------------------------------------------------------
PROJECT_CREATE_PERMISSIONS = ('projects.add_project',)
PROJECT_UPDATE_PERMISSIONS = ('projects.change_project',)

# MESSAGES
# -----------------------------------------------------------------------------
SUCCESS_MESSAGE = coreconstants.SUCCESS_MESSAGE
PERMISSION_DENIED_MESSAGE = coreconstants.PERMISSION_DENIED_MESSAGE
