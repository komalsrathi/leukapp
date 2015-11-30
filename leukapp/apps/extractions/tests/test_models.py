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
        with self.assertRaises(IntegrityError):
            e, kwargs = ExtractionFactory(), {}
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
        rdna_int_id = constants.LEUKID_ANALYTE[rdna.analyte]
        code = constants.TECHNOLOGY_PLATFORM[rdna.technology][rdna.platform]
        rdna_int_id += str(a.dna_extractions_count) + '-' + code
        rrna_int_id = constants.LEUKID_ANALYTE[rrna.analyte]
        code = constants.TECHNOLOGY_PLATFORM[rrna.technology][rrna.platform]
        rrna_int_id += str(a.rna_extractions_count) + '-' + code
        self.assertEqual(rdna.int_id, rdna_int_id)
        self.assertEqual(rrna.int_id, rrna_int_id)

    def test_unknown_platform_is_replaced_with_default_value(self):
        e = ExtractionFactory(platform=None)
        expected = constants.TECHNOLOGY_PLATFORM[e.technology]["DEFAULT"]
        self.assertEqual(e.platform, expected)

    def test_unique_together_functionality_not_raised_empty_ext_id(self):
        e, kwargs = ExtractionFactory(ext_id=None), {}
        for field in constants.EXTRACTION_CREATE_FIELDS:
            kwargs[field] = getattr(e, field)
        self.assertNotEqual(e, Extraction.objects.create(**kwargs))

    def test_char_null_field_returns_unknown_for_ext_id(self):
        e = ExtractionFactory(ext_id=None)
        e = Extraction.objects.get(pk=e.pk)
        self.assertEqual(e.ext_id, coreconstants.UNKNOWN)
