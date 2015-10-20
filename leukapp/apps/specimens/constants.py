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
    'source_type',
    'ext_id',
    ]

SPECIMEN_UPDATE_FIELDS = [
    'source',
    ]

SPECIMEN_GET_OR_CREATE_FIELDS = (
    'individual',
    'ext_id',
    )

# choices

BLOOD = 'Blood'
NAILS = 'Nails'
BUCCAL = 'Buccal'
HAIR = 'Hair'
TCELLS = 'T-Cells'
SOURCE = (
    (BLOOD, 'Blood'),
    (NAILS, 'Nails'),
    (BUCCAL, 'Buccal'),
    (HAIR, 'Hair'),
    (TCELLS, 'T-Cells'),
)

TUMOR = 'T'
NORMAL = 'N'
SOURCE_TYPE = (
    (TUMOR, 'Tumor'),
    (NORMAL, 'Normal'),
)

SPECIMEN_CHOICES = {
    "SOURCE": SOURCE,
    "SOURCE_TYPE": SOURCE_TYPE,
}

SOURCE_SHORT = [s[0] for s in SOURCE]
SOURCE_TYPE_SHORT = [s[0] for s in SOURCE_TYPE]
