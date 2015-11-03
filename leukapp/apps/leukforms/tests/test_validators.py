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
from ..validators import leukform_rows_validator


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
            leukform_rows_validator(rows=None)
        with self.assertRaises(ValidationError):
            leukform_rows_validator(rows='')
        with self.assertRaises(ValidationError):
            leukform_rows_validator(rows=[])
        with self.assertRaises(ValidationError):
            leukform_rows_validator(rows={})

    def test_leukform_rows_validator_rows_not_list(self):
        with self.assertRaises(ValidationError):
            leukform_rows_validator(rows='1234')
        with self.assertRaises(ValidationError):
            leukform_rows_validator(rows={'juan', 'san'})

    def test_leukform_rows_validator_rows_invalid_columns_type(self):
        with self.assertRaises(ValidationError):
            leukform_rows_validator(rows=[{1: 1}, {1, 1}])
        with self.assertRaises(ValidationError):
            leukform_rows_validator(rows=[1, 2])

    def test_leukform_rows_validator_rows_invalid_column_name(self):
        with self.assertRaises(ValidationError):
            leukform_rows_validator(rows=[{'juan': ''}, {'an', ''}])

    def test_leukform_rows_validator_rows_not_individual_column(self):
        with self.assertRaises(ValidationError):
            leukform_rows_validator(rows=[{'carlos.juan': ''}, {'me.an', ''}])

    def test_leukform_rows_validator_rows_valid(self):
        result = leukform_rows_validator(rows=[{'Individual.leukid': ''}])
        self.assertEqual(True, result)

    def test_leukform_rows_validator_individuals_leukid_not_valid(self):
        with self.assertRaises(ValidationError):
            leukform_rows_validator(rows=[{'Individual.juan': ''}])
