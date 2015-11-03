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
from .constants import MODELS_LIST
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
    print('deleted!!!')
    default_storage.delete(path)
    return True


def leukform_rows_validator(rows):
    """ tested """
    if not rows:
        raise ValidationError(u"Invalid leukform: couldn't read rows.")
    try:
        rows = list(rows)
    except ValueError:
        raise ValidationError(u"Invalid leukform: couldn't parse rows.")
    except TypeError:
        raise ValidationError(u"Invalid leukform: couldn't parse rows.")

    leukform_columns_validator(rows)
    leukform_specimen_order_unique_together_validator(rows)

    # validate unique together for Specimen.order
    return True


def leukform_columns_validator(rows):
    """ validate the leukform columns being submitted """

    # validate columns are a valid list of names
    if type(rows[0]) != dict:
        raise ValidationError(u"Invalid leukform: invalid row content")
    try:
        columns = list(rows[0])
    except ValueError:
        raise ValidationError(u"Invalid leukform: couldn't parse columns.")
    except TypeError:
        raise ValidationError(u"Invalid leukform: couldn't parse columns.")
    if not columns:
        raise ValidationError(u"Invalid leukform: couldn't parse columns.")
    if type(columns) != list:
        raise ValidationError(u"Invalid leukform: couldn't parse columns.")
    if len(columns) == 0:
        raise ValidationError(u"Invalid leukform: couldn't parse columns.")

    # validate whether or not columns are valid columns names
    for column in columns:
        msg = u"Invalid leukform: invalid column '%s'." % column
        try:
            model, field = column.split('.')
            if model not in MODELS_LIST:
                raise ValidationError(msg)
        except ValueError:
            raise ValidationError(msg)
        except AttributeError:
            raise ValidationError(msg)

    return True


def leukform_specimen_order_unique_together_validator(rows):
    """ validate the leukform columns being submitted """

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
            if row['Specimen.ext_id'] and row['Specimen.order']:
                key = "-".join(str(row[col]) for col in key_cols)
                if key not in unique:
                    unique[key] = row['Specimen.ext_id']
                else:
                    if unique[key] != row['Specimen.ext_id']:
                        print('test key', count, unique)
                        raise ValidationError(msg)
    return True
