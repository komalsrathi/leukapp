# -*- coding: utf-8 -*-

# python
import os

# django
from django.test import TestCase

# leukapp
from leukapp.apps.leukforms.utils import LeukformLoader
from leukapp.apps.leukforms.factories import LeukformSamplesFactory

# local
from ..constants import MODELS_LIST, LEUKAPP_FACTORIES


class TestLeukformLoader(TestCase):

    models = ['Individual', 'Specimen', 'Aliquot', 'Run']
    loader = LeukformLoader()
    batch = LeukformSamplesFactory()
    batch.create_batch(1, 1, 1, 1)
    rowexample = batch.rows[0]

    def setUp(self):
        pass

    def test_update_fields_individual(self):
        models = ['Individual', 'Specimen', 'Aliquot']
        children = ['Specimen', 'Aliquot', 'Run']
        for i in range(3):
            model, child = models[i], children[i]
            loader, fields = LeukformLoader(), {child: {}}
            instance = LEUKAPP_FACTORIES[model]()
            fields = loader._update_fields(model, fields, instance)
            expected = {model.lower(): instance.pk}
            self.assertDictEqual(fields[child], expected)

    def test_clean_fields_empty_row(self):
        loader = LeukformLoader()
        fields = loader._get_fields({})
        self.assertDictEqual(fields, {})

    def test_clean_fields(self):
        loader = LeukformLoader()
        fields = loader._get_fields(self.rowexample)
        for column in list(self.rowexample):
            model, field = column.split('.')
            expected = {field: self.rowexample[column]}
            self.assertDictContainsSubset(expected, fields[model])

    def test_get_or_create_accepted(self):
        """
        Starts requesting 1 individual (request = [1]) and tests whether or not
        the individual is created and ACCEPTED. In each iteration, it adds
        the next model (1 individual, 1 specimen: request = [1, 1]) and so on.
        """
        request = []
        batch = LeukformSamplesFactory()
        for i in range(4):
            request.append(1)
            batch.create_batch(*request, delete=True)
            loader = LeukformLoader()
            fields = loader._get_fields(batch.rows[0])
            for model in MODELS_LIST[:i+1]:
                instance, msg = loader._get_or_create(model, fields)
                fields = loader._update_fields(model, fields, instance)
                expected = batch.instances[model][0]
                self.assertEqual('ACCEPTED', msg)
                self.assertEqual(expected.ext_id, instance.ext_id)
                self.assertEqual(len(loader.added[model]), 1)

    def test_get_or_create_existed_slug_false(self):
        """
        Using the same rationale as `test_get_or_create_accepted`, this test
        evaluates whether or not instances are found (EXISTED) using all their
        data. For the last model requested, it tests whether or not they are
        created correctly. This is a LeukformSamplesFactory functionality.
        Instances for the last model requested are always deleted.
        """
        request = []
        batch = LeukformSamplesFactory()
        for i in range(4):
            request.append(1)
            batch.create_batch(*request, delete=False)
            loader = LeukformLoader()
            fields = loader._get_fields(batch.rows[0])
            for j, model in enumerate(MODELS_LIST[:i+1]):
                instance, msg = loader._get_or_create(model, fields)
                fields = loader._update_fields(model, fields, instance)
                expected = batch.instances[model][0]
                self.assertEqual(expected.ext_id, instance.ext_id)
                if j == i:
                    self.assertEqual('ACCEPTED', msg)
                    self.assertEqual(len(loader.added[model]), 1)
                else:
                    self.assertEqual('EXISTED', msg)
                    self.assertEqual(len(loader.existed[model]), 1)

    def test_get_or_create_existed_slug_true(self):
        """
        Using the same rationale as `test_get_or_create_accepted`, this test
        evaluates whether or not instances are found (EXISTED) using their
        slug. For the last model requested, it tests whether or not they are
        created correctly. This is a LeukformSamplesFactory functionality.
        Instances for the last model requested are always deleted.

        When using slug=True in LeukformSamplesFactory, only two sets of data
        are provided: the data of the object to be created and the slug of the
        parent object. Therefore, when j==0 it's always and existing object,
        and when j==1, it's always a created object.
        """
        request = [1]
        batch = LeukformSamplesFactory()
        for i in range(3):
            request.append(1)
            batch.create_batch(*request, slug=True)
            loader = LeukformLoader()
            fields = loader._get_fields(batch.rows[0])
            for j, model in enumerate(MODELS_LIST[i:i+2]):
                instance, msg = loader._get_or_create(model, fields)
                fields = loader._update_fields(model, fields, instance)
                expected = batch.instances[model][0]
                self.assertEqual(expected.ext_id, instance.ext_id)
                if j == 0:
                    self.assertEqual('EXISTED', msg)
                    self.assertEqual(len(loader.existed[model]), 1)
                else:
                    self.assertEqual('ACCEPTED', msg)
                    self.assertEqual(len(loader.added[model]), 1)

    def test_get_or_create_invalid_slug(self):
        request = [1]
        batch = LeukformSamplesFactory()
        for i in range(3):
            request.append(1)
            row = batch.create_batch(*request, slug=True)[0]
            row[MODELS_LIST[i] + '.slug'] = '546321'
            loader = LeukformLoader()
            fields = loader._get_fields(row)
            model = MODELS_LIST[i]
            instance, msg = loader._get_or_create(model, fields)
            self.assertEqual('SLUG NOT FOUND', msg)
            self.assertEqual(loader.rejected[model], 1)

    def test_process_row(self):
        loader = LeukformLoader()
        batch = LeukformSamplesFactory()
        rows = batch.create_batch(1, 1, 1, 1)
        row = loader._process_row(rows[0])
        self.assertEqual(row['STATUS'], 'ACCEPTED')

    def test_process_leukform(self):
        batch = LeukformSamplesFactory()
        batch.create_batch(2, 2, 2, 2, delete=True)
        loader = LeukformLoader()
        loader._columns_submitted = list(batch.rows[0])
        loader._process_leukform(batch.rows)
        added = len(loader.added["Run"])
        self.assertEqual(added, 2 ** 4)

    def test_sort_rows_not_specimen_order(self):
        loader = LeukformLoader()
        rows = loader._sort_rows([{1: 1}])
        self.assertCountEqual([{1: 1}], rows)

    def test_sort_rows_slug(self):
        loader = LeukformLoader()
        batch = LeukformSamplesFactory()
        batch.create_batch(1, 3, slug=True)
        rows = batch.get_rows(shuffle=True)
        expected = sorted(rows, key=lambda k: (
                k['Individual.slug'], int(k['Specimen.order'])))
        obtained = loader._sort_rows(rows)
        self.assertCountEqual(obtained, expected)

    def test_sort_rows_ext_id(self):
        loader = LeukformLoader()
        batch = LeukformSamplesFactory()
        batch.create_batch(1, 3, slug=False)
        rows = batch.get_rows(shuffle=True)
        expected = sorted(rows, key=lambda k: (
                k['Individual.ext_id'], int(k['Specimen.order'])))
        obtained = loader._sort_rows(rows)
        self.assertCountEqual(obtained, expected)

    def test_submit_leukform_filename(self):
        batch = LeukformSamplesFactory()
        batch.create_batch(2, 2, 2, 2, delete=False)
        path = batch.create_csv_from_rows()
        loader = LeukformLoader()
        output = loader.submit(filepath=path, validate=True)
        batch_runs = [r.ext_id for r in batch.instances["Run"]]
        out_runs = [r.ext_id for r in output["added"]["Run"]]
        self.assertCountEqual(batch_runs, out_runs)
        os.remove(path)

    def test_submit_leukform_rows(self):
        batch = LeukformSamplesFactory()
        rows = batch.create_batch(2, 2, 2, 2, delete=False)
        loader = LeukformLoader()
        output = loader.submit(rows=rows, validate=True)
        batch_runs = [r.ext_id for r in batch.instances["Run"]]
        out_runs = [r.ext_id for r in output["added"]["Run"]]
        self.assertCountEqual(batch_runs, out_runs)

    def test_submit_leukform_no_rows_no_filename(self):
        with self.assertRaises(Exception):
            LeukformLoader().submit()

    def test_submit_leukform_rows_and_filename(self):
        with self.assertRaises(Exception):
            LeukformLoader().submit(rows=[], filename='juan')

    def test_alter_row_special_case_specimen_blank_no_aliquot(self):
        row = {
            'Individual.ext_id': '123',
            'Specimen.ext_id': ''
            }
        obtained = LeukformLoader()._alter_row_special_case(row)
        expected = row
        expected['Specimen.ext_id'] = 1
        self.assertDictEqual(obtained, expected)

    def test_alter_row_special_case_specimen_blank_aliquot_blank(self):
        row = {
            'Individual.ext_id': '123',
            'Specimen.ext_id': '',
            'Aliquot.ext_id': '',
            }
        obtained = LeukformLoader()._alter_row_special_case(row)
        expected = row
        expected['Specimen.ext_id'] = 1
        expected['Aliquot.ext_id'] = 1
        self.assertDictEqual(obtained, expected)

    def test_alter_row_special_case_specimen_notblank_aliquot_blank(self):
        row = {
            'Individual.ext_id': '123',
            'Specimen.ext_id': '123',
            'Aliquot.ext_id': '',
            }
        obtained = LeukformLoader()._alter_row_special_case(row)
        expected = row
        expected['Aliquot.ext_id'] = 1
        self.assertDictEqual(obtained, expected)

    def test_alter_row_special_case_no_individual_ext_id(self):
        row = {
            'Individual.slug': '123',
            'Specimen.ext_id': '',
            'Aliquot.ext_id': '',
            }
        obtained = LeukformLoader()._alter_row_special_case(row)
        self.assertDictEqual(obtained, row)
