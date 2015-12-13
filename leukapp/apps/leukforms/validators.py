# -*- coding: utf-8 -*-

"""
:mod:`leukforms` validators.

Please refer to `Django's validation documentation`_ to learn more and follow
best practices.

.. _Django's validation documentation:
    https://docs.djangoproject.com/en/1.8/ref/forms/validation/

"""

# python
import csv
import os

# django
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# local
from .constants import MODELS_LIST, CREATE_FIELDS


# LEUKFORM VALIDATORS
# =============================================================================

def leukform_csv_validator(document):
    """.. todo: NOTTESTED, NOTDOCUMENTED."""
    if type(document) == str:
        path = document
    else:
        tmp_path = 'tmp/%s' % document.name
        path = os.path.join(settings.MEDIA_ROOT, tmp_path)
        default_storage.delete(tmp_path)  # Delete file in case it exists
        document.file.seek(0)
        default_storage.save(tmp_path, ContentFile(document.file.read()))
    try:
        with open(path, 'r') as leukform:
            rows = csv.DictReader(leukform, delimiter=",", dialect=csv.excel)
            leukform_rows_validator(rows)
    except csv.Error:
        msg = _('Not a valid csv file.')
        raise ValidationError(msg, code='invalid_file')
    except UnicodeDecodeError:
        msg = _('Invalid encoding type: use utf-8 and a valid csv file.')
        raise ValidationError(msg, code='invalid_file')

    return True


def leukform_rows_validator(rows):
    """
    Validate the ``rows`` format.

    This validator ensures that `rows` isn't empty and that can be
    converted to a list. It also checks if the contents are dictionaries.
    Additionally, it calls :func:`~leukform_columns_validator` to validate the
    columns and :func:`~leukform_specimen_order_validator` to validate custom
    :mod:`~leukapp.apps.specimens.models.Specimen` order functionality.
    """
    try:
        rows = list(rows)
    except (ValueError, TypeError):
        msg = _("Couldn't parse rows.")
        raise ValidationError(msg, code='invalid_rows')
    if not rows:
        msg = _("Couldn't read rows.")
        raise ValidationError(msg, code='invalid_rows')
    if len(rows) == 0:
        msg = _("Empty rows.")
        raise ValidationError(msg, code='invalid_rows')
    if type(rows[0]) != dict:
        msg = _("Invalid row content")
        raise ValidationError(msg, code='invalid_rows')

    leukform_columns_validator(rows)            # Validate columns
    leukform_specimen_order_validator(rows)     # Validate specimen order

    return True


def leukform_columns_validator(rows):
    """
    Validate the :mod:`~Leukform` columns.

    First checks if `rows` contents are dictionaries. Then, converts the
    columns to a list and checks that it's not empty. Lastly, loops over the
    columns valitading that they are correct `leukform` fields.
    """
    # converts columns to list.
    try:
        columns = list(rows[0])
    except (ValueError, TypeError):
        msg = _("Couldn't parse columns.")
        raise ValidationError(msg, code='invalid_columns')

    # checks that the columns aren't empty.
    if len(columns) == 0:
        msg = _("Empty columns.")
        raise ValidationError(msg, code='invalid_columns')

    # Validate whether or not columns are valid leukform fields
    for column in columns:
        msg = _("Column '%(column)s' isn't valid.")
        params = {"column": column}
        try:
            model, field = column.split('.')
            fieldnotinleukform = (field not in CREATE_FIELDS[model])
            notslug = (field != 'slug')
            if (model not in MODELS_LIST) or (fieldnotinleukform and notslug):
                raise ValidationError(
                    msg, code='invalid_columns', params=params)
        except (ValueError, AttributeError, KeyError):
            msg = _("Couldn't parse columns.")
            raise ValidationError(msg, code='invalid_columns')

    return True


def leukform_specimen_order_validator(rows):
    """
    Validate whether or not the order submitted is valid.

    This function makes sure that the Specimen.order is unique at the
    Individual.ext_id (or Individual.slug if the leukid is submitted)
    and Specimen.ext_id levels.
    """

    columns = list(rows[0])
    unique = {}
    msg = _(
        "Specimen.order has to be unique "
        "at Individual and Specimen.ext_id levels. Error found in row: %(row)s"
        )

    count = 1
    if ('Specimen.order' in columns) and ('Specimen.ext_id' in columns):
        if 'Individual.slug' in columns:
            key_cols = ('Specimen.order', 'Individual.slug')
        else:
            key_cols = ('Specimen.order', 'Individual.ext_id')
        for row in rows:
            count += 1
            params = {"count": count}
            if row['Specimen.ext_id'] and row['Specimen.order']:
                key = "-".join(str(row[col]) for col in key_cols)
                if key not in unique:
                    unique[key] = row['Specimen.ext_id']
                else:
                    if unique[key] != row['Specimen.ext_id']:
                        raise ValidationError(
                            msg, code='invalid_order', params=params)
    return True


# ROUTINE PROTECTION
# =============================================================================

if __name__ == '__main__':
    pass
