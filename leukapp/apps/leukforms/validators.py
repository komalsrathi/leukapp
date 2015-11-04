# -*- coding: utf-8 -*-

# python
import csv
import os

# django
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.conf import settings

# local
from .constants import MODELS_LIST, LEUKFORM_FIELDS
# used to map csv headers to location fields


def leukform_csv_validator(document):
    """ NOTTESTED """
    if type(document) == str:
        path = document
    else:
        tmp_path = 'tmp/%s' % document.name
        path = os.path.join(settings.MEDIA_ROOT, tmp_path)
        default_storage.delete(path)  # Delete file in case it exists
        default_storage.save(tmp_path, ContentFile(document.file.read()))
    try:
        with open(path, 'r') as leukform:
            rows = csv.DictReader(leukform, delimiter=",")
            leukform_rows_validator(rows)
    except csv.Error:
        raise ValidationError(u'Not a valid csv file.')
    except UnicodeDecodeError:
        msg = u'Invalid encoding type: use utf-8 and a valid csv file.'
        raise ValidationError(msg)
    default_storage.delete(path)
    return True


def leukform_rows_validator(rows):
    """ Validate that rows look good """
    if not rows:
        raise ValidationError(u"Invalid leukform: couldn't read rows.")
    try:
        rows = list(rows)
    except (ValueError, TypeError):
        raise ValidationError(u"Invalid leukform: couldn't parse rows.")

    leukform_columns_validator(rows)  # Validate columns
    leukform_specimen_order_validator(rows)  # Validate specimen order

    return True


def leukform_columns_validator(rows):
    """ Validate the leukform columns being submitted """

    if type(rows[0]) != dict:
        raise ValidationError(u"Invalid leukform: invalid row content")
    try:
        columns = list(rows[0])
    except (ValueError, TypeError):
        raise ValidationError(u"Invalid leukform: couldn't parse columns.")
    if not columns:
        raise ValidationError(u"Invalid leukform: couldn't parse columns.")
    if type(columns) != list:
        raise ValidationError(u"Invalid leukform: couldn't parse columns.")
    if len(columns) == 0:
        raise ValidationError(u"Invalid leukform: couldn't parse columns.")

    # Validate whether or not columns are valid leukform fields
    for column in columns:
        msg = u"Invalid leukform: invalid column '%s'." % column
        try:
            model, field = column.split('.')
            notinleukform = (field not in LEUKFORM_FIELDS[model])
            notslug = (field != 'slug')
            if model not in MODELS_LIST or (notinleukform and notslug):
                raise ValidationError(msg)
        except (ValueError, AttributeError, KeyError):
            raise ValidationError(msg)

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
    msg_template = u"Invalid leukform: Specimen.order has to be unique " + \
        "at Individual and Specimen.ext_id levels. Error found in row: {0}"
    count = 1
    if ('Specimen.order' in columns) and ('Specimen.ext_id' in columns):
        if 'Individual.slug' in columns:
            key_cols = ('Specimen.order', 'Individual.slug')
        else:
            key_cols = ('Specimen.order', 'Individual.ext_id')
        for row in rows:
            count += 1
            msg = msg_template.format(count)
            c1 = row['Specimen.ext_id'] is not None
            c2 = row['Specimen.order'] is not None
            if c1 and c2:
                key = "-".join(str(row[col]) for col in key_cols)
                if key not in unique:
                    unique[key] = row['Specimen.ext_id']
                else:
                    if unique[key] != row['Specimen.ext_id']:
                        raise ValidationError(msg)
    return True
