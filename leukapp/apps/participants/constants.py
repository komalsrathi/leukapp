# -*- coding: utf-8 -*-
"""
individuals app constants
"""
# app name
APP_NAME = 'participants'

# urls
CREATE_URL = APP_NAME + ':create'
LIST_URL = APP_NAME + ':list'

# model fields

PARTICIPANT_CREATE_FIELDS = [
    'first_name',
    'last_name',
    'email',
    'phone',
    ]

PARTICIPANT_UPDATE_FIELDS = [
    'first_name',
    'last_name',
    'phone',
    ]

PARTICIPANT_GET_OR_CREATE_FIELDS = (
    'email',
    )
