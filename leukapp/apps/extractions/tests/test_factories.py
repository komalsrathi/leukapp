# -*- coding: utf-8 -*-

# django
from django.test import TestCase

# local
from ..models import Extraction
from ..factories import ExtractionFactory


class ExtractionFactoriesTest(TestCase):

    def test_runfactory_creates_run(self):
        a = ExtractionFactory()
        b = Extraction.objects.get(pk=a.pk)
        self.assertEqual(a, b)

    def test_aliquotfactory_ext_id_len_is_correct(self):
        a = ExtractionFactory()
        self.assertEqual(len(a.ext_id), 12)
