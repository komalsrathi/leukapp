# -*- coding: utf-8 -*-

# django
from django.test import TestCase
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

# leukapp
from leukapp.apps.aliquots.factories import AliquotFactory

# local
from ..factories import ExtractionFactory
from ..models import Extraction
from .. import constants


class ExtractionsModelTest(TestCase):

    def test_saving_and_retrieving_extractions(self):
        s = ExtractionFactory()
        extractions = Extraction.objects.all()
        self.assertEqual(extractions.count(), 1)
        self.assertEqual(extractions[0], s)

    def test_ext_id_uses_validator(self):
        with self.assertRaises(ValidationError):
            ExtractionFactory(ext_id="1234 % ''10").full_clean()

    def test_unique_together_functionality(self):
        s = ExtractionFactory()
        with self.assertRaises(IntegrityError):
            kwargs = {
                "aliquot": s.aliquot,
                "ext_id": s.ext_id,
                "analyte": s.analyte,
                }
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
        s = ExtractionFactory()
        slug = '-'.join([s.aliquot.slug, s.int_id])
        self.assertEqual(slug, s.__str__())

    def test_get_absolute_url(self):
        s = ExtractionFactory()
        slug = s.slug
        url = reverse(constants.APP_NAME + ':detail', kwargs={'slug': slug})
        self.assertEqual(url, s.get_absolute_url())

    def test_get_update_url(self):
        s = ExtractionFactory()
        slug = s.slug
        url = reverse(constants.APP_NAME + ':update', kwargs={'slug': slug})
        self.assertEqual(url, s.get_update_url())

    def test_int_id_returns_expected_value(self):
        a = AliquotFactory()
        rdna = ExtractionFactory(aliquot=a, analyte=constants.DNA)
        rrna = ExtractionFactory(aliquot=a, analyte=constants.RNA)
        rdna_int_id = constants.LEUKID_ANALYTE[rdna.analyte]
        rdna_int_id += str(a.dna_extractions_count)
        rrna_int_id = constants.LEUKID_ANALYTE[rrna.analyte]
        rrna_int_id += str(a.rna_extractions_count)
        self.assertEqual(rdna.int_id, rdna_int_id)
        self.assertEqual(rrna.int_id, rrna_int_id)
