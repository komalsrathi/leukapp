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
# =============================================================================

# SEQUENCING CENTER
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
CMO = 'CMO'
NYGC = 'NYGC'
FOUNDATION = 'FOUNDATION'

CENTER = (
    (CMO, CMO),
    (NYGC, NYGC),
    (FOUNDATION, FOUNDATION),
    )
"""
List of value, verbose_name pairs for the
:attr:`~leukapp.apps.extractions.models.Extraction.center` attribute.
"""

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

# TECHNOLOGY
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
WHOLEGENOME = 'WHOLE-GENOME'
WHOLEEXOME = 'WHOLE-EXOME'
TARGETEDDNA = 'TARGETED-DNA'
RNASEQ = 'RNA-SEQ'
RNASEQCUSTOM = 'RNA-SEQ-CUSTOM'
RNASEQSINGLECELL = 'RNA-SEQ-SINGLE-CELL'
CHIPSEQ = 'CHIP-SEQ'
ATACSEQ = 'ATAC-SEQ'
FOUNDATION = 'FOUNDATION'
RLP = 'RLP'

TECHNOLOGY = (
    (WHOLEEXOME, WHOLEEXOME),
    (WHOLEGENOME, WHOLEGENOME),
    (TARGETEDDNA, TARGETEDDNA),
    (RNASEQ, RNASEQ),
    (RNASEQCUSTOM, RNASEQCUSTOM),
    (RNASEQSINGLECELL, RNASEQSINGLECELL),
    (CHIPSEQ, CHIPSEQ),
    (ATACSEQ, ATACSEQ),
    (FOUNDATION, FOUNDATION),
    (RLP, RLP),
    )
"""
List of `(value, verbose name)` pairs for the
:attr:`~leukapp.apps.extractions.models.Extraction.technology` attribute.
"""

# PLATFORM
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# WHOLE GENOME
HISEQ = "HISEQ"
ILLUMINAXTEN = "ILLUMINA-XTEN"

# WHOLE EXOME
AGILENT50MB = "AGILENT-50MB"
AGILENT51MB = "AGILENT-51MB"

# RNA-SEQ
PAIREDEND50BP = "PAIRED-END-50BP"
SINGLEEND150BP = "SINGLE-END-150BP"

# TARGETED DNA
HEMEPACTV1 = "HEMEPACT-V1"
HEMEPACTV2 = "HEMEPACT-V2"
HEMEPACTV3 = "HEMEPACT-V3"
IMPACTHEME = "IMPACT-HEME"
IMPACT300 = "IMPACT-300"
IMPACT340 = "IMPACT-340"
IMPACTCLINICAL = "IMPACT-CLINICAL"

# CHIP-SEQ
H3K4ME1 = "H3K4ME1"
H3K4ME3 = "H3K4ME3"
H3K4ME2 = "H3K4ME2"
H3K27AC = "H3K27AC"

# FOUNDATION
FOUNDATIONONEHEMEPANEL = "FOUNDATIONONE-HEME-PANEL"
FOUNDATIONONEPANEL = "FOUNDATIONONE-PANEL"

PLATFORM = (
    (HISEQ, HISEQ),
    (ILLUMINAXTEN, ILLUMINAXTEN),
    (AGILENT50MB, AGILENT50MB),
    (AGILENT51MB, AGILENT51MB),
    (PAIREDEND50BP, PAIREDEND50BP),
    (SINGLEEND150BP, SINGLEEND150BP),
    (HEMEPACTV1, HEMEPACTV1),
    (HEMEPACTV2, HEMEPACTV2),
    (HEMEPACTV3, HEMEPACTV3),
    (IMPACTHEME, IMPACTHEME),
    (IMPACT300, IMPACT300),
    (IMPACT340, IMPACT340),
    (IMPACTCLINICAL, IMPACTCLINICAL),
    (H3K4ME1, H3K4ME1),
    (H3K4ME3, H3K4ME3),
    (H3K4ME2, H3K4ME2),
    (H3K27AC, H3K27AC),
    (FOUNDATIONONEHEMEPANEL, FOUNDATIONONEHEMEPANEL),
    (FOUNDATIONONEPANEL, FOUNDATIONONEPANEL),
    )
"""
List of value, verbose_name pairs for the
:attr:`~leukapp.apps.extractions.models.Extraction.platform` attribute.
"""

# TECHNOLOGY-PLATFORM CODES
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TECHNOLOGY_PLATFORM = {

    WHOLEGENOME: {
        HISEQ: "1",
        ILLUMINAXTEN: "1",
        },

    WHOLEEXOME: {
        AGILENT50MB: "2",
        AGILENT51MB: "2",
        },

    RNASEQ: {
        PAIREDEND50BP: "3",
        SINGLEEND150BP: "3",
        },

    TARGETEDDNA: {
        HEMEPACTV1: "4",
        HEMEPACTV2: "4",
        HEMEPACTV3: "4",
        IMPACTHEME: "4",
        IMPACT300: "5",
        IMPACT340: "5",
        IMPACTCLINICAL: "5",
        },

    CHIPSEQ: {
        H3K4ME1: "",
        H3K4ME3: "",
        H3K4ME2: "",
        H3K27AC: "",
        },

    RLP: {
        "": "8",
        },

    RNASEQCUSTOM: {
        "": "9",
        },

    ATACSEQ: {
        "": "10",
        },

    RNASEQSINGLECELL: {
        "": "11",
        },

    FOUNDATION: {
        FOUNDATIONONEHEMEPANEL: "12",
        FOUNDATIONONEPANEL: "12",
        },

    }
"""
Technology platform codes dictionary.

.. important: Juan doesn't like this "code" thing. Too artistic.
"""

# ALL CHOICES
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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
