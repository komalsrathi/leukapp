# -*- coding: utf-8 -*-
"""
Individuals app constants
"""

# app name
APP_NAME = 'individuals'

# urls
CREATE_URL = APP_NAME + ':create'
LIST_URL = APP_NAME + ':list'

# model fields
INDIVIDUAL_CREATE_FIELDS = [
    'institution',
    'species',
    'ext_id',
    ]

INDIVIDUAL_UPDATE_FIELDS = [
    'institution',
    'species',
    ]

# choices
MSK = 'MSK'
OTHER = 'O'
INSTITUTION = (
    (MSK, 'Memorial Sloan-Kettering Cancer Center'),
    (OTHER, 'Other'),
    )

HUMAN = 'H'
MOUSE = 'M'
YEAST = 'Y'
ZEBRAFISH = 'Z'
SPECIES = (
    (HUMAN, 'Human'),
    (MOUSE, 'Mouse'),
    (YEAST, 'Yeast'),
    (ZEBRAFISH, 'Zebrafish'),
    )

INDIVIDUAL_CHOICES = {
    "INSTITUTION": INSTITUTION,
    "SPECIES": SPECIES,
    }
