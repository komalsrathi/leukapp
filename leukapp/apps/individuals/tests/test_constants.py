# -*- coding: utf-8 -*-

# django imports
from django.test import TestCase

# local
from .. import constants


class ConstantsTest(TestCase):

    def test_INT_ID_SPECIES_is_subset_of_SPECIES(self):
        species = [tup[0] for tup in constants.SPECIES]
        self.assertCountEqual(species, list(constants.INT_ID_SPECIES))
