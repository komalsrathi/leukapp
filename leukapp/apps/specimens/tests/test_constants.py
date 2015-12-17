# -*- coding: utf-8 -*-

"""Tests for the `workflows` application `constants`."""

# django
from django.test import TestCase

# local
from .. import constants


class SpecimenConstantsTest(TestCase):

    """Tests for specimens constants."""

    def test_leukid_field_should_have_id_characters(self):
        """Test if leukid field has a leukid character."""
        for source_type in constants.SOURCE_TYPE:
            self.assertIn(source_type[0], constants.INT_ID_SOURCE_TYPE)
