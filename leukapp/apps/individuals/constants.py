# -*- coding: utf-8 -*-
"""
individuals app constants
"""

# app name
APP_NAME = 'individuals'

# urls
INDIVIDUAL_CREATE_URL = APP_NAME + ':create'
INDIVIDUAL_LIST_URL = APP_NAME + ':list'

# models fields
INDIVIDUAL_CREATE_FIELDS = (
    'institution',
    'species',
    'ext_id',
    )

INDIVIDUAL_UPDATE_FIELDS = (
    'institution',
    'species',
    )

INDIVIDUAL_UNIQUE_TOGETHER = (
    'institution',
    'species',
    'ext_id',
    )

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

SPECIES_SHORT = [s[0] for s in SPECIES]
INSTITUTION_SHORT = [i[0] for i in INSTITUTION]
