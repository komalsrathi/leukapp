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


class SamplesFromCsvTest(TestCase):

    def setUp(self):
        self.loader = SamplesCSV()

    def test_initialize_out_row(self):
        loader = SamplesCSV()
        loader.initialize_out_row()
        for model in loader.models:
            for key in loader.out_row:
                self.assertEqual(loader.out_row[key], loader.ACTION_NOT_TESTED)

    def test_get_fields_from_row(self):
        batch = LeukformFactory()
        batch.create_batch(1, 1, 1, 1)
        row = batch.create_rows()[0]
        fields = self.loader.get_fields_from_row(row)

        out = {
            'Individual':
            'Aliquot':
            'Project'
        }
        individual = batch.individuals[0]
        specimen = batch.specimens[0]
        aliquot = batch.aliquots[0]

        for model in fields:
            for field in fields[model]:
                self.assertEqual(field, eval())
        self.assertEqual(fields['Individual'], individual)
        self.assertEqual(fields['Specimen'], specimen)
        self.assertEqual(fields['Aliquot'], aliquot)
        self.assertNotEqual(fields['Project']['pk'], None)

    def test_get_instance_using_existent_instance(self):
        batch = LeukformFactory()
        batch.create_batch(1, 1, 1)
        batch.create_rows()
        row = batch.rows[0]

        # batch instances
        b = {
            'Individual': batch.individuals[0],
            'Specimen': batch.specimens[0],
            'Aliquot': batch.aliquots[0],
            }

        self.loader.get_fields_from_row(row)
        individual = self.loader.get_instance(model='Individual')
        specimen = self.loader.get_instance(model='Specimen')
        aliquot = self.loader.get_instance(model='Aliquot')

        self.assertEqual(b['Individual'], individual)
        self.assertEqual(b['Specimen'], specimen)
        self.assertEqual(b['Aliquot'], aliquot)

        # test existing is updated
        self.assertCountEqual(
            self.loader.existing['Individual'], [individual])
        self.assertCountEqual(
            self.loader.existing['Specimen'], [specimen])
        self.assertCountEqual(
            self.loader.existing['Aliquot'], [aliquot])

        # test out_row is updated
        for model in self.loader.models:
            if model == 'Project':
                continue
            self.assertEqual(
                b[model].ext_id,
                self.loader.out_row[model + '.ext_id'])

            self.assertEqual(
                self.loader.ACTION_EXISTING,
                self.loader.out_row[model + '.action'])

            self.assertEqual(
                self.loader.ACTION_NO_ERRORS,
                self.loader.out_row[model + '.errors'])

    def test_get_instance_using_nonexistent_instance(self):
        for model in self.loader.models:
            if model == 'Project':
                continue
            DoesNotExist = self.loader.models[model].DoesNotExist
            with self.assertRaises(DoesNotExist):
                self.loader.get_instance(model=model, fields={})

    def test_create_instance_form_valid(self):
        batch = LeukformFactory()
        batch.create_batch(1, 1, 1)
        batch.create_rows()
        row = batch.rows[0]

        self.loader.get_fields_from_row(row)

        # save batch ext_id
        b = {
            'Individual': batch.individuals[0].ext_id,
            'Specimen': batch.specimens[0].ext_id,
            'Aliquot': batch.aliquots[0].ext_id,
            }

        # delete batch instances
        batch.individuals[0].delete()
        batch.specimens[0].delete()
        batch.aliquots[0].delete()

        # create
        individual, errors = self.loader.create_instance(model='Individual')
        specimen, errors = self.loader.create_instance(model='Specimen')
        aliquot, errors = self.loader.create_instance(model='Aliquot')

        self.assertEqual(b['Individual'], individual.ext_id)
        self.assertEqual(b['Specimen'], specimen.ext_id)
        self.assertEqual(b['Aliquot'], aliquot.ext_id)

        # test added is updated
        self.assertCountEqual(self.loader.added['Individual'], [individual])
        self.assertCountEqual(self.loader.added['Specimen'], [specimen])
        self.assertCountEqual(self.loader.added['Aliquot'], [aliquot])

        # test out_row is updated
        for model in self.loader.models:
            if model == 'Project':
                continue
            self.assertEqual(
                b[model],
                self.loader.out_row[model + '.ext_id'])

            self.assertEqual(
                self.loader.ACTION_ADDED,
                self.loader.out_row[model + '.action'])

            self.assertEqual(
                self.loader.ACTION_NO_ERRORS,
                self.loader.out_row[model + '.errors'])

    def test_create_instance_form_invalid(self):
        for model in self.loader.models:
            if model == 'Project':
                continue
            instance, errors = self.loader.create_instance(
                model=model, fields={'ext_id': '1'})
            self.assertEqual(
                '1',
                self.loader.out_row[model + '.ext_id'])

            self.assertEqual(
                self.loader.ACTION_ERROR,
                self.loader.out_row[model + '.action'])

            self.assertEqual(
                str(errors),
                self.loader.out_row[model + '.errors'])

    def test_update_models_fields_for_specimen(self):
        batch = LeukformFactory()
        batch.create_batch(1, 1, 1)
        batch.create_rows()
        row = batch.rows[0]

        self.loader.get_fields_from_row(row)

        individual = self.loader.get_instance(model='Individual')
        self.assertEqual(
            self.loader.models_fields['Specimen']['individual'],
            individual.pk)

    def test_update_models_fields_for_aliquot(self):
        batch = LeukformFactory()
        batch.create_batch(1, 1, 1)
        batch.create_rows()
        row = batch.rows[0]

        self.loader.get_fields_from_row(row)

        specimen = self.loader.get_instance(model='Specimen')
        self.assertEqual(
            self.loader.models_fields['Aliquot']['specimen'],
            specimen.pk)

    def test_get_or_create_instance_existent_instance(self):
        batch = LeukformFactory()
        batch.create_batch(1, 1, 1)
        batch.create_rows()
        row = batch.rows[0]

        self.loader.get_fields_from_row(row)
        specimen = self.loader.get_or_create_instance(model='Specimen')

        self.assertEqual(specimen, batch.specimens[0])

    def test_get_or_create_instance_nonexistent_instance(self):
        specimen = self.loader.get_or_create_instance(model='Specimen')
        self.assertEqual(specimen, None)

    def test_process_row_existing_instances(self):
        batch = LeukformFactory()
        batch.create_batch(1, 1, 1)
        batch.create_rows()
        row = batch.rows[0]

        self.loader.process_row(row)

        # save batch ext_id
        b = {
            'Individual': batch.individuals[0].ext_id,
            'Specimen': batch.specimens[0].ext_id,
            'Aliquot': batch.aliquots[0].ext_id,
            }

        # test out_row is updated
        for model in self.loader.models:
            if model == 'Project':
                continue
            self.assertEqual(
                b[model],
                self.loader.out_row[model + '.ext_id'])

            self.assertEqual(
                self.loader.ACTION_EXISTING,
                self.loader.out_row[model + '.action'])

            self.assertEqual(
                self.loader.ACTION_NO_ERRORS,
                self.loader.out_row[model + '.errors'])

    def test_process_row_empty_row_dict(self):

        self.loader.process_row({})

        # test out_row is updated
        for model in self.loader.models:
            if model == 'Project':
                continue
            self.assertEqual(
                self.loader.ACTION_NOT_TESTED,
                self.loader.out_row[model + '.ext_id'])

            self.assertEqual(
                self.loader.ACTION_NOT_TESTED,
                self.loader.out_row[model + '.action'])

            self.assertEqual(
                self.loader.ACTION_NOT_TESTED,
                self.loader.out_row[model + '.errors'])

    def test_process_row_empty_row(self):

        self.loader.process_row({})

        # test out_row is updated
        for model in self.loader.models:
            if model == 'Project':
                continue
            self.assertEqual(
                self.loader.ACTION_NOT_TESTED,
                self.loader.out_row[model + '.ext_id'])

            self.assertEqual(
                self.loader.ACTION_NOT_TESTED,
                self.loader.out_row[model + '.action'])

            self.assertEqual(
                self.loader.ACTION_NOT_TESTED,
                self.loader.out_row[model + '.errors'])

    def test_process_row_invalid_individual(self):

        batch = LeukformFactory()
        batch.create_batch(1, 1, 1)
        batch.create_rows()
        row = batch.rows[0]

        row['Individual.institution'] = ''
        row['Individual.species'] = ''
        row['Individual.ext_id'] = ''

        self.loader.process_row(row)

        # test out_row is updated
        for model in self.loader.models:
            if model == 'Project':
                continue
            if model == 'Individual':

                self.assertEqual(
                    '',
                    self.loader.out_row[model + '.ext_id'])

                self.assertEqual(
                    self.loader.ACTION_ERROR,
                    self.loader.out_row[model + '.action'])
                continue

            self.assertEqual(
                self.loader.ACTION_NOT_TESTED,
                self.loader.out_row[model + '.ext_id'])

            self.assertEqual(
                self.loader.ACTION_NOT_TESTED,
                self.loader.out_row[model + '.action'])

            self.assertEqual(
                self.loader.ACTION_NOT_TESTED,
                self.loader.out_row[model + '.errors'])

    def test_process_row_invalid_specimen(self):

        batch = LeukformFactory()
        batch.create_batch(1, 1, 1)
        batch.create_rows()
        row = batch.rows[0]

        row['Specimen.source'] = ''
        row['Specimen.ext_id'] = ''

        self.loader.process_row(row)

        # test out_row is updated
        self.assertEqual(
            self.loader.ACTION_EXISTING,
            self.loader.out_row['Individual' + '.action'])
        self.assertEqual(
            self.loader.ACTION_NO_ERRORS,
            self.loader.out_row['Individual' + '.errors'])

        self.assertEqual(
            '',
            self.loader.out_row['Specimen' + '.ext_id'])
        self.assertEqual(
            self.loader.ACTION_ERROR,
            self.loader.out_row['Specimen' + '.action'])

        self.assertEqual(
            self.loader.ACTION_NOT_TESTED,
            self.loader.out_row['Aliquot' + '.ext_id'])
        self.assertEqual(
            self.loader.ACTION_NOT_TESTED,
            self.loader.out_row['Aliquot' + '.action'])
        self.assertEqual(
            self.loader.ACTION_NOT_TESTED,
            self.loader.out_row['Aliquot' + '.errors'])

    def test_process_row_invalid_aliquot(self):

        batch = LeukformFactory()
        batch.create_batch(1, 1, 1)
        batch.create_rows()
        row = batch.rows[0]

        row['Aliquot.bio_source'] = ''
        row['Aliquot.ext_id'] = ''

        self.loader.process_row(row)

        # test out_row is updated
        self.assertEqual(
            self.loader.ACTION_EXISTING,
            self.loader.out_row['Individual' + '.action'])
        self.assertEqual(
            self.loader.ACTION_NO_ERRORS,
            self.loader.out_row['Individual' + '.errors'])

        self.assertEqual(
            self.loader.ACTION_EXISTING,
            self.loader.out_row['Specimen' + '.action'])
        self.assertEqual(
            self.loader.ACTION_NO_ERRORS,
            self.loader.out_row['Specimen' + '.errors'])

        self.assertEqual(
            '',
            self.loader.out_row['Aliquot' + '.ext_id'])
        self.assertEqual(
            self.loader.ACTION_ERROR,
            self.loader.out_row['Aliquot' + '.action'])

    def test_save_samples_from_rows(self):
        batch = LeukformFactory()
        batch.create_batch(10, 2, 2)
        batch.create_rows()
        self.loader.save_samples_from_rows(batch.rows)
        out_rows_number = len(self.loader.out_rows)
        self.assertGreater(out_rows_number, 5)
        self.assertLessEqual(out_rows_number, 10 * 2 * 2)

    def test_added_existing_individuals(self):
        batch = LeukformFactory()
        batch.create_batch(20, 2, 2)
        batch.create_rows()

        for i in range(10):
            batch.individuals[i].delete()
        self.loader.save_samples_from_rows(batch.rows)

        self.assertEqual(
            len(self.loader.existing['Individual']),
            len(batch.individuals) - 10)
        self.assertEqual(
            len(self.loader.added['Individual']), 10)

    def test_added_existing_specimens(self):
        batch = LeukformFactory()
        batch.create_batch(20, 2, 2)
        batch.create_rows()

        for i in range(10):
            batch.specimens[i].delete()
        self.loader.save_samples_from_rows(batch.rows)

        self.assertEqual(
            len(self.loader.existing['Specimen']),
            len(batch.specimens) - 10)
        self.assertEqual(
            len(self.loader.added['Specimen']), 10)

    def test_added_existing_aliquots(self):
        batch = LeukformFactory()
        batch.create_batch(20, 2, 2)
        batch.create_rows()

        for i in range(10):
            batch.aliquots[i].delete()
        self.loader.save_samples_from_rows(batch.rows)

        self.assertEqual(
            len(self.loader.existing['Aliquot']),
            len(batch.aliquots) - 10)
        self.assertEqual(
            len(self.loader.added['Aliquot']), 10)

    def test_save_out_rows_in_csv(self):
        batch = LeukformFactory()
        batch.create_batch(2, 1, 1)
        batch.create_rows()

        self.loader.save_samples_from_rows(batch.rows)
        path = self.loader.save_out_rows_in_csv()

        with open(path, 'r') as testcsv:
            rows = csv.DictReader(testcsv, delimiter=",")
            rows = list(rows)

        self.assertCountEqual(self.loader.out_rows, rows)
        # os.remove(path)

    def test_rejected_invalid_individual(self):

        batch = LeukformFactory()
        batch.create_batch(1, 1, 1)
        batch.create_rows()
        batch.rows[0]['Individual.institution'] = ''
        batch.rows[0]['Individual.species'] = ''
        batch.rows[0]['Individual.ext_id'] = ''
        self.loader.save_samples_from_rows(batch.rows)
        self.assertEqual(
            len(self.loader.rejected['Individual']), 1)

    def test_rejected_invalid_specimen(self):

        batch = LeukformFactory()
        batch.create_batch(1, 1, 1)
        batch.create_rows()
        batch.rows[0]['Specimen.source'] = ''
        batch.rows[0]['Specimen.ext_id'] = ''
        self.loader.save_samples_from_rows(batch.rows)
        self.assertEqual(
            len(self.loader.rejected['Specimen']), 1)

    def test_rejected_invalid_aliquot(self):

        batch = LeukformFactory()
        batch.create_batch(1, 1, 1)
        batch.create_rows()
        batch.rows[0]['Aliquot.bio_source'] = ''
        batch.rows[0]['Aliquot.ext_id'] = ''
        self.loader.save_samples_from_rows(batch.rows)
        self.assertEqual(
            len(self.loader.rejected['Aliquot']), 1)
