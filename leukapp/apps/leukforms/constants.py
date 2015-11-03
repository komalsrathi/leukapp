# -*- coding: utf-8 -*-
"""
runs app constants
"""

# leukapp
from leukapp.apps.individuals.constants import INDIVIDUAL_UNIQUE_TOGETHER
from leukapp.apps.specimens.constants import SPECIMEN_UNIQUE_TOGETHER
from leukapp.apps.aliquots.constants import ALIQUOT_UNIQUE_TOGETHER
from leukapp.apps.runs.constants import RUN_UNIQUE_TOGETHER
from leukapp.apps.individuals.models import Individual
from leukapp.apps.specimens.models import Specimen
from leukapp.apps.aliquots.models import Aliquot
from leukapp.apps.runs.models import Run

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
    'Run.projects_list',
]

LEUKAPP_UNIQUE_TOGETHER = {
    'Individual': INDIVIDUAL_UNIQUE_TOGETHER,
    'Specimen': SPECIMEN_UNIQUE_TOGETHER,
    'Aliquot': ALIQUOT_UNIQUE_TOGETHER,
    'Run': RUN_UNIQUE_TOGETHER,
    }

# Models
MODELS_LIST = ['Individual', 'Specimen', 'Aliquot', 'Run']

LEUKAPP_MODELS = {
    'Individual': Individual,
    'Specimen': Specimen,
    'Aliquot': Aliquot,
    'Run': Run,
    }
