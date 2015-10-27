# -*- coding: utf-8 -*-

# django
from django.test import TestCase

# leukapp
from leukapp.apps.leukforms.utils import RunsFromCsv
from leukapp.apps.leukforms.factories import LeukformCsvFactory


class TestRunsFromCsv(TestCase):

    def setUp(self):
        self.models = ['Individual', 'Specimen', 'Aliquot', 'Run']
        self.loader = RunsFromCsv()
        self.batch = LeukformCsvFactory()

        self.batch.create_batch(1, 1, 1, 1)
        self.batch.create_rows()
        self.row = self.batch.rows[0]
        self.loader._fields_from_row(self.row)

        # batch instances
        self.created = {
            'Individual': self.batch.individuals[0],
            'Specimen': self.batch.specimens[0],
            'Aliquot': self.batch.aliquots[0],
            'Run': self.batch.runs[0],
            }

        self.row = self.batch.rows[0]
        self.loader._fields_from_row(self.row)

        individual, errors = self.loader._get_or_create(model='Individual')
        specimen, errors = self.loader._get_or_create(model='Specimen')
        aliquot, errors = self.loader._get_or_create(model='Aliquot')
        run, errors = self.loader._get_or_create(model='Run')

        # batch instances
        self.loaded = {
            'Individual': individual,
            'Specimen': specimen,
            'Aliquot': aliquot,
            'Run': run,
            }

    def test_fields_from_row_excluding_run(self):
        fields = self.loader._fields_from_row(self.row)
        for model in self.models:
            fields[model].pop('projects', None)
            fields[model].pop('individual', None)
            fields[model].pop('specimen', None)
            fields[model].pop('aliquot', None)
            for field in fields[model]:
                value = "self.created[model].{0}".format(field)
                self.assertEqual(fields[model][field], eval(value))

    def test_fields_for_run_projects(self):
        fields = self.loader._fields_from_row(self.row)
        projects = [p.pk for p in self.created['Run'].projects.all()]
        for p in fields['Run']['projects']:
            self.assertIn(p, projects)

    def test_get_or_create_using_existent_instance(self):
        for model in self.created:
            self.assertEqual(self.created[model], self.loaded[model])
            self.assertCountEqual(
                self.loader.existed[model], [self.loaded[model]])

    def test_get_or_create_using_nonexistent_instance(self):
        for model in self.models:
            self.loader.input[model] = {}
            instance, errors = self.loader._get_or_create(model)
            self.assertNotEqual(errors, None)

    def test_create_instance_form_valid(self):
        ext_ids = {}
        for model in self.models:
            ext_ids[model] = self.created[model].ext_id
            self.created[model].delete()

        for model in self.models:
            instance, errors = self.loader._get_or_create(model=model)
            added = [instance]
            self.assertCountEqual(self.loader.added[model], added)
            self.assertEqual(instance.ext_id, ext_ids[model])

    def test_process_row_invalid_individual(self):
        self.row['Individual.institution'] = ''
        self.row['Individual.species'] = ''
        self.row['Individual.ext_id'] = ''
        self.loader._fields_from_row(self.row)
        self.loader.save_runs_from_rows(self.batch.rows)
        self.assertEqual(self.loader.rejected["Individual"], 1)

    def test_process_row_invalid_specimen(self):
        self.row['Specimen.ext_id'] = ''
        self.loader._fields_from_row(self.row)
        self.loader.save_runs_from_rows(self.batch.rows)
        self.assertEqual(self.loader.rejected["Specimen"], 1)

    def test_process_row_invalid_aliquot(self):
        self.row['Aliquot.bio_source'] = ''
        self.row['Aliquot.ext_id'] = ''
        self.loader._fields_from_row(self.row)
        self.loader.save_runs_from_rows(self.batch.rows)
        self.assertEqual(self.loader.rejected["Aliquot"], 1)

    def test_process_row_invalid_run(self):
        self.batch.runs[0].delete()
        self.row['Run.projects'] = 'asa5|ss56'
        self.loader._fields_from_row(self.row)
        self.loader.save_runs_from_rows(self.batch.rows)
        self.assertEqual(self.loader.rejected["Run"], 1)

    def test_save_runs_from_rows(self):
        batch = LeukformCsvFactory()
        batch.create_batch(5, 3, 2, 1)
        batch.create_rows()
        loader = RunsFromCsv()
        for i in batch.individuals:
            i.delete()
        loader.save_runs_from_rows(batch.rows)
        added = len(loader.added["Run"])
        self.assertGreater(added, 5)
        self.assertLessEqual(added, 5 * 3 * 2 * 1)

    def test_added_existed_individuals(self):
        batch = LeukformCsvFactory()
        batch.create_batch(5, 3, 2, 1)
        batch.create_rows()
        loader = RunsFromCsv()
        for i in range(3):
            batch.individuals[i].delete()

        loader.save_runs_from_rows(batch.rows)
        self.assertEqual(len(loader.added['Individual']), 3)
        self.assertEqual(len(loader.existed['Individual']), 2)
