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
    'bio_source',
    )

ALIQUOT_UNIQUE_TOGETHER = (
    'specimen',
    'bio_source',
    'ext_id',
    )

# choices
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
