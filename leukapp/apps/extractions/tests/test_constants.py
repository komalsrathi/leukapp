# -*- coding: utf-8 -*-

"""
Tests for the `extractions` application `constants`.
"""

# django
from django.test import TestCase

#leukapp
from leukapp.apps.core.constants import UNKNOWN

# local
from .. import constants


class ExtractionsConstantsTest(TestCase):

    def test_all_platforms_are_in_techplatcode_dictionary(self):
        """
        All platforms must be also included only once in TECHNOLOGY_PLATFORM.
        """
        PLATFORM = [e[0] for e in constants.PLATFORM]

        for platform in PLATFORM:
            if platform == UNKNOWN:
                continue
            platform_isin_codedict = 0
            for technology in constants.TECHNOLOGY_PLATFORM:
                if platform in constants.TECHNOLOGY_PLATFORM[technology]:
                    platform_isin_codedict += 1
            self.assertEqual(True, platform_isin_codedict == 1)

    def test_all_analytes_must_be_in_LEUKID_ANALYTE(self):
        """
        All analytes in ANALYTE must have a leukid character.
        """
        ANALYTE = [e[0] for e in constants.ANALYTE]
        for analyte in ANALYTE:
            self.assertIn(analyte, constants.LEUKID_ANALYTE)

    def test_default_platform_ispart_of_technology(self):
        """
        Default platform must be a valid KEY in
        TECHNOLOGY_PLATFORM[technology].
        """
        for technology in constants.TECHNOLOGY_PLATFORM:
            platforms = list(constants.TECHNOLOGY_PLATFORM[technology])
            default = constants.TECHNOLOGY_PLATFORM[technology]["DEFAULT"]
            self.assertIn(default, platforms)
