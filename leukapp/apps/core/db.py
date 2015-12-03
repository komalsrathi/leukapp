# -*- coding: utf-8 -*-

"""
Custom fields and database-related code use across the :mod:`leukapp` project.
"""

# django
from django.db import models

# local
from .constants import UNKNOWN


class CharNullField(models.CharField):

    """
    Subclass of the CharField that allows empty strings to be stored as NULL.

    .. important:
        Empty strings are equal to empty strings for uniqueness checks.
        However, NULL values aren't. As such, the use of this custom field
        enables the ability to have multiple NULL values but unique non-NULL
        records.
    """

    description = "CharField that stores NULL but returns %s." % UNKNOWN

    def from_db_value(self, value, expression, connection, contex):
        """
        Gets value right out of the db and changes it if its ``None``.
        """
        if value is None:
            return UNKNOWN
        else:
            return value

    def to_python(self, value):
        """
        Gets value right out of an instance, and changes it if its ``None``.
        """
        if isinstance(value, models.CharField):
            # If an instance, just return the instance.
            return value
        if value is None:
            # If db has NULL, convert it to UNKNOWN.
            return UNKNOWN

        # Otherwise, just return the value.
        return value

    def get_prep_value(self, value):
        """
        Catches value right before sending to db.
        """
        if (value is UNKNOWN) or (value is ''):
            # If Django tries to save an empty string, send the db None (NULL).
            return None
        else:
            # Otherwise, just pass the value.
            return value
