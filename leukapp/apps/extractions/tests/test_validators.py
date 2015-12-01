# |*- coding: utf-8 -*-

"""
Tests for the `extractions` application `validators`.
"""

# django
from django.test import TestCase
from django.core.exceptions import ValidationError

# local
from .. import constants
from .. import validators


class ExtractionsValidatorsTest(TestCase):

    """
    Tests for the `extractions` application `validators`.
    """

    def test_projects_string_validator_valid(self):
        """
        `projects_string_validator` must return True for valid formats.
        """
        valid = ['100|1001|300', "10| 1|   30"]
        v = validators.projects_string_validator
        [self.assertTrue(v(string)) for string in valid]

    def test_projects_string_validator_invalid(self):
        """
        `projects_string_validator` must raise error for invalid formats.
        """
        invalid = ['123, 12, 32', 'juansan|carlos|10']
        v = validators.projects_string_validator
        for string in invalid:
            with self.assertRaises(ValidationError):
                v(string)

    def test_technology_platform_validator_valid(self):
        """
        `technology_platform_validator` must return True for valid
        combinations.
        """
        v = validators.technology_platform_validator
        for technology in constants.TECHNOLOGY_PLATFORM:
            for platform in constants.TECHNOLOGY_PLATFORM[technology]:
                self.assertTrue(v(technology=technology, platform=platform))

    def test_technology_platform_validator_invalid(self):
        """
        `technology_platform_validator` must raise error for invalid
        combinations.
        """
        v = validators.technology_platform_validator
        for technology in constants.TECHNOLOGY_PLATFORM:
            with self.assertRaises(ValidationError):
                v(technology=technology, platform='INVALIDPLATFORM')
