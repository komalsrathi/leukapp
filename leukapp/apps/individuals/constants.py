# -*- coding: utf-8 -*-

"""
This module contains the :mod:`~leukapp.apps.individuals` app constants.

Information that isn't likely to change and that is used across the
:mod:`~leukapp.apps.individuals` app and the :mod:`~leukapp` project
should be stored here.

.. important::
    **DO NOT** change any constant unless you know what you are doing.
"""

# leukapp
from leukapp.apps.core import constants as coreconstants

# APP INFO
# =============================================================================

APP_NAME = "individuals"  #: Application's name.

# URLS
# =============================================================================
INDIVIDUAL_CREATE_URL = APP_NAME + ":create"  #: Create URL reverse string.
INDIVIDUAL_LIST_URL = APP_NAME + ":list"      #: List URL reverse string.

# FIELDS
# =============================================================================

#: Fields required to create a new instance.
INDIVIDUAL_CREATE_FIELDS = (
    "institution",
    "species",
    "ext_id",
    )

#: Enabled fields to update an existing instance.
INDIVIDUAL_UPDATE_FIELDS = (
    )

#: Fields that are required to be unique together.
INDIVIDUAL_UNIQUE_TOGETHER = (
    "institution",
    "species",
    "ext_id",
    )

# CHOICES
# =============================================================================

# INSTITUTION
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
MSK = "MSK"
ICO = "ICO"
PV = "PV"
IHBT = "IHBT"
OTHER = "OTHER"
INSTITUTION = (
    (MSK, MSK),
    (ICO, ICO),
    (PV, PV),
    (IHBT, IHBT),
    (OTHER, OTHER),
    )
"""
List of value, verbose_name pairs for the
:attr:`~leukapp.apps.individuals.models.Individual.institution` attribute.
"""

# SPECIES
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

HUMAN = "HUMAN"
MOUSE = "MOUSE"
YEAST = "YEAST"
ZEBRAFISH = "ZEBRAFISH"
SPECIES = (
    (HUMAN, HUMAN),
    (MOUSE, MOUSE),
    (YEAST, YEAST),
    (ZEBRAFISH, ZEBRAFISH),
    )
"""
List of value, verbose_name pairs for the
:attr:`~leukapp.apps.individuals.models.Individual.species` attribute.
"""

# ALL CHOICES
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

INDIVIDUAL_CHOICES = {
    "INSTITUTION": INSTITUTION,
    "SPECIES": SPECIES,
    }
"""
Dictionary including all
:class:`Individual's <~leukapp.apps.individuals.models.Individual>` choices.
"""

# INTERNAL ID CHARACTERS
# =============================================================================

# SPECIES
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

INT_ID_SPECIES = {
    HUMAN: "H",
    MOUSE: "M",
    YEAST: "Y",
    ZEBRAFISH: "Z",
    }
"""
Characters used in the **leukid** to describe the `Individual's`
:attr:`~leukapp.apps.individuals.models.Individual.species` attribute.
"""

# PERMISSIONS
# =============================================================================

#: Tuple of permissions required to create a new instance.
INDIVIDUAL_CREATE_PERMISSIONS = ("individuals.add_individual",)

#: Tuple of permissions required to update an existing instance.
INDIVIDUAL_UPDATE_PERMISSIONS = ("individuals.change_individual",)

# MESSAGES
# =============================================================================

#: Sucess message.
SUCCESS_MESSAGE = coreconstants.SUCCESS_MESSAGE

#: Permission denied message.
PERMISSION_DENIED_MESSAGE = coreconstants.PERMISSION_DENIED_MESSAGE
