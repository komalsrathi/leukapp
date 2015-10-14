# -*- coding: utf-8 -*-

# django imports
from django.test import TestCase

# local imports
from .. import utils


class SamplesUtilsTest(TestCase):

    def test_samples_factory_create_batch(self):
        batch = utils.SamplesFactory()
        batch.create_batch(10, 2, 2)
        self.assertEqual(len(batch.individuals), 10)
        self.assertNotEqual(batch.individuals[0].slug, None)
        self.assertNotEqual(batch.specimens[0].slug, None)
        self.assertNotEqual(batch.aliquots[0].slug, None)

    def test_samples_factory_create_rows(self):
        batch = utils.SamplesFactory()
        batch.create_batch(10, 2, 2)
        batch.create_rows()
        self.assertGreater(len(batch.rows), 10 * 3)
        self.assertLessEqual(len(batch.rows), 10 * 2 * 2)
