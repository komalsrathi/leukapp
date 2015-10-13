# -*- coding: utf-8 -*-

# django
from django.test import TestCase

# local
from ..models import Individual
from .. import utils


class IndividualModelTest(TestCase):

    def test_individualfactory_creates_individual(self):
        a = utils.IndividualFactory()
        b = Individual.objects.get(pk=a.pk)
        self.assertEqual(a, b)

    def test_individualfactory_doesnt_create_existing_individual(self):
        a = utils.IndividualFactory(institution='MSK', species='H', ext_id='1')
        b = utils.IndividualFactory(institution='MSK', species='H', ext_id='1')
        self.assertEqual(a, b)

    def test_individualfactory_ext_id_len_is_correct(self):
        a = utils.IndividualFactory()
        self.assertEqual(len(a.ext_id), 12)
