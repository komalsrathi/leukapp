# -*- coding: utf-8 -*-
"""
extractions app constants
"""

# APP INFO
# -----------------------------------------------------------------------------
APP_NAME = 'extractions'

# URLS
# -----------------------------------------------------------------------------
EXTRACTION_CREATE_URL = APP_NAME + ':create'
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
    'projects_list',
    )

EXTRACTION_UPDATE_FIELDS = (
    'platform',
    'technology',
    'center',
    )

EXTRACTION_UNIQUE_TOGETHER = (
    'aliquot',
    'ext_id',
    'analyte',
    )

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
SUCCESS_MESSAGE = "Looking good"
PERMISSION_DENIED_MESSAGE = \
    '''
    You don't have permission to perform this action, please contact a Leukgen
    Administrator
    '''
