# -*- coding: utf-8 -*-
"""
runs app constants
"""

# app name
APP_NAME = 'leukforms'

# urls
LEUKFORM_CREATE_URL = APP_NAME + ':create'
LEUKFORM_LIST_URL = APP_NAME + ':list'

# run fields
LEUKFORM_CREATE_FIELDS = [
    'description',
    'submission',
    ]

LEUKFORM_UPDATE_FIELDS = [
    'description',
    ]

LEUKFORM_GET_OR_CREATE_FIELDS = (
    'description',
    'submission',
    )

# leukform fields
LEUKFORM_CSV_FIELDS = [
    'Individual.ext_id',
    'Individual.institution',
    'Individual.species',
    'Specimen.ext_id',
    'Specimen.source_type',
    'Specimen.order',
    'Aliquot.ext_id',
    'Aliquot.bio_source',
    'Run.ext_id',
    'Run.platform',
    'Run.technology',
    'Run.center',
    'Run.projects',
]

# Models
MODELS = ['Individual', 'Specimen', 'Aliquot', 'Run']
