# -*- coding: utf-8 -*-

"""
Tests for the `workflows` application `constants`.
"""

# django
from django.test import TestCase

# leukapp
from leukapp.apps.core.constants import DEFAULT

# local
from .. import constants
from ..constants import DNA, RNA


class WorkflowsConstantsTest(TestCase):

    def test_all_technology_types_are_in_techplatcode_dictionary(self):
        """
        All technology_types must be included only once in INT_ID_TECHNOLOGY.
        """
        TECHNOLOGY_TYPE = [e[0] for e in constants.TECHNOLOGY_TYPE]
        TECHNOLOGY = list(constants.INT_ID_TECHNOLOGY[DNA])
        TECHNOLOGY += list(constants.INT_ID_TECHNOLOGY[RNA])

        for technology_type in TECHNOLOGY_TYPE:
            if technology_type == DEFAULT:
                continue
            technology_type_isin_codedict = 0

            DNA_TECHNOLOGY = constants.INT_ID_TECHNOLOGY[DNA]
            for technology in DNA_TECHNOLOGY:
                if technology_type in DNA_TECHNOLOGY[technology]:
                    technology_type_isin_codedict += 1

            RNA_TECHNOLOGY = constants.INT_ID_TECHNOLOGY[RNA]
            for technology in RNA_TECHNOLOGY:
                if technology_type in RNA_TECHNOLOGY[technology]:
                    technology_type_isin_codedict += 1

            self.assertEqual(True, technology_type_isin_codedict == 1)

    def test_default_technology_type_ispart_of_technology(self):
        """
        "DEFAULT_TECHNOLOGY" must be a valid KEY in
        INT_ID_TECHNOLOGY[analyte][technology].
        """
        for technology in constants.INT_ID_TECHNOLOGY[DNA]:
            technologies = constants.INT_ID_TECHNOLOGY[DNA]
            technology_types = technologies[technology]
            default = technology_types["DEFAULT_TECHNOLOGY"]
            self.assertIn(default, technology_types)

        for technology in constants.INT_ID_TECHNOLOGY[RNA]:
            technologies = constants.INT_ID_TECHNOLOGY[RNA]
            technology_types = technologies[technology]
            default = technology_types["DEFAULT_TECHNOLOGY"]
            self.assertIn(default, technology_types)

    def test_all_centers_must_be_in_INT_ID_CENTER(self):
        """
        All centers in CENTER must have a leukid character.
        """
        CENTER = [e[0] for e in constants.CENTER]
        for center in CENTER:
            self.assertIn(center, constants.INT_ID_CENTER)

    def test_all_platforms_must_be_in_INT_ID_PLATFORM(self):
        """
        All platforms in PLATFORM must have a leukid character.
        """
        PLATFORM = [e[0] for e in constants.PLATFORM]
        for platform in PLATFORM:
            self.assertIn(platform, constants.INT_ID_PLATFORM)

    def test_all_read_lengths_must_be_in_INT_ID_READ_LENGTH(self):
        """
        All read_lengths in READ_LENGTH must have a leukid character.
        """
        READ_LENGTH = [e[0] for e in constants.READ_LENGTH]
        for read_length in READ_LENGTH:
            self.assertIn(read_length, constants.INT_ID_READ_LENGTH)

    def test_all_read_types_must_be_in_INT_ID_READ_TYPE(self):
        """
        All read_types in READ_TYPE must have a leukid character.
        """
        READ_TYPE = [e[0] for e in constants.READ_TYPE]
        for read_type in READ_TYPE:
            self.assertIn(read_type, constants.INT_ID_READ_TYPE)
