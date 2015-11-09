# -*- coding: utf-8 -*-
"""
projects app constants
"""

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
    'name',
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
    'name',
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
    'name',
    )

# MESSAGES
# -----------------------------------------------------------------------------
PERMISSION_DENIED_MESSAGE = \
    '''
    You don't have permission to perform this action, please contact a Leukgen
    Administrator
    '''
