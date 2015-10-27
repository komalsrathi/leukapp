# -*- coding: utf-8 -*-

# python
import csv
import os

# django
from django.test import TestCase

# leukapp
from leukapp.apps.leukforms.factories import LeukformCsvFactory


class LeukformCsvFactoryTest(TestCase):

    def test_leukform_factory_create_batch(self):
        batch = LeukformCsvFactory()
        batch.create_batch(4, 2, 2, 1)
        batch.create_rows()
        self.assertEqual(len(batch.individuals), 4)
        self.assertNotEqual(batch.individuals[0].slug, None)
        self.assertNotEqual(batch.specimens[0].slug, None)
        self.assertNotEqual(batch.aliquots[0].slug, None)
        self.assertNotEqual(batch.runs[0].slug, None)
        self.assertGreater(len(batch.rows), 5)
        self.assertLessEqual(len(batch.rows), 4 * 2 * 2 * 1)

    def test_csv_from_rows(self):
        batch = LeukformCsvFactory()
        batch.create_batch(1, 1, 1, 1)
        batch.create_rows()
        path = batch.create_csv_from_rows()

        with open(path, 'r') as testcsv:
            rows = csv.DictReader(testcsv, delimiter=",")
            rows = list(rows)

        self.assertCountEqual(batch.rows, rows)
        os.remove(path)
