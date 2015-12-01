# -*- coding: utf-8 -*-

"""
This module contains the :mod:`~leukapp.apps.leukforms` app constants.
Information that isn't likely to change and that is used across the
:mod:`~leukapp.apps.leukforms` app and the :mod:`~leukapp` project
should be stored here.

.. important::
    **DO NOT** change any constant unless you know what you are doing.
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
# =============================================================================
APP_NAME = 'leukforms'  #: Application's name.

# URLS
# =============================================================================
LEUKFORM_CREATE_URL = APP_NAME + ':create'  #: Create URL reverse string.
LEUKFORM_LIST_URL = APP_NAME + ':list'      #: List URL reverse string.

# FIELDS
# =============================================================================

#: Fields required to create a new instance.
LEUKFORM_CREATE_FIELDS = (
    'description',
    'submission',
    'mock',
    )

#: Enabled fields to update an existing instance.
LEUKFORM_UPDATE_FIELDS = (
    'description',
    )

#: Fields that are required to be unique together.
LEUKFORM_UNIQUE_TOGETHER = (
    'description',
    'submission',
    'mock',
    )

#: Dictionary including **create fields*** for `leukapp` apps models.
CREATE_FIELDS = {
    'Individual': INDIVIDUAL_CREATE_FIELDS,
    'Specimen': SPECIMEN_CREATE_FIELDS,
    'Aliquot': ALIQUOT_CREATE_FIELDS,
    'Extraction': EXTRACTION_CREATE_FIELDS,
    }

#: Dictionary including **unique together fields*** for `leukapp` apps models.
LEUKAPP_UNIQUE_TOGETHER = {
    'Individual': INDIVIDUAL_UNIQUE_TOGETHER,
    'Specimen': SPECIMEN_UNIQUE_TOGETHER,
    'Aliquot': ALIQUOT_UNIQUE_TOGETHER,
    'Extraction': EXTRACTION_UNIQUE_TOGETHER,
    }

#: During submission, empty values are replaced for ``UNKNOWN`` for these cols.
UNKWOWN_ENABLED_COLUMNS = (
    'Specimen.ext_id',
    'Aliquot.ext_id',
    'Extraction.ext_id',
    'Extraction.platform',
    )

# MODELS
# =============================================================================

#: List of models names potentially used during a leukform submission.
MODELS_LIST = ['Individual', 'Specimen', 'Aliquot', 'Extraction']

#: Dictionary of model classes potentially used during a leukform submission.
LEUKAPP_MODELS = {
    'Individual': Individual,
    'Specimen': Specimen,
    'Aliquot': Aliquot,
    'Extraction': Extraction,
    }

# FACTORIES
# =============================================================================

#: Dictionary of model factories potentially used during a leukform submission.
LEUKAPP_FACTORIES = {
    'Individual': IndividualFactory,
    'Specimen': SpecimenFactory,
    'Aliquot': AliquotFactory,
    'Extraction': ExtractionFactory,
    'Project': ProjectFactory,
    }

# FORMS
# =============================================================================

#: Dictionary of model forms potentially used during a leukform submission.
LEUKAPP_FORMS = {
    'Individual': IndividualForm,
    'Specimen': SpecimenForm,
    'Aliquot': AliquotForm,
    'Extraction': ExtractionForm
    }

# PERMISSIONS
# =============================================================================

#: Tuple of permissions required to create a new instance.
LEUKFORM_CREATE_PERMISSIONS = ('leukforms.add_leukform',)

#: Tuple of permissions required to update an existing instance.
LEUKFORM_UPDATE_PERMISSIONS = ('leukforms.change_leukform',)

# MESSAGES
# =============================================================================

#: Sucess message.
SUCCESS_MESSAGE = coreconstants.SUCCESS_MESSAGE

#: Permission denied message.
PERMISSION_DENIED_MESSAGE = coreconstants.PERMISSION_DENIED_MESSAGE
