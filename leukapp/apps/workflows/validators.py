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


def technology_type_validator(analyte, sequencing_technology, technology_type):
    """
    Validates the analyte/technology/technology_type combination.

    :param str analyte: :data:`~leukapp.apps.extractions.constants.ANALYTE`
    :param str sequencing_technology: :data:`~.constants.SEQUENCING_TECHNOLOGY`
    :param str technology_type: :data:`~.constants.TECHNOLOGY_TYPE`
    """

    if sequencing_technology not in constants.INT_ID_TECHNOLOGY[analyte]:
        msg = _("Invalid analyte/sequencing_technology combination.")
        raise ValidationError(msg, code='invalid_technology')

    types = constants.INT_ID_TECHNOLOGY[analyte][sequencing_technology]
    if technology_type not in types:
        msg = _("Invalid sequencing_technology/technology_type combination.")
        raise ValidationError(msg, code='invalid_technology_type')

    return True


# ROUTINE PROTECTION
# =============================================================================

if __name__ == '__main__':
    pass
