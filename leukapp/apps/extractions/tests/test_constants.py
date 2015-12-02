# -*- coding: utf-8 -*-

"""
Tests for the `extractions` application `constants`.
"""

# django
from django.test import TestCase

# local
from .. import constants


class ExtractionsConstantsTest(TestCase):

    def test_all_analytes_must_be_in_LEUKID_ANALYTE(self):
        """
        All analytes in ANALYTE must have a leukid character.
        """
        ANALYTE = [e[0] for e in constants.ANALYTE]
        for analyte in ANALYTE:
            self.assertIn(analyte, constants.LEUKID_ANALYTE)
