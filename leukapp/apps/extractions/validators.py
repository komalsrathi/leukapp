# -*- coding: utf-8 -*-

# django
from django.core.exceptions import ValidationError


def projects_list_validator(projects_list):
    """ NOTTESTED NOTDOCUMENTED """
    if not projects_list:
        return True
    try:
        [int(e) for e in projects_list.split("|")]
    except Exception:
        msg = u"Invalid project list format (e.g. please follow: '1|2|3')."
        raise ValidationError(msg)
    return True
