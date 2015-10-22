# -*- coding: utf-8 -*-
"""
samples app constants
"""

# app name
APP_NAME = 'leukforms'

# urls
LEUKFORM_CREATE_URL = APP_NAME + ':create'
LEUKFORM_LIST_URL = APP_NAME + ':list'

# sample fields
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
    'Specimen.source',
    'Specimen.source_type',
    'Aliquot.ext_id',
    'Aliquot.bio_source',
    'Sample.ext_id',
    'Sample.platform',
    'Sample.technology',
    'Sample.center',
    'Sample.projects',
]