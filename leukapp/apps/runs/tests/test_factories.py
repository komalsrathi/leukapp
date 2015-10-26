# -*- coding: utf-8 -*-

# django
from django.test import TestCase

# leukapp
from leukapp.apps.aliquots.factories import AliquotFactory

# local
from ..models import Run
from ..factories import RunFactory


class AliquotUtilsTest(TestCase):

    def test_aliquotfactory_creates_aliquot(self):
        a = RunFactory()
        b = Run.objects.get(pk=a.pk)
        self.assertEqual(a, b)

    def test_aliquotfactory_doesnt_create_existing_sample(self):
        a = AliquotFactory()
        s_a = RunFactory(aliquot=a, ext_id='1')
        s_b = RunFactory(aliquot=a, ext_id='1')
        self.assertEqual(s_a, s_b)

    def test_aliquotfactory_ext_id_len_is_correct(self):
        a = RunFactory()
        self.assertEqual(len(a.ext_id), 12)
