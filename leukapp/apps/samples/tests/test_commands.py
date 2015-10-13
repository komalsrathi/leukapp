# -*- coding: utf-8 -*-

# django imports
from django.test import TestCase

# apps imports
from leukapp.apps.individuals.models import Individual
from leukapp.apps.specimens.models import Specimen
from leukapp.apps.aliquots.models import Aliquot
from leukapp.apps.projects.models import Project

from leukapp.apps.individuals.utils import IndividualFactory
from leukapp.apps.specimens.utils import SpecimenFactory
from leukapp.apps.aliquots.utils import AliquotFactory

# local imports
from ..management.commands import submit_samples_from_csv


class SamplesCommandsTest(TestCase):

    def setUp(self):
        self.Command = submit_samples_from_csv.Command()

    def test_initialize_out_row(self):
        self.Command.initialize_out_row()

        for model in self.Command.models_names:
            self.assertEqual(
                self.Command.ACTION_NOT_TESTED,
                self.Command.out_row[model + '.id'])

            self.assertEqual(
                self.Command.ACTION_NOT_TESTED,
                self.Command.out_row[model + '.action'])

            self.assertEqual(
                self.Command.ACTION_NOT_TESTED,
                self.Command.out_row[model + '.errors'])
