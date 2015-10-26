# -*- coding: utf-8 -*-

# django
from django.test import TestCase

# leukapp
from leukapp.apps.individuals.factories import IndividualFactory

# local
from ..models import Specimen
from ..factories import SpecimenFactory
from ..constants import TUMOR

class SpecimenUtilsTest(TestCase):

    def test_specimenfactory_creates_specimen(self):
        a = SpecimenFactory()
        b = Specimen.objects.get(pk=a.pk)
        self.assertEqual(a, b)

    def test_specimenfactory_doesnt_create_existing_specimen(self):
        i = IndividualFactory()
        a = SpecimenFactory(
            individual=i, source_type=TUMOR, ext_id='1')
        b = SpecimenFactory(
            individual=i, source_type=TUMOR, ext_id='1')
        self.assertEqual(a, b)

    def test_specimenfactory_ext_id_len_is_correct(self):
        a = SpecimenFactory()
        self.assertEqual(len(a.ext_id), 12)
