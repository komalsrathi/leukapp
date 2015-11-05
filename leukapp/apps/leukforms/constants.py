# -*- coding: utf-8 -*-
"""
runs app constants
"""

# leukapp unique together
from leukapp.apps.individuals.constants import INDIVIDUAL_UNIQUE_TOGETHER
from leukapp.apps.specimens.constants import SPECIMEN_UNIQUE_TOGETHER
from leukapp.apps.aliquots.constants import ALIQUOT_UNIQUE_TOGETHER
from leukapp.apps.runs.constants import RUN_UNIQUE_TOGETHER

# leukform fields
from leukapp.apps.individuals.constants import INDIVIDUAL_LEUKFORM_FIELDS
from leukapp.apps.specimens.constants import SPECIMEN_LEUKFORM_FIELDS
from leukapp.apps.aliquots.constants import ALIQUOT_LEUKFORM_FIELDS
from leukapp.apps.runs.constants import RUN_LEUKFORM_FIELDS

# leukapp models
from leukapp.apps.individuals.models import Individual
from leukapp.apps.specimens.models import Specimen
from leukapp.apps.aliquots.models import Aliquot
from leukapp.apps.runs.models import Run

# leukapp factories
from leukapp.apps.projects.factories import ProjectFactory
from leukapp.apps.individuals.factories import IndividualFactory
from leukapp.apps.specimens.factories import SpecimenFactory
from leukapp.apps.aliquots.factories import AliquotFactory
from leukapp.apps.runs.factories import RunFactory

# local
from .forms import IndividualForm
from .forms import SpecimenForm
from .forms import AliquotForm
from .forms import RunForm

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
LEUKFORM_FIELDS = {
    'Individual': INDIVIDUAL_LEUKFORM_FIELDS,
    'Specimen': SPECIMEN_LEUKFORM_FIELDS,
    'Aliquot': ALIQUOT_LEUKFORM_FIELDS,
    'Run': RUN_LEUKFORM_FIELDS,
    }

# unique together
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

# factories
LEUKAPP_FACTORIES = {
    'Individual': IndividualFactory,
    'Specimen': SpecimenFactory,
    'Aliquot': AliquotFactory,
    'Run': RunFactory,
    'Project': ProjectFactory,
    }

# leukapp forms
LEUKAPP_FORMS = {
    'Individual': IndividualForm,
    'Specimen': SpecimenForm,
    'Aliquot': AliquotForm,
    'Run': RunForm
    }
