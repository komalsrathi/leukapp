# -*- coding: utf-8 -*-

# django imports
from django.test import TestCase

# local imports
from .. import constants
from ..forms import ParticipantForm


class ParticipantFormsTest(TestCase):

    def tests_participant_form_fiels(self):
        """
        ParticipantForm.Meta.fields must be equal to PARTICIPANT_CREATE_FIELDS
        """
        expected = constants.PARTICIPANT_CREATE_FIELDS
        obtained = ParticipantForm().Meta.fields
        self.assertCountEqual(expected, obtained)
