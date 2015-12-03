# -*- coding: utf-8 -*-

# python
import csv
import os

# django
from django.test import TestCase

# leukapp
from leukapp.apps.leukforms.factories import LeukformSamplesFactory
from leukapp.apps.aliquots.factories import AliquotFactory

# local
from ..constants import CREATE_FIELDS, MODELS_LIST


class LeukformCsvFactoryTest(TestCase):

    def test_set_parameters_individual(self):
        batch = LeukformSamplesFactory()
        parent = None
        batch.request['Specimen'] = 0
        kwargs, child = batch._update_parameters(
            model='Individual', parent=parent)
        self.assertDictEqual(kwargs, {})
        self.assertEqual(child, 'Specimen')
        self.assertEqual(batch._last, True)

    def test_set_parameters_specimen(self):
        batch = LeukformSamplesFactory()
        parent = 'individualInstance'
        batch.request['Aliquot'] = 0
        kwargs, child = batch._update_parameters(
            model='Specimen', parent=parent, order=1)
        self.assertDictEqual(kwargs, {'individual': parent, 'order': '1'})
        self.assertEqual(child, 'Aliquot')
        self.assertEqual(batch._last, True)

    def test_set_parameters_aliquot(self):
        batch = LeukformSamplesFactory()
        parent = 'specimenInstance'
        batch.request['Extraction'] = 0
        kwargs, child = batch._update_parameters(
            model='Aliquot', parent=parent)
        self.assertDictEqual(kwargs, {'specimen': parent})
        self.assertEqual(child, 'Extraction')
        self.assertEqual(batch._last, True)

    def test_set_parameters_extraction(self):
        batch = LeukformSamplesFactory()
        parent = 'aliquotInstance'
        batch.request['Workflow'] = 0
        kwargs, child = batch._update_parameters(
            model='Extraction', parent=parent)
        self.assertDictEqual(kwargs, {'aliquot': parent})
        self.assertEqual(child, 'Workflow')
        self.assertEqual(batch._last, True)

    def test_set_parameters_workflow(self):
        batch = LeukformSamplesFactory()
        parent = 'extractionInstance'
        kwargs, child = batch._update_parameters(
            model='Workflow', parent=parent)
        self.assertEqual(kwargs['extraction'], parent)
        self.assertEqual(batch._last, True)
        self.assertEqual(child, None)
        batch_projects = [p.pk for p in batch.projects]
        projects_string = kwargs['projects_string'].split('|')
        projects_string = [int(e) for e in projects_string]
        [self.assertIn(p, batch_projects) for p in projects_string]

    def test_write_row_delete_false_last_false_slug_true(self):
        batch = LeukformSamplesFactory()
        batch._last = False
        batch._delete = False
        batch._slug = True
        instance = AliquotFactory()
        batch._write_row(instance, model='Aliquot')
        self.assertDictEqual(batch._row, {'Aliquot.slug': instance.slug})

    def test_write_row_delete_false_last_false_slug_false(self):
        batch = LeukformSamplesFactory()
        batch._last = False
        batch._delete = False
        batch._slug = False
        instance = AliquotFactory()
        batch._write_row(instance, model='Aliquot')
        self.assertEqual(batch._row['Aliquot.ext_id'], instance.ext_id)

    def test_write_row_delete_true_last_false(self):
        batch = LeukformSamplesFactory()
        batch._last = False
        batch._delete = True
        batch._slug = False
        instance = AliquotFactory()
        row = {}
        notused = ["individual", "specimen", "aliquot", "extraction"]
        for field in CREATE_FIELDS['Aliquot']:
            if field in notused:
                continue
            column = "{0}.{1}".format('Aliquot', field)
            value = eval('instance.{0}'.format(field))
            row[column] = str(value)
        batch._write_row(instance, model='Aliquot')
        self.assertDictEqual(batch._row, row)

    def test_write_row_delete_true_last_true(self):
        batch = LeukformSamplesFactory()
        batch._last = True
        batch._delete = True
        batch._slug = False
        instance = AliquotFactory()
        row = {}
        rows = []
        notused = ["individual", "specimen", "aliquot", "extraction"]
        for field in CREATE_FIELDS['Aliquot']:
            if field in notused:
                continue
            column = "{0}.{1}".format('Aliquot', field)
            value = eval('instance.{0}'.format(field))
            row[column] = str(value)
        rows.append(row.copy())
        batch._write_row(instance, model='Aliquot')
        self.assertDictEqual(batch._row, row)
        self.assertCountEqual(batch.rows, rows)
        with self.assertRaises(AssertionError):
            instance.delete()

    def test_create_batch_create_instances(self):
        batch = LeukformSamplesFactory()

        # prefunction
        for model in MODELS_LIST:
            self.assertEqual(len(batch.instances[model]), 0)

        batch.create_batch()

        # check that the required number of instances were created
        for model in MODELS_LIST:
            self.assertEqual(len(batch.instances[model]), 1)

        # test extractions projects lists are being assigned correctly
        batch_projects = [p.pk for p in batch.projects]
        projects_string = \
            batch.rows[0]['Workflow.projects_string'].split("|")
        projects_string = [int(e) for e in projects_string]
        [self.assertIn(p, batch_projects) for p in projects_string]

    def test_csv_from_rows(self):
        self.maxDiff = None
        batch = LeukformSamplesFactory()
        batch.create_batch()
        path = batch.create_csv_from_rows()

        with open(path, 'r') as testcsv:
            rows = csv.DictReader(testcsv, delimiter=",")
            rows = list(rows)

        self.assertCountEqual(batch.rows, rows)
        os.remove(path)
