# -*- coding: utf-8 -*-

# django
from django.test import TestCase

# leukapp
from leukapp.apps.leukforms.utils import LeukformLoader
from leukapp.apps.leukforms.factories import LeukformCsvFactory


class TestLeukformLoader(TestCase):

    models = ['Individual', 'Specimen', 'Aliquot', 'Run']
    loader = LeukformLoader()
    batch = LeukformCsvFactory()
    batch.create_batch(1, 1, 1, 1)
    batch.get_rows()
    rowexample = batch.rows[0]

    # example of created instances
    created = {
        'Individual': batch.individuals[0],
        'Specimen': batch.specimens[0],
        'Aliquot': batch.aliquots[0],
        'Run': batch.runs[0],
        }

    # example of loaded instances
    loaded = {
        'Individual': loader._get_or_create(model='Individual')[0],
        'Specimen': loader._get_or_create(model='Specimen')[0],
        'Aliquot': loader._get_or_create(model='Aliquot')[0],
        'Run': loader._get_or_create(model='Run')[0],
        }

    def setUp(self):
        pass

    def test_clean_row_excluding_run(self):
        fields = self.loader._clean_row(self.rowexample)
        for model in self.models:
            fields[model].pop('projects', None)
            fields[model].pop('individual', None)
            fields[model].pop('specimen', None)
            fields[model].pop('aliquot', None)
            for field in fields[model]:
                value = "self.created[model].{0}".format(field)
                self.assertEqual(fields[model][field], eval(value))

    def test_fields_for_run_projects(self):
        fields = self.loader._clean_row(self.rowexample)
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
        self.rowexample['Individual.institution'] = ''
        self.rowexample['Individual.species'] = ''
        self.rowexample['Individual.ext_id'] = ''
        self.loader._clean_row(self.rowexample)
        self.loader.process_leukform(self.batch.rows)
        self.assertEqual(self.loader.rejected["Individual"], 1)

    def test_process_row_invalid_specimen(self):
        self.rowexample['Specimen.ext_id'] = ''
        self.loader._clean_row(self.rowexample)
        self.loader.process_leukform(self.batch.rows)
        self.assertEqual(self.loader.rejected["Specimen"], 1)

    def test_process_row_invalid_aliquot(self):
        self.rowexample['Aliquot.bio_source'] = ''
        self.rowexample['Aliquot.ext_id'] = ''
        self.loader._clean_row(self.rowexample)
        self.loader.process_leukform(self.batch.rows)
        self.assertEqual(self.loader.rejected["Aliquot"], 1)

    def test_process_row_invalid_run(self):
        self.batch.runs[0].delete()
        self.rowexample['Run.projects'] = 'asa5|ss56'
        self.loader._clean_row(self.rowexample)
        self.loader.process_leukform(self.batch.rows)
        self.assertEqual(self.loader.rejected["Run"], 1)

    def test_process_leukform(self):
        batch = LeukformCsvFactory()
        batch.create_batch(5, 3, 2, 1)
        batch.get_rows()
        loader = LeukformLoader()
        for i in batch.individuals:
            i.delete()
        loader.process_leukform(batch.rows)
        added = len(loader.added["Run"])
        self.assertGreater(added, 5)
        self.assertLessEqual(added, 5 * 3 * 2 * 1)

    def test_added_existed_individuals(self):
        batch = LeukformCsvFactory()
        batch.create_batch(5, 3, 2, 1)
        batch.get_rows()
        loader = LeukformLoader()
        for i in range(3):
            batch.individuals[i].delete()

        loader.process_leukform(batch.rows)
        self.assertEqual(len(loader.added['Individual']), 3)
        self.assertEqual(len(loader.existed['Individual']), 2)
