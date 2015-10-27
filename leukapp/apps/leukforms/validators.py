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
from .constants import LEUKFORM_CSV_FIELDS
# used to map csv headers to location fields


def leukform_csv_validator(document):
    # check file valid csv format
    tmp_path = 'tmp/%s' % document.name[2:]
    default_storage.save(tmp_path, ContentFile(document.file.read()))
    full_tmp_path = os.path.join(settings.MEDIA_ROOT, tmp_path)

    try:
        with open(full_tmp_path, 'r') as leukform:
            rows = csv.DictReader(leukform, delimiter=",")
            rows = list(rows)
            try:
                row = rows[0]
                keys = set(row.keys())
                leukformcsvfields = set(LEUKFORM_CSV_FIELDS)
                if not leukformcsvfields.issubset(keys):
                    dif = leukformcsvfields - keys
                    msg = u'Invalid leukform: missing columns, %s' % str(dif)
                    raise ValidationError(msg)
            except IndexError:
                raise ValidationError(u'Invalid leukform: empty rows.')
    except csv.Error:
        raise ValidationError(u'Not a valid csv file.')
    except UnicodeDecodeError:
        msg = u'Invalid encoding type. '
        msg += 'Please use utf-8 and make sure is a valid csv file.'
        raise ValidationError(msg)

    default_storage.delete(full_tmp_path)
    return True
