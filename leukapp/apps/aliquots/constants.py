# -*- coding: utf-8 -*-

"""
specimens app constants
"""

# app name
APP_NAME = 'aliquots'

# urls
ALIQUOT_CREATE_URL = APP_NAME + ':create'
ALIQUOT_LIST_URL = APP_NAME + ':list'

# models fields
ALIQUOT_CREATE_FIELDS = [
    'specimen',
    'bio_source',
    'ext_id',
    ]

ALIQUOT_UPDATE_FIELDS = [
    'bio_source',
    ]

ALIQUOT_GET_OR_CREATE_FIELDS = (
    'specimen',
    'bio_source',
    'ext_id',
    )

# choices
DNA = 'D'
RNA = 'R'
BIO_SOURCE = (
    (DNA, 'DNA'),
    (RNA, 'RNA'),
)

ALIQUOT_CHOICES = {
    "BIO_SOURCE": BIO_SOURCE,
}

BIO_SOURCE_SHORT = [b[0] for b in BIO_SOURCE]
