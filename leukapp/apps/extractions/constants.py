# -*- coding: utf-8 -*-
"""
This module contains the :py:mod:`~leukapp.apps.extractions` app constants.
Information that isn't likely to change and that is used across
:py:mod:`~leukapp.apps.extractions` and :py:mod:`~leukapp` should be stored
here.

.. important::
    Please, **DO NOT** change any constant unless you are sure of what you are
    doing.
"""

# leukapp
from leukapp.apps.core import constants as coreconstants

# APP INFO
# -----------------------------------------------------------------------------

APP_NAME = 'extractions'
""" Application's name. """

# URLS
# -----------------------------------------------------------------------------

EXTRACTION_CREATE_URL = APP_NAME + ':create'
""" :py:class:`~leukapp.apps.extractions.models.Extraction` create url. """

EXTRACTION_LIST_URL = APP_NAME + ':list'

# FIELDS
# -----------------------------------------------------------------------------
EXTRACTION_CREATE_FIELDS = (
    'aliquot',
    'platform',
    'technology',
    'center',
    'ext_id',
    'analyte',
    'projects_string',
    )

EXTRACTION_UPDATE_FIELDS = tuple()
EXTRACTION_UNIQUE_TOGETHER = tuple()

# CHOICES
# -----------------------------------------------------------------------------

# technology
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
TECHNOLOGY_VALUE = [e[0] for e in TECHNOLOGY]

# platform
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
PLATFORM_VALUE = [e[0] for e in PLATFORM]

# sequencing center
CMO = 'CMO'
NYGC = 'NYGC'
FOUNDATION = 'FOUNDATION'
CENTER = (
    (CMO, 'CMO'),
    (NYGC, 'NYGC'),
    (FOUNDATION, 'FOUNDATION'),
    )
CENTER_VALUE = [e[0] for e in CENTER]

# extracted material
DNA = 'DNA'
RNA = 'RNA'
ANALYTE = (
    (DNA, 'DNA'),
    (RNA, 'RNA'),
    )
ANALYTE_VALUE = [b[0] for b in ANALYTE]

ALIQUOT_CHOICES = {
    "ANALYTE": ANALYTE,
    }

LEUKID_ANALYTE = {
    DNA: 'D',
    RNA: 'R',
    }

EXTRACTION_CHOICES = {
    "PLATFORM": PLATFORM,
    "TECHNOLOGY": TECHNOLOGY,
    "CENTER": CENTER,
    "ANALYTE": ANALYTE,
    }

# PERMISSIONS
# -----------------------------------------------------------------------------
EXTRACTION_CREATE_PERMISSIONS = ('extractions.add_extraction',)
EXTRACTION_UPDATE_PERMISSIONS = ('extractions.change_extraction',)

# MESSAGES
# -----------------------------------------------------------------------------
SUCCESS_MESSAGE = coreconstants.SUCCESS_MESSAGE
PERMISSION_DENIED_MESSAGE = coreconstants.PERMISSION_DENIED_MESSAGE
