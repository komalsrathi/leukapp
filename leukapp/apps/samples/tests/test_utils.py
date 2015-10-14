# -*- coding: utf-8 -*-

# python
import csv
import os

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
        self.assertGreater(len(batch.rows), 5)
        self.assertLessEqual(len(batch.rows), 10 * 2 * 2)

    def test_csv_from_rows(self):
        batch = utils.SamplesFactory()
        batch.create_batch(1, 1, 1)
        batch.create_rows()
        path = batch.create_csv_from_rows()

        with open(path, 'r') as testcsv:
            rows = csv.DictReader(testcsv, delimiter=",")
            rows = list(rows)

        self.assertCountEqual(batch.rows, rows)
        os.remove(path)
