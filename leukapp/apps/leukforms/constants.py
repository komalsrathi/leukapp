# -*- coding: utf-8 -*-
"""
extractions app constants
"""

# leukapp
from leukapp.apps.core import constants as coreconstants

# leukapp unique together
from leukapp.apps.individuals.constants import INDIVIDUAL_UNIQUE_TOGETHER
from leukapp.apps.specimens.constants import SPECIMEN_UNIQUE_TOGETHER
from leukapp.apps.aliquots.constants import ALIQUOT_UNIQUE_TOGETHER
from leukapp.apps.extractions.constants import EXTRACTION_UNIQUE_TOGETHER

# leukform fields
from leukapp.apps.individuals.constants import INDIVIDUAL_CREATE_FIELDS
from leukapp.apps.specimens.constants import SPECIMEN_CREATE_FIELDS
from leukapp.apps.aliquots.constants import ALIQUOT_CREATE_FIELDS
from leukapp.apps.extractions.constants import EXTRACTION_CREATE_FIELDS

# leukapp models
from leukapp.apps.individuals.models import Individual
from leukapp.apps.specimens.models import Specimen
from leukapp.apps.aliquots.models import Aliquot
from leukapp.apps.extractions.models import Extraction

# leukapp factories
from leukapp.apps.projects.factories import ProjectFactory
from leukapp.apps.individuals.factories import IndividualFactory
from leukapp.apps.specimens.factories import SpecimenFactory
from leukapp.apps.aliquots.factories import AliquotFactory
from leukapp.apps.extractions.factories import ExtractionFactory

# local
from .forms import IndividualForm
from .forms import SpecimenForm
from .forms import AliquotForm
from .forms import ExtractionForm

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
    'Extraction': EXTRACTION_CREATE_FIELDS,
    }

# unique together
LEUKAPP_UNIQUE_TOGETHER = {
    'Individual': INDIVIDUAL_UNIQUE_TOGETHER,
    'Specimen': SPECIMEN_UNIQUE_TOGETHER,
    'Aliquot': ALIQUOT_UNIQUE_TOGETHER,
    'Extraction': EXTRACTION_UNIQUE_TOGETHER,
    }

# MODELS
# -----------------------------------------------------------------------------
MODELS_LIST = ['Individual', 'Specimen', 'Aliquot', 'Extraction']

LEUKAPP_MODELS = {
    'Individual': Individual,
    'Specimen': Specimen,
    'Aliquot': Aliquot,
    'Extraction': Extraction,
    }

# FACTORIES
# -----------------------------------------------------------------------------
LEUKAPP_FACTORIES = {
    'Individual': IndividualFactory,
    'Specimen': SpecimenFactory,
    'Aliquot': AliquotFactory,
    'Extraction': ExtractionFactory,
    'Project': ProjectFactory,
    }

# FORMS
# -----------------------------------------------------------------------------
LEUKAPP_FORMS = {
    'Individual': IndividualForm,
    'Specimen': SpecimenForm,
    'Aliquot': AliquotForm,
    'Extraction': ExtractionForm
    }


# PERMISSIONS
# -----------------------------------------------------------------------------
LEUKFORM_CREATE_PERMISSIONS = ('leukforms.add_leukform',)
LEUKFORM_UPDATE_PERMISSIONS = ('leukforms.change_leukform',)

# MESSAGES
# -----------------------------------------------------------------------------
SUCCESS_MESSAGE = coreconstants.SUCCESS_MESSAGE
PERMISSION_DENIED_MESSAGE = coreconstants.PERMISSION_DENIED_MESSAGE
