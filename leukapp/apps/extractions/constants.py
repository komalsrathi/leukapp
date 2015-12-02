# -*- coding: utf-8 -*-

"""
This module contains the :mod:`~leukapp.apps.extractions` app constants.
Information that isn't likely to change and that is used across
:mod:`~leukapp.apps.extractions` and :mod:`~leukapp` should be stored
here.

.. important::
    **DO NOT** change any constant unless you know what you are doing.
"""

# leukapp
from leukapp.apps.core import constants as coreconstants

# APP INFO
# =============================================================================
APP_NAME = 'extractions'  #: Application's name.

# URLS
# =============================================================================
EXTRACTION_CREATE_URL = APP_NAME + ':create'  #: Create URL reverse string.
EXTRACTION_LIST_URL = APP_NAME + ':list'      #: List URL reverse string.

# FIELDS
# =============================================================================

#: Fields required to create a new instance.
EXTRACTION_CREATE_FIELDS = (
    'aliquot',
    'ext_id',
    'analyte',
    )

#: Enabled fields to update an existing instance.
EXTRACTION_UPDATE_FIELDS = tuple()

#: Fields that are required to be unique together.
EXTRACTION_UNIQUE_TOGETHER = (
    'aliquot',
    'ext_id',
    )

# CHOICES
# =============================================================================

# ANALYTE
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
DNA = 'DNA'
RNA = 'RNA'

ANALYTE = (
    (DNA, DNA),
    (RNA, RNA),
    )
"""
List of value, verbose_name pairs for the
:attr:`~leukapp.apps.extractions.models.Extraction.analyte` attribute.
"""

# ALL CHOICES
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
EXTRACTION_CHOICES = {
    "ANALYTE": ANALYTE,
    }
"""
Dictionary including all
:class:`Extraction's <~leukapp.apps.extractions.models.Extraction>` choices.
"""

# LEUKID ANALYTE CHARACTERS
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
LEUKID_ANALYTE = {
    DNA: 'D',
    RNA: 'R',
    }
"""
Characters used in the **leukid** to describe the `Extraction's`
:attr:`~leukapp.apps.extractions.models.Extraction.analyte` attribute.
"""

# PERMISSIONS
# =============================================================================

#: Tuple of permissions required to create a new instance.
EXTRACTION_CREATE_PERMISSIONS = ('extractions.add_extraction',)

#: Tuple of permissions required to update an existing instance.
EXTRACTION_UPDATE_PERMISSIONS = ('extractions.change_extraction',)

# MESSAGES
# =============================================================================

#: Sucess message.
SUCCESS_MESSAGE = coreconstants.SUCCESS_MESSAGE

#: Permission denied message.
PERMISSION_DENIED_MESSAGE = coreconstants.PERMISSION_DENIED_MESSAGE
