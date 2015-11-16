# -*- coding: utf-8 -*-

# django
from django.test import TestCase

# leukapp
from leukapp.apps.aliquots.factories import AliquotFactory

# local
from ..models import Run
from ..factories import RunFactory
from .. import constants


class RunFactoriesTest(TestCase):

    def test_runfactory_creates_run(self):
        a = RunFactory()
        b = Run.objects.get(pk=a.pk)
        self.assertEqual(a, b)

    def test_runfactory_doesnt_create_existing_run(self):
        a = AliquotFactory()
        r_a = RunFactory(aliquot=a, ext_id='1', analyte=constants.DNA)
        r_b = RunFactory(aliquot=a, ext_id='1', analyte=constants.DNA)
        self.assertEqual(r_a, r_b)

    def test_aliquotfactory_ext_id_len_is_correct(self):
        a = RunFactory()
        self.assertEqual(len(a.ext_id), 12)
