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
from ..factories import LeukformSamplesFactory
from .. import validators


class TestValidators(TestCase):

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
        rows = [{'Individual.slug': ''}]
        result = validators.leukform_rows_validator(rows=rows)
        self.assertEqual(True, result)

    def test_leukform_rows_validator_individuals_leukid_not_valid(self):
        with self.assertRaises(ValidationError):
            validators.leukform_rows_validator(rows=[{'Individual.juan': ''}])

    def test_leukform_specimen_order_validator_valid(self):
        batch = LeukformSamplesFactory()
        rows = batch.create_batch(2, 2, 0, 0)
        function = validators.leukform_specimen_order_validator
        self.assertEqual(True, function(rows))

    def test_leukform_specimen_order_validator_not_valid(self):
        batch = LeukformSamplesFactory()
        rows = batch.create_batch(1, 2, 0, 0)
        rows[1]['Specimen.order'] = rows[0]['Specimen.order']
        function = validators.leukform_specimen_order_validator
        with self.assertRaises(ValidationError):
            function(rows)

    def test_leukform_specimen_order_validator_valid_using_slug(self):
        batch = LeukformSamplesFactory()
        rows = batch.create_batch(2, 2, 0, 0, delete=False)
        function = validators.leukform_specimen_order_validator
        self.assertEqual(True, function(rows))

    def test_leukform_specimen_order_validator_not_valid_using_slug(self):
        batch = LeukformSamplesFactory()
        rows = batch.create_batch(1, 2, 0, 0, delete=False)
        rows[1]['Specimen.order'] = rows[0]['Specimen.order']
        function = validators.leukform_specimen_order_validator
        with self.assertRaises(ValidationError):
            function(rows)
