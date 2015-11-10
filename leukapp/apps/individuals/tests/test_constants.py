# -*- coding: utf-8 -*-

from .. import constants


class ConstantsTest(TestCase):

    def test_LEUKID_SPECIES_is_subset_of_SPECIES(self):
        species = [tup[0] for tup in constants.SPECIES]
        self.assertCounEqual(species, list(constants.LEUKID_SPECIES))
