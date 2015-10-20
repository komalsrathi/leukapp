# -*- coding: utf-8 -*-

# python
import csv
import os

# django imports
from django.test import TestCase

# local imports
from ..utils import LeukformFactory, SamplesCSV


class LeukformFactoryTest(TestCase):

    def test_leukform_factory_create_batch(self):
        batch = LeukformFactory()
        batch.create_batch(10, 2, 2, 1)
        self.assertEqual(len(batch.individuals), 10)
        self.assertNotEqual(batch.individuals[0].slug, None)
        self.assertNotEqual(batch.specimens[0].slug, None)
        self.assertNotEqual(batch.aliquots[0].slug, None)
        self.assertNotEqual(batch.samples[0].slug, None)

    def test_leukform_factory_create_rows(self):
        batch = LeukformFactory()
        batch.create_batch(10, 2, 2, 1)
        batch.create_rows()
        self.assertGreater(len(batch.rows), 5)
        self.assertLessEqual(len(batch.rows), 10 * 2 * 2)

    def test_csv_from_rows(self):
        batch = LeukformFactory()
        batch.create_batch(1, 1, 1, 1)
        batch.create_rows()
        path = batch.create_csv_from_rows()

        with open(path, 'r') as testcsv:
            rows = csv.DictReader(testcsv, delimiter=",")
            rows = list(rows)

        self.assertCountEqual(batch.rows, rows)
        os.remove(path)


class TestSamplesCSV(TestCase):

    def setUp(self):
        self.models = ['Individual', 'Specimen', 'Aliquot', 'Sample']
        self.loader = SamplesCSV()
        self.batch = LeukformFactory()

        self.batch.create_batch(1, 1, 1, 1)
        self.batch.create_rows()
        self.row = self.batch.rows[0]
        self.loader.fields_from_row(self.row)

        # batch instances
        self.created = {
            'Individual': self.batch.individuals[0],
            'Specimen': self.batch.specimens[0],
            'Aliquot': self.batch.aliquots[0],
            'Sample': self.batch.samples[0],
            }

        self.row = self.batch.rows[0]
        self.loader.fields_from_row(self.row)

        individual, errors = self.loader.get_or_create(model='Individual')
        specimen, errors = self.loader.get_or_create(model='Specimen')
        aliquot, errors = self.loader.get_or_create(model='Aliquot')
        sample, errors = self.loader.get_or_create(model='Sample')

        # batch instances
        self.loaded = {
            'Individual': individual,
            'Specimen': specimen,
            'Aliquot': aliquot,
            'Sample': sample,
            }

    def test_fields_from_row_excluding_sample(self):
        fields = self.loader.fields_from_row(self.row)
        for model in self.models:
            fields[model].pop('projects', None)
            fields[model].pop('individual', None)
            fields[model].pop('specimen', None)
            fields[model].pop('aliquot', None)
            for field in fields[model]:
                value = "self.created[model].{0}".format(field)
                self.assertEqual(fields[model][field], eval(value))

    def test_fields_for_sample_projects(self):
        fields = self.loader.fields_from_row(self.row)
        projects = [p.pk for p in self.created['Sample'].projects.all()]
        for p in fields['Sample']['projects']:
            self.assertIn(p, projects)

    def test_get_or_create_using_existent_instance(self):
        for model in self.created:
            self.assertEqual(self.created[model], self.loaded[model])
            self.assertCountEqual(
                self.loader.existing[model], [self.loaded[model]])

    def test_get_or_create_using_nonexistent_instance(self):
        for model in self.models:
            self.loader.input[model] = {}
            instance, errors = self.loader.get_or_create(model)
            self.assertNotEqual(errors, None)

    def test_create_instance_form_valid(self):
        ext_ids = {}
        for model in self.models:
            ext_ids[model] = self.created[model].ext_id
            self.created[model].delete()

        for model in self.models:
            instance, errors = self.loader.get_or_create(model=model)
            added = [instance]
            self.assertCountEqual(self.loader.added[model], added)
            self.assertEqual(instance.ext_id, ext_ids[model])

    def test_process_row_invalid_individual(self):
        self.row['Individual.institution'] = ''
        self.row['Individual.species'] = ''
        self.row['Individual.ext_id'] = ''
        self.loader.fields_from_row(self.row)
        self.loader.save_samples_from_rows(self.batch.rows)
        self.assertEqual(len(self.loader.rejected), 1)

    def test_process_row_invalid_specimen(self):
        self.row['Specimen.source'] = ''
        self.row['Specimen.ext_id'] = ''
        self.loader.fields_from_row(self.row)
        self.loader.save_samples_from_rows(self.batch.rows)
        self.assertEqual(len(self.loader.rejected), 1)

    def test_process_row_invalid_aliquot(self):
        self.row['Aliquot.bio_source'] = ''
        self.row['Aliquot.ext_id'] = ''
        self.loader.fields_from_row(self.row)
        self.loader.save_samples_from_rows(self.batch.rows)
        self.assertEqual(len(self.loader.rejected), 1)

    def test_process_row_invalid_sample(self):
        self.batch.samples[0].delete()
        self.row['Sample.projects'] = 'asa5|ss56'
        self.loader.fields_from_row(self.row)
        self.loader.save_samples_from_rows(self.batch.rows)
        self.assertEqual(len(self.loader.rejected), 1)

    def test_save_samples_from_rows(self):
        batch = LeukformFactory()
        batch.create_batch(5, 3, 2, 1)
        batch.create_rows()
        loader = SamplesCSV()
        loader.save_samples_from_rows(batch.rows)
        accepted = len(loader.accepted)
        self.assertGreater(accepted, 5)
        self.assertLessEqual(accepted, 5 * 3 * 2 * 1)

    def test_added_existing_individuals(self):
        batch = LeukformFactory()
        batch.create_batch(5, 3, 2, 1)
        batch.create_rows()
        loader = SamplesCSV()
        for i in range(3):
            batch.individuals[i].delete()

        loader.save_samples_from_rows(batch.rows)
        self.assertEqual(len(loader.added['Individual']), 3)
        self.assertEqual(len(loader.existing['Individual']), 2)

    # def test_save_out_rows_in_csv(self):
    #     batch = LeukformFactory()
    #     batch.create_batch(2, 1, 1)
    #     batch.create_rows()

    #     self.loader.save_samples_from_rows(batch.rows)
    #     path = self.loader.save_out_rows_in_csv()

    #     with open(path, 'r') as testcsv:
    #         rows = csv.DictReader(testcsv, delimiter=",")
    #         rows = list(rows)

    #     self.assertCountEqual(self.loader.out_rows, rows)
    #     # os.remove(path)
