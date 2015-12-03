# -*- coding: utf-8 -*-

"""
This module contains the :mod:`~` app constants.
Information that isn't likely to change and that is used across
:mod:`~` and :mod:`~leukapp` should be stored
here.

.. important::
    **DO NOT** change any constant unless you know what you are doing.
"""

# leukapp
from leukapp.apps.core.constants import DEFAULT, SUCCESS_MESSAGE
from leukapp.apps.core.constants import PERMISSION_DENIED_MESSAGE
from leukapp.apps.extractions.constants import DNA, RNA

# APP INFO
# =============================================================================
APP_NAME = 'workflows'  #: Application's name.

# URLS
# =============================================================================
WORKFLOW_CREATE_URL = APP_NAME + ':create'  #: Create URL reverse string.
WORKFLOW_LIST_URL = APP_NAME + ':list'      #: List URL reverse string.

# FIELDS
# =============================================================================

#: Fields required to create a new instance.
WORKFLOW_CREATE_FIELDS = (
    'extraction',
    'ext_id',
    'sequencing_center',
    'sequencing_technology',
    'technology_type',
    'sequencing_platform',
    'read_length',
    'read_type',
    'projects_string',
    )

#: Enabled fields to update an existing instance.
WORKFLOW_UPDATE_FIELDS = tuple()

#: Fields that are required to be unique together.
WORKFLOW_UNIQUE_TOGETHER = (
    'extraction',
    'sequencing_center',
    'ext_id',
    )

# CHOICES
# =============================================================================

# SEQUENCING CENTER
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
CMO = 'CMO'
NYGC = 'NYGC'
FOUNDATION = 'FOUNDATION'
ILLUMINA = 'ILLUMINA'
SANGER = 'SANGER'

CENTER = (
    (CMO, CMO),
    (NYGC, NYGC),
    (FOUNDATION, FOUNDATION),
    (ILLUMINA, ILLUMINA),
    (SANGER, SANGER),
    )
"""
List of value, verbose_name pairs for the
:attr:`~.models.Workflow.center` attribute.
"""

# SEQUENCING TECHNOLOGY
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
    )
"""
List of `(value, verbose name)` pairs for the
:attr:`~.models.Workflow.sequencing_technology` attribute.
"""

# TECHNOLOGY_TYPE
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# WHOLE GENOME
DEFAULT

# WHOLE EXOME
AGILENT50MB = "AGILENT-50MB"
AGILENT51MB = "AGILENT-51MB"

# RNA-SEQ
FULLTRANSCRIPT = "FULLTRANSCRIPT"
THREEPRIMEEND = "3'END"

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
FOUNDATIONONHEMEPANEL = "FOUNDATIONON-HEME-PANEL"
FOUNDATIONONPANEL = "FOUNDATIONON-PANEL"

TECHNOLOGY_TYPE = (
    (DEFAULT, DEFAULT),
    (AGILENT50MB, AGILENT50MB),
    (AGILENT51MB, AGILENT51MB),
    (FULLTRANSCRIPT, FULLTRANSCRIPT),
    (THREEPRIMEEND, THREEPRIMEEND),
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
    (FOUNDATIONONHEMEPANEL, FOUNDATIONONHEMEPANEL),
    (FOUNDATIONONPANEL, FOUNDATIONONPANEL),
    )
"""
List of value, verbose_name pairs for the
:attr:`~.models.Workflow.technology_type` attribute.
"""

# SEQUENCING PLATFORM
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ILLUMINAHISEQ2000 = 'ILLUMINA-HISEQ-2000'
ILLUMINAHISEQ2500 = 'ILLUMINA-HISEQ-2500'
ILLUMINAMISEQ = 'ILLUMINA-MISEQ'
ILLUMINAX10 = 'ILLUMINA-X10'
ILLUMINAX5 = 'ILLUMINA-X5'
PACBIORSII = 'PACBIO-RSII'
IONTORRENTPROTON = 'ION-TORRENT-PROTON'
IONTORRENTPGM = 'ION-TORRENT-PGM'

PLATFORM = (
    (ILLUMINAHISEQ2000, ILLUMINAHISEQ2000),
    (ILLUMINAHISEQ2500, ILLUMINAHISEQ2500),
    (ILLUMINAMISEQ, ILLUMINAMISEQ),
    (ILLUMINAX10, ILLUMINAX10),
    (ILLUMINAX5, ILLUMINAX5),
    (PACBIORSII, PACBIORSII),
    (IONTORRENTPROTON, IONTORRENTPROTON),
    (IONTORRENTPGM, IONTORRENTPGM),
    )
"""
List of value, verbose_name pairs for the
:attr:`~.models.Workflow.sequencing_platform` attribute.
"""

# READ LENGTH
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RL50 = '50'
RL100 = '100'
RL125 = '125'
RL150 = '150'
RL200 = '200'
RL225 = '225'
RL250 = '250'

READ_LENGTH = (
    (RL50, RL50),
    (RL100, RL100),
    (RL125, RL125),
    (RL150, RL150),
    (RL200, RL200),
    (RL225, RL225),
    (RL250, RL250),
)
"""
List of value, verbose_name pairs for the
:attr:`~.models.Workflow.read_lenght` attribute.
"""

# READ TYPE
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SINGLEEND = 'SINGLE-END'
PAIREND = 'PAIR-END'

READ_TYPE = (
    (SINGLEEND, SINGLEEND),
    (PAIREND, PAIREND),
    )
"""
List of value, verbose_name pairs for the
:attr:`~.models.Workflow.read_type` attribute.
"""

# ALL CHOICES
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
WORKFLOW_CHOICES = {
    "CENTER": CENTER,
    "TECHNOLOGY": TECHNOLOGY,
    "TECHNOLOGY_TYPE": TECHNOLOGY_TYPE,
    "PLATFORM": PLATFORM,
    "READ_LENGTH": READ_LENGTH,
    "READ_TYPE": READ_TYPE,
    }
"""
Dictionary including all
:class:`Workflow's <~.models.Workflow>` choices.
"""

# INTERNAL ID CHARACTERS
# =============================================================================

# INT_ID TECHNOLOGY | TECHNOLOGY_TYPE
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INT_ID_TECHNOLOGY = {

    DNA: {

        WHOLEGENOME: {
            "DEFAULT_TECHNOLOGY": DEFAULT,
            DEFAULT: "1A",
            },

        WHOLEEXOME: {
            "DEFAULT_TECHNOLOGY": AGILENT50MB,
            AGILENT50MB: "2A",
            AGILENT51MB: "2B",
            },

        TARGETEDDNA: {
            "DEFAULT_TECHNOLOGY": HEMEPACTV1,
            HEMEPACTV1: "4A",
            HEMEPACTV2: "4B",
            HEMEPACTV3: "4C",
            IMPACTHEME: "4D",
            IMPACT300: "5A",
            IMPACT340: "5B",
            IMPACTCLINICAL: "5C",
            },

        CHIPSEQ: {
            "DEFAULT_TECHNOLOGY": H3K4ME1,
            H3K4ME1: "6A",
            H3K4ME3: "6B",
            H3K4ME2: "6C",
            H3K27AC: "6D",
            },

        ATACSEQ: {
            "DEFAULT_TECHNOLOGY": DEFAULT,
            DEFAULT: "10A",
            },

        FOUNDATION: {
            "DEFAULT_TECHNOLOGY": FOUNDATIONONHEMEPANEL,
            FOUNDATIONONHEMEPANEL: "12A",
            FOUNDATIONONPANEL: "12B",
            },

        },

    RNA: {

        RNASEQ: {
            "DEFAULT_TECHNOLOGY": FULLTRANSCRIPT,
            FULLTRANSCRIPT: "3A",
            THREEPRIMEEND: "3B",
            },

        RNASEQCUSTOM: {
            "DEFAULT_TECHNOLOGY": DEFAULT,
            DEFAULT: "9A",
            },

        RNASEQSINGLECELL: {
            "DEFAULT_TECHNOLOGY": DEFAULT,
            DEFAULT: "10A",
            },

        }

    }
"""
``Analyte/Technology/Technolgy Type`` codes dictionary.
"""

# INTERNAL ID SEQUENCING CENTER
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INT_ID_CENTER = {
    CMO: 'CMO',
    NYGC: 'NYGC',
    FOUNDATION: 'FNDTN',
    ILLUMINA: 'ILLMN',
    SANGER: 'SNGR',
    }
"""
Characters used in the **leukid** to describe the ``Workflow's``
:attr:`~leukapp.apps.workflows.models.Workflow.sequencing_center` attribute.
"""

# INTERNAL ID SEQUENCING PLATFORM
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INT_ID_PLATFORM = {
    ILLUMINAHISEQ2000: 'HISQ2K',
    ILLUMINAHISEQ2500: 'HISQ25K',
    ILLUMINAMISEQ: 'MISQ',
    ILLUMINAX10: 'X10',
    ILLUMINAX5: 'X5',
    PACBIORSII: 'RSII',
    IONTORRENTPROTON: 'IONTP',
    IONTORRENTPGM: 'IONTPGM',
    }
"""
Characters used in the **leukid** to describe the ``Workflow's``
:attr:`~leukapp.apps.workflows.models.Workflow.sequencing_platform` attribute.
"""

# INTERNAL ID READ LENGTH
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INT_ID_READ_LENGTH = {
    RL50: '50',
    RL100: '100',
    RL125: '125',
    RL150: '150',
    RL200: '200',
    RL225: '225',
    RL250: '250',
    }
"""
Characters used in the **leukid** to describe the ``Workflow's``
:attr:`~leukapp.apps.workflows.models.Workflow.read_lenght` attribute.
"""

# READ TYPE
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INT_ID_READ_TYPE = {
    SINGLEEND: 'S',
    PAIREND: 'P',
    }
"""
Characters used in the **leukid** to describe the ``Workflow's``
:attr:`~leukapp.apps.workflows.models.Workflow.read_type` attribute.
"""

# PERMISSIONS
# =============================================================================

#: Tuple of permissions required to create a new instance.
WORKFLOW_CREATE_PERMISSIONS = ('workflows.add_workflow',)

#: Tuple of permissions required to update an existing instance.
WORKFLOW_UPDATE_PERMISSIONS = ('workflows.change_workflow',)

# MESSAGES
# =============================================================================

#: Sucess message.
SUCCESS_MESSAGE = SUCCESS_MESSAGE

#: Permission denied message.
PERMISSION_DENIED_MESSAGE = PERMISSION_DENIED_MESSAGE
