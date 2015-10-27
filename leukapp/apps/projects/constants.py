# -*- coding: utf-8 -*-
"""
projects app constants
"""

# app name
APP_NAME = 'projects'

# urls
PROJECT_CREATE_URL = APP_NAME + ':create'
PROJECT_LIST_URL = APP_NAME + ':list'

# fields
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
