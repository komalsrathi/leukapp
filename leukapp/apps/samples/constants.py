# -*- coding: utf-8 -*-
"""
samples app constants
"""

# app name
APP_NAME = 'samples'

# leukform fields
LEUKFORM_FIELDS = [
    'Project.pk',
    'Individual.institution',
    'Individual.species',
    'Individual.ext_id',
    'Specimen.source',
    'Specimen.ext_id',
    'Aliquot.bio_source',
    'Aliquot.ext_id',
]

LEUKFORM_OUT_FIELDS = [
    'Project.action',
    'Project.pk',
    'Project.errors',
    'Individual.ext_id',
    'Individual.action',
    'Individual.errors',
    'Specimen.ext_id',
    'Specimen.action',
    'Specimen.errors',
    'Aliquot.ext_id',
    'Aliquot.action',
    'Aliquot.errors',
]
