# -*- coding: utf-8 -*-

# django
from django.test import TestCase

# leukapp
from leukapp.apps.specimens.factories import SpecimenFactory

# local
from ..models import Aliquot
from ..factories import AliquotFactory


class AliquotUtilsTest(TestCase):

    def test_aliquotfactory_creates_aliquot(self):
        a = AliquotFactory()
        b = Aliquot.objects.get(pk=a.pk)
        self.assertEqual(a, b)

    def test_aliquotfactory_doesnt_create_existing_aliquot(self):
        s = SpecimenFactory()
        a = AliquotFactory(specimen=s, bio_source='T', ext_id='1')
        b = AliquotFactory(specimen=s, bio_source='T', ext_id='1')
        self.assertEqual(a, b)

    def test_aliquotfactory_ext_id_len_is_correct(self):
        a = AliquotFactory()
        self.assertEqual(len(a.ext_id), 12)
