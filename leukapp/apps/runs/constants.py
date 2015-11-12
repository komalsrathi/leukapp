# -*- coding: utf-8 -*-
"""
runs app constants
"""

# APP INFO
# -----------------------------------------------------------------------------
APP_NAME = 'runs'

# URLS
# -----------------------------------------------------------------------------
RUN_CREATE_URL = APP_NAME + ':create'
RUN_LIST_URL = APP_NAME + ':list'

# FIELDS
# -----------------------------------------------------------------------------
RUN_CREATE_FIELDS = (
    'aliquot',
    'platform',
    'technology',
    'center',
    'ext_id',
    'projects',
    'bio_source',
    )

RUN_LEUKFORM_FIELDS = (
    'platform',
    'technology',
    'center',
    'ext_id',
    'projects_list',
    'bio_source',
    )

RUN_UPDATE_FIELDS = (
    'platform',
    'technology',
    'center',
    )

RUN_UNIQUE_TOGETHER = (
    'aliquot',
    'ext_id',
    'bio_source',
    )

# CHOICES
# -----------------------------------------------------------------------------

# platform
WHOLE_EXOME = 'WHOLE-EXOME'
WHOLE_GENOME = 'WHOLE-GENOME'
TARGETED_DNA = 'TARGETED-DNA'
RNA_SEQ_TARGETED = 'RNA-SEQ-TARGETED'
RNA_SEQ_WHOLE_TRANSCRIPTOME = 'RNA-SEQ-WHOLE-TRANSCRIPTOME'
RNA_SEQ_SINGLE_CELL = 'RNA-SEQ-SINGLE-CELL'
DNA_METHYLATION_SEQ = 'DNA-METHYLATION-SEQ'
CHIP_SEQ = 'CHIP-SEQ'
ATAC_SEQ = 'ATAC-SEQ'
PLATFORM = (
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
PLATFORM_VALUE = [e[0] for e in PLATFORM]

# technology
AGILENTV4 = 'AGILENTV4'
AGILENTV5 = 'AGILENTV5'
WHOLEGENOMELIBRARYV1 = 'WHOLEGENOMELIBRARYV1'
HEMEPACTV1 = 'HEMEPACTV1'
HEMEPACTV2 = 'HEMEPACTV2'
TECHNOLOGY = (
    (AGILENTV4, 'AGILENTV4'),
    (AGILENTV5, 'AGILENTV5'),
    (WHOLEGENOMELIBRARYV1, 'WHOLEGENOMELIBRARYV1'),
    (HEMEPACTV1, 'HEMEPACTV1'),
    (HEMEPACTV2, 'HEMEPACTV2'),
    )
TECHNOLOGY_VALUE = [e[0] for e in TECHNOLOGY]

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
BIO_SOURCE = (
    (DNA, 'DNA'),
    (RNA, 'RNA'),
    )
BIO_SOURCE_VALUE = [b[0] for b in BIO_SOURCE]

ALIQUOT_CHOICES = {
    "BIO_SOURCE": BIO_SOURCE,
    }

LEUKID_BIO_SOURCE = {
    DNA: 'D',
    RNA: 'R',
    }

RUN_CHOICES = {
    "PLATFORM": PLATFORM,
    "TECHNOLOGY": TECHNOLOGY,
    "CENTER": CENTER,
    "BIO_SOURCE": BIO_SOURCE,
    }

# PERMISSIONS
# -----------------------------------------------------------------------------
RUN_CREATE_PERMISSIONS = ('runs.add_run',)
RUN_UPDATE_PERMISSIONS = ('runs.change_run',)

# MESSAGES
# -----------------------------------------------------------------------------
SUCCESS_MESSAGE = "Looking good"
PERMISSION_DENIED_MESSAGE = \
    '''
    You don't have permission to perform this action, please contact a Leukgen
    Administrator
    '''
