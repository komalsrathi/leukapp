# -*- coding: utf-8 -*-
"""
samples app constants
"""

# app name
APP_NAME = 'samples'

# leukgen_form fields
LEUKGEN_FORM_FIELDS = [
    'Project.pk',
    'Individual.institution',
    'Individual.species',
    'Individual.ext_id',
    'Specimen.source',
    'Specimen.ext_id',
    'Aliquot.bio_source',
    'Aliquot.ext_id',
]

LEUKGEN_FORM_TEST_FIELDS = [
    'RESULT_Project',
    'Project.pk',
    'RESULT_Individual',
    'Individual.institution',
    'ERROR_Individual.institution',
    'Individual.species',
    'ERROR_Individual.species',
    'Individual.ext_id',
    'ERROR_Individual.ext_id',
    'RESULT_Specimen',
    'Specimen.source',
    'ERROR_Specimen.source',
    'Specimen.ext_id',
    'ERROR_Specimen.ext_id',
    'RESULT_Aliquot',
    'Aliquot.bio_source',
    'ERROR_Aliquot.bio_source',
    'Aliquot.ext_id',
    'ERROR_Aliquot.ext_id',
]
