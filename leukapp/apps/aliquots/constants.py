# -*- coding: utf-8 -*-

"""
specimens app constants
"""

# APP INFO
# -----------------------------------------------------------------------------
APP_NAME = 'aliquots'

# URLS
# -----------------------------------------------------------------------------
ALIQUOT_CREATE_URL = APP_NAME + ':create'
ALIQUOT_LIST_URL = APP_NAME + ':list'

# FIELDS
# -----------------------------------------------------------------------------
ALIQUOT_CREATE_FIELDS = (
    'specimen',
    'bio_source',
    'ext_id',
    )

ALIQUOT_LEUKFORM_FIELDS = (
    'bio_source',
    'ext_id',
    )

ALIQUOT_UPDATE_FIELDS = (
    )

ALIQUOT_UNIQUE_TOGETHER = (
    'specimen',
    'bio_source',
    'ext_id',
    )

# CHOICES
# -----------------------------------------------------------------------------
DNA = 'DNA'
RNA = 'RNA'
BIO_SOURCE = (
    (DNA, 'DNA'),
    (RNA, 'RNA'),
    )
BIO_SOURCE_VALUE = [b[0] for b in BIO_SOURCE]

ALIQUOT_CHOICES = {
    "BIO_SOURCE": BIO_SOURCE,
    }

LEUKID_BIO_SOURCE = {
    DNA: 'D',
    RNA: 'R',
    }

# PERMISSIONS
# -----------------------------------------------------------------------------
ALIQUOT_CREATE_PERMISSIONS = ('aliquots.add_aliquot',)
ALIQUOT_UPDATE_PERMISSIONS = ('aliquots.change_aliquot',)

# MESSAGES
# -----------------------------------------------------------------------------
SUCCESS_MESSAGE = "Looking good"
PERMISSION_DENIED_MESSAGE = \
    '''
    You don't have permission to perform this action, please contact a Leukgen
    Administrator
    '''
