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

INDIVIDUAL_LEUKFORM_FIELDS = (
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
OTHER = 'OTHER'
INSTITUTION = (
    (MSK, 'Memorial Sloan-Kettering Cancer Center'),
    (OTHER, 'Other'),
    )
INSTITUTION_VALUE = [s[0] for s in INSTITUTION]

HUMAN = 'HUMAN'
MOUSE = 'MOUSE'
YEAST = 'YEAST'
ZEBRAFISH = 'ZEBRAFISH'
XENOGRAFT = 'XENOGRAFT'
SPECIES = (
    (HUMAN, 'Human'),
    (MOUSE, 'Mouse'),
    (YEAST, 'Yeast'),
    (ZEBRAFISH, 'Zebrafish'),
    (XENOGRAFT, 'Xenograft'),
    )
SPECIES_VALUE = [i[0] for i in SPECIES]

INDIVIDUAL_CHOICES = {
    "INSTITUTION": INSTITUTION,
    "SPECIES": SPECIES,
    }

LEUKID_SPECIES = {
    HUMAN: 'H',
    MOUSE: 'M',
    YEAST: 'Y',
    ZEBRAFISH: 'Z',
    XENOGRAFT: 'X',
    }
