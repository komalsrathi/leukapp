# -*- coding: utf-8 -*-

"""
Tests for mod:`extractions.factories`.
"""

# django
from django.test import TestCase

# local
from ..models import Extraction
from ..factories import ExtractionFactory
from .. import constants


class ExtractionFactoriesTest(TestCase):

    """
    Tests for mod:`extractions.factories`.
    """

    def test_extractionfactory_creates_extraction(self):
        """
        ExtractionFactory must create instance correctly.
        """
        a = ExtractionFactory()
        b = Extraction.objects.get(pk=a.pk)
        self.assertEqual(a, b)

    def test_extractionfactory_doesnt_create_existing_extraction(self):
        e, kwargs = ExtractionFactory(), {}
        for field in constants.EXTRACTION_CREATE_FIELDS:
            kwargs[field] = getattr(e, field)
        self.assertEqual(e, ExtractionFactory(**kwargs))

    def test_extractionfactory_does_create_extraction(self):
        e, kwargs = ExtractionFactory(ext_id=None), {}
        for field in constants.EXTRACTION_CREATE_FIELDS:
            kwargs[field] = getattr(e, field)
        self.assertNotEqual(e, Extraction.objects.create(**kwargs))

    def test_extractionfactory_attributes_are_correct(self):
        """
        Instance attributes must have correct choices.
        """
        a = ExtractionFactory()
        self.assertEqual(len(a.ext_id), 12)
        self.assertIn(a.analyte, [e[0] for e in constants.ANALYTE])
        self.assertIn(a.center, [e[0] for e in constants.CENTER])
        self.assertIn(a.technology, [e[0] for e in constants.TECHNOLOGY])
        self.assertIn(a.platform, [e[0] for e in constants.PLATFORM])
