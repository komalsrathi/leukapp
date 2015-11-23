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
# -----------------------------------------------------------------------------
APP_NAME = 'extractions'  #: Application's name.

# URLS
# -----------------------------------------------------------------------------
EXTRACTION_CREATE_URL = APP_NAME + ':create'  #: Create URL reverse string.
EXTRACTION_LIST_URL = APP_NAME + ':list'      #: List URL reverse string.

# FIELDS
# -----------------------------------------------------------------------------

#: Fields required to create a new instance.
EXTRACTION_CREATE_FIELDS = (
    'aliquot',
    'platform',
    'technology',
    'center',
    'ext_id',
    'analyte',
    'projects_string',
    )

#: Enabled fields to update an existing instance.
EXTRACTION_UPDATE_FIELDS = tuple()

#: Fields that are required to be unique together.
EXTRACTION_UNIQUE_TOGETHER = tuple()

# CHOICES
# -----------------------------------------------------------------------------
WHOLE_EXOME = 'WHOLE-EXOME'
WHOLE_GENOME = 'WHOLE-GENOME'
TARGETED_DNA = 'TARGETED-DNA'
RNA_SEQ_TARGETED = 'RNA-SEQ-TARGETED'
RNA_SEQ_WHOLE_TRANSCRIPTOME = 'RNA-SEQ-WHOLE-TRANSCRIPTOME'
RNA_SEQ_SINGLE_CELL = 'RNA-SEQ-SINGLE-CELL'
DNA_METHYLATION_SEQ = 'DNA-METHYLATION-SEQ'
CHIP_SEQ = 'CHIP-SEQ'
ATAC_SEQ = 'ATAC-SEQ'
TECHNOLOGY = (
    (WHOLE_EXOME, 'WHOLE-EXOME'),
    (WHOLE_GENOME, 'WHOLE-GENOME'),
    (TARGETED_DNA, 'TARGETED-DNA'),
    (RNA_SEQ_TARGETED, 'RNA-SEQ-TARGETED'),
    (RNA_SEQ_WHOLE_TRANSCRIPTOME, 'RNA-SEQ-WHOLE-TRANSCRIPTOME'),
    (RNA_SEQ_SINGLE_CELL, 'RNA-SEQ-SINGLE-CELL'),
    (DNA_METHYLATION_SEQ, 'DNA-METHYLATION-SEQ'),
    (CHIP_SEQ, 'CHIP-SEQ'),
    (ATAC_SEQ, 'ATAC-SEQ'),
    )
"""
List of value, verbose_name pairs for the
:attr:`~leukapp.apps.extractions.models.Extraction.technology` attribute.
"""

TECHNOLOGY_VALUE = [e[0] for e in TECHNOLOGY]
"""
Values for the :attr:`~leukapp.apps.extractions.models.Extraction.technology`
attribute.
"""

AGILENTV4 = 'AGILENTV4'
AGILENTV5 = 'AGILENTV5'
WHOLEGENOMELIBRARYV1 = 'WHOLEGENOMELIBRARYV1'
HEMEPACTV1 = 'HEMEPACTV1'
HEMEPACTV2 = 'HEMEPACTV2'
PLATFORM = (
    (AGILENTV4, 'AGILENTV4'),
    (AGILENTV5, 'AGILENTV5'),
    (WHOLEGENOMELIBRARYV1, 'WHOLEGENOMELIBRARYV1'),
    (HEMEPACTV1, 'HEMEPACTV1'),
    (HEMEPACTV2, 'HEMEPACTV2'),
    )
"""
List of value, verbose_name pairs for the
:attr:`~leukapp.apps.extractions.models.Extraction.platform` attribute.
"""

PLATFORM_VALUE = [e[0] for e in PLATFORM]
"""
Values for the :attr:`~leukapp.apps.extractions.models.Extraction.platform`
attribute.
"""

CMO = 'CMO'
NYGC = 'NYGC'
FOUNDATION = 'FOUNDATION'
CENTER = (
    (CMO, 'CMO'),
    (NYGC, 'NYGC'),
    (FOUNDATION, 'FOUNDATION'),
    )
"""
List of value, verbose_name pairs for the
:attr:`~leukapp.apps.extractions.models.Extraction.center` attribute.
"""

CENTER_VALUE = [e[0] for e in CENTER]
"""
Values for the :attr:`~leukapp.apps.extractions.models.Extraction.center`
attribute.
"""

DNA = 'DNA'
RNA = 'RNA'
ANALYTE = (
    (DNA, 'DNA'),
    (RNA, 'RNA'),
    )
"""
List of value, verbose_name pairs for the
:attr:`~leukapp.apps.extractions.models.Extraction.analyte` attribute.
"""

ANALYTE_VALUE = [b[0] for b in ANALYTE]
"""
Values for the :attr:`~leukapp.apps.extractions.models.Extraction.analyte`
attribute.
"""

EXTRACTION_CHOICES = {
    "PLATFORM": PLATFORM,
    "TECHNOLOGY": TECHNOLOGY,
    "CENTER": CENTER,
    "ANALYTE": ANALYTE,
    }
"""
Dictionary including all
:class:`Extraction's <~leukapp.apps.extractions.models.Extraction>` choices.
"""

LEUKID_ANALYTE = {
    DNA: 'D',
    RNA: 'R',
    }
"""
Characters used in the **leukid** to describe the `Extraction's`
:attr:`~leukapp.apps.extractions.models.Extraction.analyte` attribute.
"""

# PERMISSIONS
# -----------------------------------------------------------------------------

#: Tuple of permissions required to create a new instance.
EXTRACTION_CREATE_PERMISSIONS = ('extractions.add_extraction',)

#: Tuple of permissions required to update an existing instance.
EXTRACTION_UPDATE_PERMISSIONS = ('extractions.change_extraction',)

# MESSAGES
# -----------------------------------------------------------------------------

#: Sucess message.
SUCCESS_MESSAGE = coreconstants.SUCCESS_MESSAGE

#: Permission denied message.
PERMISSION_DENIED_MESSAGE = coreconstants.PERMISSION_DENIED_MESSAGE
