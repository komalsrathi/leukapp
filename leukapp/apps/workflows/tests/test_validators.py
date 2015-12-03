# |*- coding: utf-8 -*-

"""
Tests for the `workflows` application `validators`.
"""

# django
from django.test import TestCase
from django.core.exceptions import ValidationError

# leukapp
from leukapp.apps.extractions.constants import DNA, RNA

# local
from .. import constants
from .. import validators


class WorkflowsValidatorsTest(TestCase):

    """
    Tests for the `workflows` application `validators`.
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

    def test_technology_type_validator_return_true(self):
        """
        Valid analyte/technology/technology_type combination must return True.
        """
        v = validators.technology_type_validator
        for analyte in constants.INT_ID_TECHNOLOGY:
            technologies = constants.INT_ID_TECHNOLOGY[analyte]
            for sequencing_technology in technologies:
                types = technologies[sequencing_technology]
                for technology_type in types:
                    validate = v(
                        analyte=analyte,
                        sequencing_technology=sequencing_technology,
                        technology_type=technology_type,
                        )
                    self.assertTrue(validate)

    def test_technology_type_validator_return_false(self):
        """
        Invalid analyte/technology/technology_type combination return False.
        """
        v = validators.technology_type_validator

        technologies = constants.INT_ID_TECHNOLOGY[DNA]
        for sequencing_technology in technologies:
            types = technologies[sequencing_technology]
            for technology_type in types:
                with self.assertRaises(ValidationError):
                    v(
                        analyte=RNA,
                        sequencing_technology=sequencing_technology,
                        technology_type=technology_type,
                        )

        v = validators.technology_type_validator
        for analyte in constants.INT_ID_TECHNOLOGY:
            technologies = constants.INT_ID_TECHNOLOGY[analyte]
            for sequencing_technology in technologies:
                types = technologies[sequencing_technology]
                for technology_type in types:
                    with self.assertRaises(ValidationError):
                        v(
                            analyte=analyte,
                            sequencing_technology=sequencing_technology,
                            technology_type="JUAN",
                            )
