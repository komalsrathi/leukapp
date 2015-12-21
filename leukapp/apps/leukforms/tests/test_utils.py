# -*- coding: utf-8 -*-

# python
import os
import json

# django
from django.test import TestCase

# leukapp
from leukapp.apps.leukforms.utils import LeukformLoader
from leukapp.apps.leukforms.factories import LeukformSamplesFactory
from leukapp.apps.core.constants import UNKNOWN

# local
from ..constants import MODELS_LIST, LEUKAPP_FACTORIES


class TestLeukformLoader(TestCase):

    models = ['Individual', 'Specimen', 'Aliquot', 'Extraction']
    loader = LeukformLoader()
    batch = LeukformSamplesFactory()
    batch.create_batch()
    rowexample = batch.rows[0]

    def setUp(self):
        pass

    def test_update_fields(self):
        parents = ['Individual', 'Specimen', 'Aliquot', 'Extraction']
        children = ['Specimen', 'Aliquot', 'Extraction', 'Workflow']
        for i in range(4):
            parent, child = parents[i], children[i]
            loader, fields = LeukformLoader(), {child: {}}
            instance = LEUKAPP_FACTORIES[parent]()
            fields = loader._update_fields(parent, fields, instance)
            expected = {parent.lower(): instance.pk}
            self.assertDictEqual(fields[child], expected)

    def test_get_fields_empty_row(self):
        loader = LeukformLoader()
        fields = loader._get_fields({})
        self.assertDictEqual(fields, {})

    def test_get_fields(self):
        loader = LeukformLoader()
        fields = loader._get_fields(self.rowexample)
        for column in list(self.rowexample):
            model, field = column.split('.')
            expected = {field: self.rowexample[column]}
            self.assertDictContainsSubset(expected, fields[model])

    def test_get_fields_strip_data(self):
        loader = LeukformLoader()
        copy = self.rowexample.copy()
        for column in list(copy):
            copy[column] += "      "
        fields = loader._get_fields(copy)
        for column in list(copy):
            model, field = column.split('.')
            expected = {field: copy[column].strip()}
            self.assertDictContainsSubset(expected, fields[model])

    def test_get_or_create_accepted(self):
        """
        Starts requesting 1 individual (request = [1]) and tests whether or not
        the individual is created and ACCEPTED. In each iteration, it adds
        the next model (1 individual, 1 specimen: request = [1, 1]) and so on.
        """
        request = {model: 0 for model in MODELS_LIST}
        batch = LeukformSamplesFactory()
        for i, model in enumerate(MODELS_LIST):
            request[model] = 1
            batch.create_batch(request=request, delete=True)
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
        request = {model: 0 for model in MODELS_LIST}
        batch = LeukformSamplesFactory()
        for i, model in enumerate(MODELS_LIST):
            request[model] = 1
            batch.create_batch(request=request, delete=False)
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
        request = {model: 0 for model in MODELS_LIST}
        request["Individual"] = 1
        batch = LeukformSamplesFactory()
        for i, model in enumerate(MODELS_LIST[1:]):
            request[model] = 1
            batch.create_batch(request=request, slug=True)
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
        request = {model: 0 for model in MODELS_LIST}
        request["Individual"] = 1
        batch = LeukformSamplesFactory()
        for i, model in enumerate(MODELS_LIST[1:]):
            request[model] = 1
            row = batch.create_batch(request=request, slug=True)[0]
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
        rows = batch.create_batch()
        row = loader._process_row(rows[0])
        self.assertEqual(row['STATUS'], 'ACCEPTED')

    def test_process_leukform(self):
        request = {model: 1 for model in MODELS_LIST}
        request["Extraction"] = 2
        batch = LeukformSamplesFactory()
        batch.create_batch(request=request, delete=True)
        loader = LeukformLoader()
        loader._columns_submitted = list(batch.rows[0])
        loader._process_leukform(batch.rows)
        added = len(loader.added["Workflow"])
        self.assertEqual(added, 2)

    def test_sort_rows_not_specimen_order(self):
        loader = LeukformLoader()
        rows = loader._sort_rows([{1: 1}])
        self.assertCountEqual([{1: 1}], rows)

    def test_sort_rows_slug(self):
        request = {model: 0 for model in MODELS_LIST}
        request["Individual"] = 1
        request["Specimen"] = 3
        loader = LeukformLoader()
        batch = LeukformSamplesFactory()
        batch.create_batch(request=request, slug=True)
        rows = batch.get_rows(shuffle=True)
        expected = sorted(rows, key=lambda k: (
                k['Individual.slug'], int(k['Specimen.order'])))
        obtained = loader._sort_rows(rows)
        self.assertCountEqual(obtained, expected)

    def test_sort_rows_ext_id(self):
        request = {model: 0 for model in MODELS_LIST}
        request["Individual"] = 1
        request["Specimen"] = 3
        loader = LeukformLoader()
        batch = LeukformSamplesFactory()
        batch.create_batch(request=request, slug=False)
        rows = batch.get_rows(shuffle=True)
        expected = sorted(rows, key=lambda k: (
                k['Individual.ext_id'], int(k['Specimen.order'])))
        obtained = loader._sort_rows(rows)
        self.assertCountEqual(obtained, expected)

    def test_submit_leukform_filename(self):
        batch = LeukformSamplesFactory()
        batch.create_batch(delete=False)
        path = batch.create_csv_from_rows()
        loader = LeukformLoader()
        output = loader.submit(filepath=path, validate=True)
        batch_extractions = [r.ext_id for r in batch.instances["Workflow"]]
        out_extractions = [r.ext_id for r in output["added"]["Workflow"]]
        self.assertCountEqual(batch_extractions, out_extractions)
        os.remove(path)

    def test_submit_leukform_rows(self):
        batch = LeukformSamplesFactory()
        rows = batch.create_batch(delete=False)
        loader = LeukformLoader()
        output = loader.submit(rows=rows, validate=True)
        batch_extractions = [r.ext_id for r in batch.instances["Workflow"]]
        out_extractions = [r.ext_id for r in output["added"]["Workflow"]]
        self.assertCountEqual(batch_extractions, out_extractions)

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

    def test_get_fields_using_special_case(self):
        row = {
            'Individual.ext_id': '123',
            'Specimen.ext_id': '',
            'Aliquot.ext_id': '',
            }
        expected = {
            'Individual': {'ext_id': '123'},
            'Specimen': {'ext_id': UNKNOWN},
            'Aliquot': {'ext_id': UNKNOWN},
            }
        obtained = LeukformLoader()._get_fields(row)
        self.assertDictEqual(obtained, expected)

    def test_clean_specimen_order_column(self):
        request = {model: 0 for model in MODELS_LIST}
        request["Individual"] = 1
        request["Specimen"] = 3
        loader = LeukformLoader()
        batch = LeukformSamplesFactory()
        rows = batch.create_batch(request=request)
        for row in rows[:2]:
            row['Specimen.order'] = ''
        rows = loader._clean_specimen_order_column(rows)
        for row in rows[:2]:
            self.assertEqual(row['Specimen.order'], '0')

    def test_delete_added_models(self):
        batch = LeukformSamplesFactory()
        rows = batch.create_batch(delete=True)
        loader = LeukformLoader()
        loader.submit(rows=rows, validate=False, mock=True)
        for model in loader.added:
            for instance in loader.added[model]:
                with self.assertRaises(AssertionError):
                    instance.delete()

    def test_write_summary(self):
        batch = LeukformSamplesFactory()
        rows = batch.create_batch(delete=True)
        loader = LeukformLoader()
        loader.submit(rows=rows, validate=False, mock=True)
        obtained = loader._write_summary()
        expected = {}
        for model in loader.added:
            expected[model] = {
                "valid": len(loader.added[model]),
                "existed": len(loader.existed[model]),
                "rejected": loader.rejected[model],
                }
        expected = json.dumps(expected)
        self.assertDictEqual(eval(expected), eval(obtained))
