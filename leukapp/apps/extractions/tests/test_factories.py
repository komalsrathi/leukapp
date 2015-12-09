# -*- coding: utf-8 -*-

"""
Tests for mod:`extractions.factories`.
"""

# django
from django.test import TestCase
from django.db.utils import IntegrityError

# leukapp
from leukapp.apps.aliquots.factories import AliquotFactory

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

    def test_specimenfactory_doesnt_create_existing_specimen(self):
        a = AliquotFactory()
        e = ExtractionFactory(ext_id='', aliquot=a)
        e2 = ExtractionFactory(ext_id=e.ext_id, aliquot=a)
        self.assertEqual(e, e2)

    def test_extractionfactory_raises_duplicate_error(self):
        e, kwargs = ExtractionFactory(ext_id=''), {}
        with self.assertRaises(IntegrityError):
            for field in constants.EXTRACTION_CREATE_FIELDS:
                kwargs[field] = getattr(e, field)
            Extraction.objects.create(**kwargs)

    def test_extractionfactory_attributes_are_correct(self):
        """
        Instance attributes must have correct choices.
        """
        a = ExtractionFactory()
        self.assertEqual(len(a.ext_id), 12)
        self.assertIn(a.analyte, [e[0] for e in constants.ANALYTE])
