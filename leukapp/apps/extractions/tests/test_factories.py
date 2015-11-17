# -*- coding: utf-8 -*-

# django
from django.test import TestCase

# leukapp
from leukapp.apps.aliquots.factories import AliquotFactory

# local
from ..models import Extraction
from ..factories import ExtractionFactory
from .. import constants


class ExtractionFactoriesTest(TestCase):

    def test_runfactory_creates_run(self):
        a = ExtractionFactory()
        b = Extraction.objects.get(pk=a.pk)
        self.assertEqual(a, b)

    def test_runfactory_doesnt_create_existing_run(self):
        a = AliquotFactory()
        r_a = ExtractionFactory(aliquot=a, ext_id='1', analyte=constants.DNA)
        r_b = ExtractionFactory(aliquot=a, ext_id='1', analyte=constants.DNA)
        self.assertEqual(r_a, r_b)

    def test_aliquotfactory_ext_id_len_is_correct(self):
        a = ExtractionFactory()
        self.assertEqual(len(a.ext_id), 12)
