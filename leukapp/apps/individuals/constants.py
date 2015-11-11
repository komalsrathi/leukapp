# -*- coding: utf-8 -*-
"""
individuals app constants
"""

# APP INFO
# -----------------------------------------------------------------------------
APP_NAME = 'individuals'

# URLS
# -----------------------------------------------------------------------------
INDIVIDUAL_CREATE_URL = APP_NAME + ':create'
INDIVIDUAL_LIST_URL = APP_NAME + ':list'

# FIELDS
# -----------------------------------------------------------------------------
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
    )

INDIVIDUAL_UNIQUE_TOGETHER = (
    'institution',
    'species',
    'ext_id',
    )

# CHOICES
# -----------------------------------------------------------------------------

# institution
MSK = 'MSK'
OTHER = 'OTHER'
INSTITUTION = (
    (MSK, 'Memorial Sloan-Kettering Cancer Center'),
    (OTHER, 'Other'),
    )
INSTITUTION_VALUE = [s[0] for s in INSTITUTION]

# species
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

# all choices
INDIVIDUAL_CHOICES = {
    "INSTITUTION": INSTITUTION,
    "SPECIES": SPECIES,
    }

# leukid
LEUKID_SPECIES = {
    HUMAN: 'H',
    MOUSE: 'M',
    YEAST: 'Y',
    ZEBRAFISH: 'Z',
    XENOGRAFT: 'X',
    }

# PERMISSIONS
# -----------------------------------------------------------------------------
INDIVIDUAL_CREATE_PERMISSIONS = ('individuals.add_individual',)
INDIVIDUAL_UPDATE_PERMISSIONS = ('individuals.change_individual',)

# MESSAGES
# -----------------------------------------------------------------------------
SUCCESS_MESSAGE = "Looking good"
PERMISSION_DENIED_MESSAGE = \
    '''
    You don't have permission to perform this action, please contact a Leukgen
    Administrator
    '''
