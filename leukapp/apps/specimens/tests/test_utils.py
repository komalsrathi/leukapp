# -*- coding: utf-8 -*-

# django
from django.test import TestCase

# leukapp
from leukapp.apps.individuals.utils import IndividualFactory

# local
from ..models import Specimen
from .. import utils


class SpecimenUtilsTest(TestCase):

    def test_specimenfactory_creates_specimen(self):
        a = utils.SpecimenFactory()
        b = Specimen.objects.get(pk=a.pk)
        self.assertEqual(a, b)

    def test_specimenfactory_doesnt_create_existing_specimen(self):
        i = IndividualFactory()
        a = utils.SpecimenFactory(individual=i, source='T', ext_id='1')
        b = utils.SpecimenFactory(individual=i, source='T', ext_id='1')
        self.assertEqual(a, b)

    def test_specimenfactory_ext_id_len_is_correct(self):
        a = utils.SpecimenFactory()
        self.assertEqual(len(a.ext_id), 12)
