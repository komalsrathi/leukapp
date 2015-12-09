# -*- coding: utf-8 -*-

"""
Tests for extractions models.
"""

# python
from unittest import skipIf

# django
from django.test import TestCase
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

# leukapp
from leukapp.apps.core import constants as coreconstants
from leukapp.apps.aliquots.factories import AliquotFactory

# local
from ..factories import ExtractionFactory
from ..models import Extraction
from .. import constants


class ExtractionsModelTest(TestCase):

    def test_saving_and_retrieving_extractions(self):
        e = ExtractionFactory()
        extractions = Extraction.objects.all()
        self.assertEqual(extractions.count(), 1)
        self.assertEqual(extractions[0], e)

    def test_ext_id_uses_validator(self):
        with self.assertRaises(ValidationError):
            ExtractionFactory(ext_id="1234 % ''10").full_clean()

    @skipIf((not constants.EXTRACTION_UNIQUE_TOGETHER), "not unique fields")
    def test_unique_together_functionality(self):
        e, kwargs = ExtractionFactory(ext_id=''), {}
        with self.assertRaises(IntegrityError):
            for field in constants.EXTRACTION_CREATE_FIELDS:
                kwargs[field] = getattr(e, field)
            Extraction.objects.create(**kwargs)

    def test_if_extractions_count_keep_count_correctly(self):
        a = AliquotFactory()
        for i in range(2):
            ExtractionFactory(aliquot=a, analyte=constants.DNA)
            ExtractionFactory(aliquot=a, analyte=constants.RNA)
        self.assertEqual(2, a.dna_extractions_count)
        self.assertEqual(2, a.rna_extractions_count)

    def test_if_extractions_count_is_correct_after_delete_extractions(self):
        a = AliquotFactory()
        for i in range(2):
            ExtractionFactory(aliquot=a, analyte=constants.DNA).delete()
            ExtractionFactory(aliquot=a, analyte=constants.RNA).delete()
        self.assertEqual(2, a.dna_extractions_count)
        self.assertEqual(2, a.rna_extractions_count)

    def test_str_returns_slug(self):
        e = ExtractionFactory()
        slug = '-'.join([e.aliquot.slug, e.int_id])
        self.assertEqual(slug, e.__str__())

    def test_get_absolute_url(self):
        e = ExtractionFactory()
        slug = e.slug
        url = reverse(constants.APP_NAME + ':detail', kwargs={'slug': slug})
        self.assertEqual(url, e.get_absolute_url())

    def test_get_update_url(self):
        e = ExtractionFactory()
        slug = e.slug
        url = reverse(constants.APP_NAME + ':update', kwargs={'slug': slug})
        self.assertEqual(url, e.get_update_url())

    def test_int_id_returns_expected_value(self):
        a = AliquotFactory()
        rdna = ExtractionFactory(aliquot=a, analyte=constants.DNA)
        rrna = ExtractionFactory(aliquot=a, analyte=constants.RNA)
        rdna_int_id = constants.INT_ID_ANALYTE[rdna.analyte]
        rdna_int_id += str(a.dna_extractions_count)
        rrna_int_id = constants.INT_ID_ANALYTE[rrna.analyte]
        rrna_int_id += str(a.rna_extractions_count)
        self.assertEqual(rdna.int_id, rdna_int_id)
        self.assertEqual(rrna.int_id, rrna_int_id)
