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
from .constants import MODELS
# used to map csv headers to location fields


def leukform_csv_validator(document):
    """ NOTTESTED """
    if type(document) == str:
        path = document
    else:
        tmp_path = 'tmp/%s' % document.name[2:]
        default_storage.save(tmp_path, ContentFile(document.file.read()))
        path = os.path.join(settings.MEDIA_ROOT, tmp_path)
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
    """ tested """
    if not rows:
        raise ValidationError(u"Invalid leukform: couldn't read rows.")
    if type(rows) != list:
        raise ValidationError(u"Invalid leukform: couldn't read rows.")
    try:
        rows, columns, fields = list(rows), list(rows[0]), {}
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
    for column in columns:
        msg = u"Invalid leukform: invalid column '%s'." % column
        try:
            model, field = column.split('.')
            fields[model] = {}
            fields[model][field] = column
            if model not in MODELS:
                raise ValidationError(msg)
        except ValueError:
            raise ValidationError(msg)
        except AttributeError:
            raise ValidationError(msg)
    if not fields['Individual']:
        raise ValidationError(u"Invalid leukform: Individual is required.")
    if (len(fields['Individual']) == 1) and \
       ('leukid' not in fields['Individual']):
        raise ValidationError(u"Invalid leukform: invalid Individual columns.")
    return True
