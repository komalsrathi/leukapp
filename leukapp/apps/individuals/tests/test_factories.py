# -*- coding: utf-8 -*-

# django
from django.test import TestCase

# local
from ..models import Individual
from ..factories import IndividualFactory
from ..constants import MSK, HUMAN


class FactoriesTest(TestCase):

    def test_individualfactory_creates_individual(self):
        a = IndividualFactory()
        b = Individual.objects.get(pk=a.pk)
        self.assertEqual(a, b)

    def test_individualfactory_doesnt_create_existing_individual(self):
        a = IndividualFactory(institution=MSK, species=HUMAN, ext_id='1')
        b = IndividualFactory(institution=MSK, species=HUMAN, ext_id='1')
        self.assertEqual(a, b)

    def test_individualfactory_ext_id_len_is_correct(self):
        a = IndividualFactory()
        self.assertEqual(len(a.ext_id), 12)
