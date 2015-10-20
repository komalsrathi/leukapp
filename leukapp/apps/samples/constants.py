# -*- coding: utf-8 -*-
"""
samples app constants
"""

# app name
APP_NAME = 'samples'

# urls
SAMPLE_CREATE_URL = APP_NAME + ':create'
SAMPLE_LIST_URL = APP_NAME + ':list'

# choices
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

CMO = 'CMO'
NYGC = 'NYGC'
FOUNDATION = 'FOUNDATION'
CENTER = (
    (CMO, 'CMO'),
    (NYGC, 'NYGC'),
    (FOUNDATION, 'FOUNDATION'),
    )

SAMPLE_CHOICES = {
    "PLATFORM": PLATFORM,
    "TECHNOLOGY": TECHNOLOGY,
    "CENTER": CENTER,
    }

# choices short
PLATFORM_SHORT = [e[0] for e in PLATFORM]
TECHNOLOGY_SHORT = [e[0] for e in TECHNOLOGY]
CENTER_SHORT = [e[0] for e in CENTER]

# sample fields
SAMPLE_CREATE_FIELDS = [
    'aliquot',
    'platform',
    'technology',
    'center',
    'ext_id',
    'projects',
    ]

SAMPLE_UPDATE_FIELDS = [
    'platform',
    'technology',
    'center',
    ]

SAMPLE_GET_OR_CREATE_FIELDS = (
    'aliquot',
    'ext_id',
    )

# leukform fields
LEUKFORM_FIELDS = [
    'Individual.ext_id',
    'Individual.institution',
    'Individual.species',
    'Specimen.ext_id',
    'Specimen.source',
    'Specimen.source_type',
    'Aliquot.ext_id',
    'Aliquot.bio_source',
    'Sample.ext_id',
    'Sample.platform',
    'Sample.technology',
    'Sample.center',
    'Sample.projects',
]

LEUKFORM_OUT_FIELDS = [
    'Individual.ext_id',
    'Individual.action',
    'Individual.errors',
    'Specimen.ext_id',
    'Specimen.action',
    'Specimen.errors',
    'Aliquot.ext_id',
    'Aliquot.action',
    'Aliquot.errors',
    'Sample.ext_id',
    'Sample.action',
    'Sample.errors',
]
