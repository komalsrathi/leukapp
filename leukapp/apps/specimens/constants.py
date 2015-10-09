# -*- coding: utf-8 -*-

"""
specimens app constants
"""

# app name
APP_NAME = 'specimens'

#  urls
SPECIMEN_CREATE_URL = APP_NAME + ':create'
SPECIMEN_LIST_URL = APP_NAME + ':list'

# models fields
SPECIMEN_CREATE_FIELDS = [
    'individual',
    'source',
    'ext_id',
    ]

SPECIMEN_UPDATE_FIELDS = [
    'individual',
    'source',
    ]

# choices
TUMOR = 'T'
NORMAL = 'N'
SOURCE = (
    (TUMOR, 'Tumor'),
    (NORMAL, 'Normal'),
)

SPECIMEN_CHOICES = {
    "SOURCE": SOURCE,
}
