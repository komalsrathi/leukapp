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
    'biological_material',
    'ext_id',
    ]

ALIQUOT_UPDATE_FIELDS = [
    'specimen',
    'biological_material',
    ]

ALIQUOT_GET_OR_CREATE_FIELDS = (
    'specimen',
    'biological_material',
    'ext_id',
    )

# choices
DNA = 'D'
RNA = 'R'
MIXED = 'M'
BIOLOGICAL_MATERIAL = (
    (DNA, 'DNA'),
    (RNA, 'RNA'),
    (MIXED, 'MIXED'),
)

ALIQUOT_CHOICES = {
    "BIOLOGICAL_MATERIAL": BIOLOGICAL_MATERIAL,
}

BIOLOGICAL_MATERIAL_SHORT = [b[0] for b in BIOLOGICAL_MATERIAL]
