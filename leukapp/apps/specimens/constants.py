# -*- coding: utf-8 -*-

"""
specimens app constants
"""

# leukapp
from leukapp.apps.core import constants as coreconstants

# APP INFO
# -----------------------------------------------------------------------------
APP_NAME = 'specimens'

# URLS
# -----------------------------------------------------------------------------
SPECIMEN_CREATE_URL = APP_NAME + ':create'
SPECIMEN_LIST_URL = APP_NAME + ':list'

# FIELDS
# -----------------------------------------------------------------------------
SPECIMEN_CREATE_FIELDS = (
    'individual',
    'source',
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

# CHOICES
# -----------------------------------------------------------------------------
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

LEUKID_SOURCE_TYPE = {
    TUMOR: 'T',
    NORMAL: 'N',
    }

# PERMISSIONS
# -----------------------------------------------------------------------------
SPECIMEN_CREATE_PERMISSIONS = ('specimens.add_specimen',)
SPECIMEN_UPDATE_PERMISSIONS = ('specimens.change_specimen',)

# MESSAGES
# -----------------------------------------------------------------------------
SUCCESS_MESSAGE = coreconstants.SUCCESS_MESSAGE
PERMISSION_DENIED_MESSAGE = coreconstants.PERMISSION_DENIED_MESSAGE
