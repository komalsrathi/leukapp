# -*- coding: utf-8 -*-

"""
Test the ``core.db`` module.
"""

# django
from django.test import TestCase

# local
from ..constants import UNKNOWN
from ..db import CharNullField
from ..models import LeukappTestModel


class DbTest(TestCase):

    def test_char_null_field_to_python_returns_unkwon(self):
        field = CharNullField()
        result = field.to_python(None)
        self.assertEqual(result, UNKNOWN)

    def test_char_null_field_to_python_returns_value(self):
        field = CharNullField()
        result = field.to_python("Juan")
        self.assertEqual(result, "Juan")

    def test_char_null_field_get_prep_value_returns_none(self):
        field = CharNullField()
        result = field.get_prep_value(UNKNOWN)
        self.assertIsNone(result)

    def test_char_null_field_get_prep_value_returns_value(self):
        field = CharNullField()
        result = field.get_prep_value("Juan")
        self.assertEqual(result, "Juan")

    def test_char_null_field_on_model_unknown(self):
        obj = LeukappTestModel.objects.create(testme=None)
        obj = LeukappTestModel.objects.get(pk=obj.pk)
        self.assertEqual(obj.testme, UNKNOWN)

    def test_char_null_field_on_model_known(self):
        obj = LeukappTestModel.objects.create(testme="JUAN")
        obj = LeukappTestModel.objects.get(pk=obj.pk)
        self.assertEqual(obj.testme, "JUAN")
