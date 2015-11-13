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
from leukapp.apps.individuals.constants import INDIVIDUAL_CREATE_FIELDS
from leukapp.apps.specimens.constants import SPECIMEN_CREATE_FIELDS
from leukapp.apps.aliquots.constants import ALIQUOT_CREATE_FIELDS
from leukapp.apps.runs.constants import RUN_CREATE_FIELDS

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

# APP INFO
# -----------------------------------------------------------------------------
APP_NAME = 'leukforms'

# URLS
# -----------------------------------------------------------------------------
LEUKFORM_CREATE_URL = APP_NAME + ':create'
LEUKFORM_LIST_URL = APP_NAME + ':list'

# FIELDS
# -----------------------------------------------------------------------------

# Leukform Model fields
LEUKFORM_CREATE_FIELDS = [
    'description',
    'submission',
    'mock',
    ]

LEUKFORM_UPDATE_FIELDS = [
    'description',
    ]

LEUKFORM_GET_OR_CREATE_FIELDS = (
    'description',
    'submission',
    'mock',
    )

# leukform fields
CREATE_FIELDS = {
    'Individual': INDIVIDUAL_CREATE_FIELDS,
    'Specimen': SPECIMEN_CREATE_FIELDS,
    'Aliquot': ALIQUOT_CREATE_FIELDS,
    'Run': RUN_CREATE_FIELDS,
    }

# unique together
LEUKAPP_UNIQUE_TOGETHER = {
    'Individual': INDIVIDUAL_UNIQUE_TOGETHER,
    'Specimen': SPECIMEN_UNIQUE_TOGETHER,
    'Aliquot': ALIQUOT_UNIQUE_TOGETHER,
    'Run': RUN_UNIQUE_TOGETHER,
    }

# MODELS
# -----------------------------------------------------------------------------
MODELS_LIST = ['Individual', 'Specimen', 'Aliquot', 'Run']

LEUKAPP_MODELS = {
    'Individual': Individual,
    'Specimen': Specimen,
    'Aliquot': Aliquot,
    'Run': Run,
    }

# FACTORIES
# -----------------------------------------------------------------------------
LEUKAPP_FACTORIES = {
    'Individual': IndividualFactory,
    'Specimen': SpecimenFactory,
    'Aliquot': AliquotFactory,
    'Run': RunFactory,
    'Project': ProjectFactory,
    }

# FORMS
# -----------------------------------------------------------------------------
LEUKAPP_FORMS = {
    'Individual': IndividualForm,
    'Specimen': SpecimenForm,
    'Aliquot': AliquotForm,
    'Run': RunForm
    }

# MESSAGES
# -----------------------------------------------------------------------------
PERMISSION_DENIED_MESSAGE = \
    '''
    You don't have permission to perform this action, please contact a Leukgen
    Administrator
    '''
