# -*- coding: utf-8 -*-

"""
:mod:`workflows` validators.

Please refer to `Django's validation documentation`_ to learn more and follow
best practices.

.. _Django's validation documentation:
    https://docs.djangoproject.com/en/1.8/ref/forms/validation/

"""

# django
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

# local
from . import constants


def projects_string_validator(projects_string):
    """
    Validates that the :attr:`projects_string` has the correct format.
    """

    if not projects_string:
        return True

    try:
        [int(e) for e in projects_string.split("|")]
    except Exception:
        msg = _("Invalid format (use: '100|102|103').")
        raise ValidationError(msg, code='invalid')

    return True


def technology_validator(analyte, technology):
    """
    Validates whether or not the technology-analyte combination is valid.
    """

    if technology not in constants.INT_ID_TECHNOLOGY[analyte]:
        msg = _("Invalid technology.")
        raise ValidationError(msg, code='invalid')

    return True


def technology_type_validator(analyte, technology, technology_type):
    """
    Validates whether or not the technology-platform combination is valid.
    """

    if technology_type not in constants.INT_ID_TECHNOLOGY[analyte][technology]:
        msg = _("Invalid technology-platform combination.")
        raise ValidationError(msg, code='invalid')

    return True


# ROUTINE PROTECTION
# =============================================================================

if __name__ == '__main__':
    pass
