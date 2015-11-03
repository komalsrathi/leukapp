# -*- coding: utf-8 -*-

"""
TODO:
leukform_rows_validator:
    validate unique together for Specimen.order

"""

# django
from django.test import TestCase
from django.core.exceptions import ValidationError

# leukapp
from ..factories import LeukformCsvFactory
from .. import validators


class TestValidators(TestCase):

    models = ['Individual', 'Specimen', 'Aliquot', 'Run']
    batch = LeukformCsvFactory()
    batch.create_batch(5, 4, 3, 2)
    rows = batch.get_rows()
    rowexample = batch.rows[0]

    def setUp(self):
        pass

    def test_leukform_rows_validator_not_rows(self):
        with self.assertRaises(ValidationError):
            validators.leukform_rows_validator(rows=None)
        with self.assertRaises(ValidationError):
            validators.leukform_rows_validator(rows='')
        with self.assertRaises(ValidationError):
            validators.leukform_rows_validator(rows=[])
        with self.assertRaises(ValidationError):
            validators.leukform_rows_validator(rows={})

    def test_leukform_columns_validator_invalid_columns_type(self):
        with self.assertRaises(ValidationError):
            validators.leukform_rows_validator(rows=[{1: 1}, {1, 1}])
        with self.assertRaises(ValidationError):
            validators.leukform_rows_validator(rows=[1, 2])

    def test_leukform_rows_validator_rows_invalid_column_name(self):
        with self.assertRaises(ValidationError):
            validators.leukform_rows_validator(rows=[{'juan': ''}, {'an', ''}])

    def test_leukform_rows_validator_rows_not_individual_column(self):
        with self.assertRaises(ValidationError):
            rows = [{'carlos.juan': ''}, {'me.an', ''}]
            validators.leukform_rows_validator(rows=rows)

    def test_leukform_rows_validator_rows_valid(self):
        result = validators.leukform_rows_validator(rows=[{'Individual.leukid': ''}])
        self.assertEqual(True, result)

    def test_leukform_rows_validator_individuals_leukid_not_valid(self):
        with self.assertRaises(ValidationError):
            validators.leukform_rows_validator(rows=[{'Individual.juan': ''}])

    def test_leukform_specimen_order_unique_together_validator(self):
        batch = LeukformCsvFactory()
        rows = batch.create_batch(2, 2, 0, 0)
        function = validators.leukform_specimen_order_unique_together_validator
        self.assertEqual(True, function(rows))
