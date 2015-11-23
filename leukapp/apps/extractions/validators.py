# -*- coding: utf-8 -*-

# django
from django.core.exceptions import ValidationError


def projects_string_validator(projects_string):
    """ NOTTESTED NOTDOCUMENTED """
    if not projects_string:
        return True
    try:
        [int(e) for e in projects_string.split("|")]
    except Exception:
        msg = u"Invalid project list format (e.g. please follow: '1|2|3')."
        raise ValidationError(msg)
    return True
