# -*- coding: utf-8 -*-

# python
import csv
import os

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
from ..utils import SamplesFactory


class SamplesCommandsTest(TestCase):

    def setUp(self):
        self.Command = submit_samples_from_csv.Command()

    def test_initialize_out_row(self):
        self.Command.initialize_out_row()

        for model in self.Command.models:
            if model == 'Project':
                self.assertEqual(
                    self.Command.ACTION_NOT_TESTED,
                    self.Command.out_row[model + '.pk'])
            else:
                self.assertEqual(
                    self.Command.ACTION_NOT_TESTED,
                    self.Command.out_row[model + '.ext_id'])
            self.assertEqual(
                self.Command.ACTION_NOT_TESTED,
                self.Command.out_row[model + '.action'])

            self.assertEqual(
                self.Command.ACTION_NOT_TESTED,
                self.Command.out_row[model + '.errors'])

    def test_get_fields_from_row(self):
        batch = SamplesFactory()
        batch.create_batch(1, 1, 1)
        batch.create_rows()
        row = batch.rows[0]
        individual = batch.individuals[0]
        specimen = batch.specimens[0]
        aliquot = batch.aliquots[0]
        fields = self.Command.get_fields_from_row(row)
        self.assertEqual(
            fields['Individual']['institution'], individual.institution)
        self.assertEqual(
            fields['Individual']['species'], individual.species)
        self.assertEqual(
            fields['Individual']['ext_id'], individual.ext_id)
        self.assertEqual(
            fields['Specimen']['ext_id'], specimen.ext_id)
        self.assertEqual(
            fields['Specimen']['source'], specimen.source)
        self.assertEqual(
            fields['Aliquot']['ext_id'], aliquot.ext_id)
        self.assertEqual(
            fields['Aliquot']['bio_source'], aliquot.bio_source)
        self.assertNotEqual(
            fields['Project']['pk'], None)

    def test_get_instance_using_existent_instance(self):
        batch = SamplesFactory()
        batch.create_batch(1, 1, 1)
        batch.create_rows()
        row = batch.rows[0]

        # batch instances
        b = {
            'Individual': batch.individuals[0],
            'Specimen': batch.specimens[0],
            'Aliquot': batch.aliquots[0],
            }

        self.Command.get_fields_from_row(row)
        individual = self.Command.get_instance(model='Individual')
        specimen = self.Command.get_instance(model='Specimen')
        aliquot = self.Command.get_instance(model='Aliquot')

        self.assertEqual(b['Individual'], individual)
        self.assertEqual(b['Specimen'], specimen)
        self.assertEqual(b['Aliquot'], aliquot)

        # test existing is updated
        self.assertCountEqual(
            self.Command.existing['Individual'], [individual])
        self.assertCountEqual(
            self.Command.existing['Specimen'], [specimen])
        self.assertCountEqual(
            self.Command.existing['Aliquot'], [aliquot])

        # test out_row is updated
        for model in self.Command.models:
            if model == 'Project':
                continue
            self.assertEqual(
                b[model].ext_id,
                self.Command.out_row[model + '.ext_id'])

            self.assertEqual(
                self.Command.ACTION_EXISTING,
                self.Command.out_row[model + '.action'])

            self.assertEqual(
                self.Command.ACTION_NO_ERRORS,
                self.Command.out_row[model + '.errors'])

    def test_get_instance_using_nonexistent_instance(self):
        for model in self.Command.models:
            if model == 'Project':
                continue
            DoesNotExist = self.Command.models[model].DoesNotExist
            with self.assertRaises(DoesNotExist):
                self.Command.get_instance(model=model, fields={})

    def test_create_instance_form_valid(self):
        batch = SamplesFactory()
        batch.create_batch(1, 1, 1)
        batch.create_rows()
        row = batch.rows[0]

        self.Command.get_fields_from_row(row)

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
        individual, errors = self.Command.create_instance(model='Individual')
        specimen, errors = self.Command.create_instance(model='Specimen')
        aliquot, errors = self.Command.create_instance(model='Aliquot')

        self.assertEqual(b['Individual'], individual.ext_id)
        self.assertEqual(b['Specimen'], specimen.ext_id)
        self.assertEqual(b['Aliquot'], aliquot.ext_id)

        # test added is updated
        self.assertCountEqual(self.Command.added['Individual'], [individual])
        self.assertCountEqual(self.Command.added['Specimen'], [specimen])
        self.assertCountEqual(self.Command.added['Aliquot'], [aliquot])

        # test out_row is updated
        for model in self.Command.models:
            if model == 'Project':
                continue
            self.assertEqual(
                b[model],
                self.Command.out_row[model + '.ext_id'])

            self.assertEqual(
                self.Command.ACTION_ADDED,
                self.Command.out_row[model + '.action'])

            self.assertEqual(
                self.Command.ACTION_NO_ERRORS,
                self.Command.out_row[model + '.errors'])

    def test_create_instance_form_invalid(self):
        for model in self.Command.models:
            if model == 'Project':
                continue
            instance, errors = self.Command.create_instance(
                model=model, fields={'ext_id': '1'})
            self.assertEqual(
                '1',
                self.Command.out_row[model + '.ext_id'])

            self.assertEqual(
                self.Command.ACTION_ERROR,
                self.Command.out_row[model + '.action'])

            self.assertEqual(
                str(errors),
                self.Command.out_row[model + '.errors'])

    def test_update_models_fields_for_specimen(self):
        batch = SamplesFactory()
        batch.create_batch(1, 1, 1)
        batch.create_rows()
        row = batch.rows[0]

        self.Command.get_fields_from_row(row)

        individual = self.Command.get_instance(model='Individual')
        self.assertEqual(
            self.Command.models_fields['Specimen']['individual'],
            individual.pk)

    def test_update_models_fields_for_aliquot(self):
        batch = SamplesFactory()
        batch.create_batch(1, 1, 1)
        batch.create_rows()
        row = batch.rows[0]

        self.Command.get_fields_from_row(row)

        specimen = self.Command.get_instance(model='Specimen')
        self.assertEqual(
            self.Command.models_fields['Aliquot']['specimen'],
            specimen.pk)

    def test_get_or_create_instance_existent_instance(self):
        batch = SamplesFactory()
        batch.create_batch(1, 1, 1)
        batch.create_rows()
        row = batch.rows[0]

        self.Command.get_fields_from_row(row)
        specimen = self.Command.get_or_create_instance(model='Specimen')

        self.assertEqual(specimen, batch.specimens[0])

    def test_get_or_create_instance_nonexistent_instance(self):
        specimen = self.Command.get_or_create_instance(model='Specimen')
        self.assertEqual(specimen, None)

    def test_process_row_existing_instances(self):
        batch = SamplesFactory()
        batch.create_batch(1, 1, 1)
        batch.create_rows()
        row = batch.rows[0]

        self.Command.process_row(row)

        # save batch ext_id
        b = {
            'Individual': batch.individuals[0].ext_id,
            'Specimen': batch.specimens[0].ext_id,
            'Aliquot': batch.aliquots[0].ext_id,
            }

        # test out_row is updated
        for model in self.Command.models:
            if model == 'Project':
                continue
            self.assertEqual(
                b[model],
                self.Command.out_row[model + '.ext_id'])

            self.assertEqual(
                self.Command.ACTION_EXISTING,
                self.Command.out_row[model + '.action'])

            self.assertEqual(
                self.Command.ACTION_NO_ERRORS,
                self.Command.out_row[model + '.errors'])

    def test_process_row_empty_row_dict(self):

        self.Command.process_row({})

        # test out_row is updated
        for model in self.Command.models:
            if model == 'Project':
                continue
            self.assertEqual(
                self.Command.ACTION_NOT_TESTED,
                self.Command.out_row[model + '.ext_id'])

            self.assertEqual(
                self.Command.ACTION_NOT_TESTED,
                self.Command.out_row[model + '.action'])

            self.assertEqual(
                self.Command.ACTION_NOT_TESTED,
                self.Command.out_row[model + '.errors'])

    def test_process_row_empty_row(self):

        self.Command.process_row({})

        # test out_row is updated
        for model in self.Command.models:
            if model == 'Project':
                continue
            self.assertEqual(
                self.Command.ACTION_NOT_TESTED,
                self.Command.out_row[model + '.ext_id'])

            self.assertEqual(
                self.Command.ACTION_NOT_TESTED,
                self.Command.out_row[model + '.action'])

            self.assertEqual(
                self.Command.ACTION_NOT_TESTED,
                self.Command.out_row[model + '.errors'])

    def test_process_row_invalid_individual(self):

        batch = SamplesFactory()
        batch.create_batch(1, 1, 1)
        batch.create_rows()
        row = batch.rows[0]

        row['Individual.institution'] = ''
        row['Individual.species'] = ''
        row['Individual.ext_id'] = ''

        self.Command.process_row(row)

        # test out_row is updated
        for model in self.Command.models:
            if model == 'Project':
                continue
            if model == 'Individual':

                self.assertEqual(
                    '',
                    self.Command.out_row[model + '.ext_id'])

                self.assertEqual(
                    self.Command.ACTION_ERROR,
                    self.Command.out_row[model + '.action'])
                continue

            self.assertEqual(
                self.Command.ACTION_NOT_TESTED,
                self.Command.out_row[model + '.ext_id'])

            self.assertEqual(
                self.Command.ACTION_NOT_TESTED,
                self.Command.out_row[model + '.action'])

            self.assertEqual(
                self.Command.ACTION_NOT_TESTED,
                self.Command.out_row[model + '.errors'])

    def test_process_row_invalid_specimen(self):

        batch = SamplesFactory()
        batch.create_batch(1, 1, 1)
        batch.create_rows()
        row = batch.rows[0]

        row['Specimen.source'] = ''
        row['Specimen.ext_id'] = ''

        self.Command.process_row(row)

        # test out_row is updated
        self.assertEqual(
            self.Command.ACTION_EXISTING,
            self.Command.out_row['Individual' + '.action'])
        self.assertEqual(
            self.Command.ACTION_NO_ERRORS,
            self.Command.out_row['Individual' + '.errors'])

        self.assertEqual(
            '',
            self.Command.out_row['Specimen' + '.ext_id'])
        self.assertEqual(
            self.Command.ACTION_ERROR,
            self.Command.out_row['Specimen' + '.action'])

        self.assertEqual(
            self.Command.ACTION_NOT_TESTED,
            self.Command.out_row['Aliquot' + '.ext_id'])
        self.assertEqual(
            self.Command.ACTION_NOT_TESTED,
            self.Command.out_row['Aliquot' + '.action'])
        self.assertEqual(
            self.Command.ACTION_NOT_TESTED,
            self.Command.out_row['Aliquot' + '.errors'])

    def test_process_row_invalid_aliquot(self):

        batch = SamplesFactory()
        batch.create_batch(1, 1, 1)
        batch.create_rows()
        row = batch.rows[0]

        row['Aliquot.bio_source'] = ''
        row['Aliquot.ext_id'] = ''

        self.Command.process_row(row)

        # test out_row is updated
        self.assertEqual(
            self.Command.ACTION_EXISTING,
            self.Command.out_row['Individual' + '.action'])
        self.assertEqual(
            self.Command.ACTION_NO_ERRORS,
            self.Command.out_row['Individual' + '.errors'])

        self.assertEqual(
            self.Command.ACTION_EXISTING,
            self.Command.out_row['Specimen' + '.action'])
        self.assertEqual(
            self.Command.ACTION_NO_ERRORS,
            self.Command.out_row['Specimen' + '.errors'])

        self.assertEqual(
            '',
            self.Command.out_row['Aliquot' + '.ext_id'])
        self.assertEqual(
            self.Command.ACTION_ERROR,
            self.Command.out_row['Aliquot' + '.action'])

    def test_save_samples_from_rows(self):
        batch = SamplesFactory()
        batch.create_batch(10, 2, 2)
        batch.create_rows()
        self.Command.save_samples_from_rows(batch.rows)
        out_rows_number = len(self.Command.out_rows)
        self.assertGreater(out_rows_number, 5)
        self.assertLessEqual(out_rows_number, 10 * 2 * 2)

    def test_added_existing_individuals(self):
        batch = SamplesFactory()
        batch.create_batch(20, 2, 2)
        batch.create_rows()

        for i in range(10):
            batch.individuals[i].delete()
        self.Command.save_samples_from_rows(batch.rows)

        self.assertEqual(
            len(self.Command.existing['Individual']),
            len(batch.individuals) - 10)
        self.assertEqual(
            len(self.Command.added['Individual']), 10)

    def test_added_existing_specimens(self):
        batch = SamplesFactory()
        batch.create_batch(20, 2, 2)
        batch.create_rows()

        for i in range(10):
            batch.specimens[i].delete()
        self.Command.save_samples_from_rows(batch.rows)

        self.assertEqual(
            len(self.Command.existing['Specimen']),
            len(batch.specimens) - 10)
        self.assertEqual(
            len(self.Command.added['Specimen']), 10)

    def test_added_existing_aliquots(self):
        batch = SamplesFactory()
        batch.create_batch(20, 2, 2)
        batch.create_rows()

        for i in range(10):
            batch.aliquots[i].delete()
        self.Command.save_samples_from_rows(batch.rows)

        self.assertEqual(
            len(self.Command.existing['Aliquot']),
            len(batch.aliquots) - 10)
        self.assertEqual(
            len(self.Command.added['Aliquot']), 10)

    def test_save_out_rows_in_csv(self):
        batch = SamplesFactory()
        batch.create_batch(2, 1, 1)
        batch.create_rows()

        self.Command.save_samples_from_rows(batch.rows)
        path = self.Command.save_out_rows_in_csv()

        with open(path, 'r') as testcsv:
            rows = csv.DictReader(testcsv, delimiter=",")
            rows = list(rows)

        self.assertCountEqual(self.Command.out_rows, rows)
        # os.remove(path)

    def test_rejected_invalid_individual(self):

        batch = SamplesFactory()
        batch.create_batch(1, 1, 1)
        batch.create_rows()
        batch.rows[0]['Individual.institution'] = ''
        batch.rows[0]['Individual.species'] = ''
        batch.rows[0]['Individual.ext_id'] = ''
        self.Command.save_samples_from_rows(batch.rows)
        self.assertEqual(
            len(self.Command.rejected['Individual']), 1)

    def test_rejected_invalid_specimen(self):

        batch = SamplesFactory()
        batch.create_batch(1, 1, 1)
        batch.create_rows()
        batch.rows[0]['Specimen.source'] = ''
        batch.rows[0]['Specimen.ext_id'] = ''
        self.Command.save_samples_from_rows(batch.rows)
        self.assertEqual(
            len(self.Command.rejected['Specimen']), 1)

    def test_rejected_invalid_aliquot(self):

        batch = SamplesFactory()
        batch.create_batch(1, 1, 1)
        batch.create_rows()
        batch.rows[0]['Aliquot.bio_source'] = ''
        batch.rows[0]['Aliquot.ext_id'] = ''
        self.Command.save_samples_from_rows(batch.rows)
        self.assertEqual(
            len(self.Command.rejected['Aliquot']), 1)
