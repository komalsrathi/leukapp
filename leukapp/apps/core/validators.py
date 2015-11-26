# -*- coding: utf-8 -*-

"""
Core validators used across :mod:`leukapp.apps` applications.
"""

# dango
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


# PHONE VALIDATOR
# =============================================================================
phone_validator = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message=_(
        "Phone number must be entered in the format: '+999999999'. "
        "Up to 15 digits allowed."
        )
    )
"""
Standard phone validator.

Phone numbers must have at least 9 and no more than 15 digits. The `+`
character is allowed.
"""


# SIMPLE NAME VALIDATOR
# =============================================================================
name_validator = RegexValidator(
    regex=r'^[a-zA-Z\s]$',
    message=_(
        "Enter a valid name consisting of letters, numbers, white spaces "
        "and underscores."
        ),
    )
"""
Simple name validator.

This validator allows letters, numbers, white spaces and underscores.
"""


# OBJECT NAME VALIDATOR
# =============================================================================
object_name_validator = RegexValidator(
    regex=r'^[-a-zA-Z0-9_\s]+\Z',
    code='invalid',
    message=_(
        "Enter a valid name consisting of letters, numbers, white spaces, "
        "underscores or hyphens."
        ),
    )
"""
Simple object name validator.

This validator allows letters, numbers, white spaces, underscores and hyphens.
"""


# EXTERNAL ID VALIDATOR
# =============================================================================
ext_id_validator = RegexValidator(
    regex=r'^[-a-zA-Z0-9_.]+\Z',
    code='invalid',
    message=_(
        "Enter a valid 'External id' consisting of "
        "letters, numbers, underscores or hyphens."
        ),
    )
"""
Validates an external id.

This validator uses the same regex as
:class:`django.core.validators.validate_slug`. It allows the use of letters,
numbers, underscores and hyphens.
"""
