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
SPECIMEN_CREATE_FIELDS = (
    'individual',
    'source',
    'source_type',
    'ext_id',
    'order',
    )

SPECIMEN_LEUKFORM_FIELDS = (
    'source_type',
    'ext_id',
    'order',
    )

SPECIMEN_UPDATE_FIELDS = (
    'source',
    )

SPECIMEN_UNIQUE_TOGETHER = (
    'individual',
    'ext_id',
    'source_type',
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
SOURCE_VALUE = [s[0] for s in SOURCE]

TUMOR = 'TUMOR'
NORMAL = 'NORMAL'
SOURCE_TYPE = (
    (TUMOR, 'Tumor'),
    (NORMAL, 'Normal'),
)
SOURCE_TYPE_VALUE = [s[0] for s in SOURCE_TYPE]

SPECIMEN_CHOICES = {
    "SOURCE": SOURCE,
    "SOURCE_TYPE": SOURCE_TYPE,
}

LEUKID_SOURCE = {
    TUMOR: 'T',
    NORMAL: 'N',
    }
