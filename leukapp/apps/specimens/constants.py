# -*- coding: utf-8 -*-

"""
This module contains the :mod:`~leukapp.apps.specimens` app constants.
Information that isn't likely to change and that is used across the
:mod:`~leukapp.apps.specimens` app and the :mod:`~leukapp` project
should be stored here.

.. important::
    **DO NOT** change any constant unless you know what you are doing.
"""

# leukapp
from leukapp.apps.core import constants as coreconstants

# APP INFO
# -----------------------------------------------------------------------------
APP_NAME = 'specimens'  #: Application's name.

# URLS
# -----------------------------------------------------------------------------
SPECIMEN_CREATE_URL = APP_NAME + ':create'  #: Create URL reverse string.
SPECIMEN_LIST_URL = APP_NAME + ':list'      #: List URL reverse string.

# FIELDS
# -----------------------------------------------------------------------------

#: Fields required to create a new instance.
SPECIMEN_CREATE_FIELDS = (
    'individual',
    'source',
    'source_type',
    'ext_id',
    'order',
    )

#: Enabled fields to update an existing instance.
SPECIMEN_UPDATE_FIELDS = (
    'source',
    )

#: Fields that are required to be unique together.
SPECIMEN_UNIQUE_TOGETHER = (
    'individual',
    'ext_id',
    'source_type',
    )

# CHOICES
# -----------------------------------------------------------------------------
BLOOD = 'BLOOD'
NAILS = 'NAILS'
BUCCAL = 'BUCCAL'
HAIR = 'HAIR'
TCELLS = 'TCELLS'
SOURCE = (
    (BLOOD, BLOOD),
    (NAILS, NAILS),
    (BUCCAL, BUCCAL),
    (HAIR, HAIR),
    (TCELLS, TCELLS),
)
"""
List of value, verbose_name pairs for the
:attr:`~leukapp.apps.specimens.models.Specimen.source` attribute.
"""

SOURCE_VALUE = [s[0] for s in SOURCE]
"""
Values for the :attr:`~leukapp.apps.specimens.models.Specimen.source`
attribute.
"""

TUMOR = 'TUMOR'
NORMAL = 'NORMAL'
SOURCE_TYPE = (
    (TUMOR, 'TUMOR'),
    (NORMAL, 'NORMAL'),
)
"""
List of value, verbose_name pairs for the
:attr:`~leukapp.apps.specimens.models.Specimen.source_type` attribute.
"""

SOURCE_TYPE_VALUE = [s[0] for s in SOURCE_TYPE]
"""
Values for the :attr:`~leukapp.apps.specimens.models.Specimen.source_type`
attribute.
"""

SPECIMEN_CHOICES = {
    "SOURCE": SOURCE,
    "SOURCE_TYPE": SOURCE_TYPE,
}
"""
Dictionary including all
:class:`Specimen's <~leukapp.apps.specimens.models.Specimen>` choices.
"""

LEUKID_SOURCE_TYPE = {
    TUMOR: 'T',
    NORMAL: 'N',
    }
"""
Characters used in the **leukid** to describe the `Specimen's`
:attr:`~leukapp.apps.specimens.models.Specimen.source_type` attribute.
"""

# PERMISSIONS
# -----------------------------------------------------------------------------

#: Tuple of permissions required to create a new instance.
SPECIMEN_CREATE_PERMISSIONS = ('specimens.add_specimen',)

#: Tuple of permissions required to update an existing instance.
SPECIMEN_UPDATE_PERMISSIONS = ('specimens.change_specimen',)

# MESSAGES
# -----------------------------------------------------------------------------

#: Sucess message.
SUCCESS_MESSAGE = coreconstants.SUCCESS_MESSAGE

#: Permission denied message.
PERMISSION_DENIED_MESSAGE = coreconstants.PERMISSION_DENIED_MESSAGE
