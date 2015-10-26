# -*- coding: utf-8 -*-

# django imports
from django.test import TestCase
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

# apps imports
from leukapp.apps.individuals.factories import IndividualFactory

# local imports
from ..models import Specimen
from ..factories import SpecimenFactory
from .. import constants


class SpecimenModelTest(TestCase):

    def test_saving_and_retrieving_specimens(self):
        s = SpecimenFactory()
        specimens = Specimen.objects.all()
        self.assertEqual(specimens.count(), 1)
        self.assertEqual(specimens[0], s)

    def test_ext_id_uses_validator(self):
        with self.assertRaises(ValidationError):
            SpecimenFactory(ext_id="1234 % ''10").full_clean()

    def test_unique_together_functionality(self):
        s = SpecimenFactory()
        with self.assertRaises(IntegrityError):
            Specimen.objects.create(individual=s.individual, ext_id=s.ext_id)

    def test_if_specimen_counters_keep_count_correctly(self):
        i = IndividualFactory()
        for c in range(3):
            SpecimenFactory(individual=i, source_type=constants.TUMOR)
        for c in range(2):
            SpecimenFactory(individual=i, source_type=constants.NORMAL)
        self.assertEqual(3, i.tumors_count)
        self.assertEqual(2, i.normals_count)

    def test_if_specimen_counters_are_correct_after_delete_specimens(self):
        i = IndividualFactory()
        for c in range(3):
            SpecimenFactory(
                individual=i, source_type=constants.TUMOR).delete()
            SpecimenFactory(
                individual=i, source_type=constants.NORMAL).delete()
        self.assertEqual(3, i.tumors_count)
        self.assertEqual(3, i.normals_count)

    def test_int_id_returns_expected_value(self):
        i = IndividualFactory()
        st = SpecimenFactory(individual=i, source_type=constants.TUMOR)
        sn = SpecimenFactory(individual=i, source_type=constants.NORMAL)
        st_int_id = constants.TUMOR + str(i.tumors_count)
        sn_int_id = constants.NORMAL + str(i.normals_count)
        self.assertEqual(st.int_id, st_int_id)
        self.assertEqual(sn.int_id, sn_int_id)

    def test_str_returns_slug(self):
        s = SpecimenFactory()
        slug = '-'.join([s.individual.slug, s.int_id])
        self.assertEqual(slug, s.__str__())

    def test_if_new_initializes_aliquots_counters_with_zero(self):
        self.assertEqual(SpecimenFactory().dna_count, 0)
        self.assertEqual(SpecimenFactory().rna_count, 0)

    def test_get_absolute_url(self):
        s = SpecimenFactory()
        slug = s.slug
        url = reverse(constants.APP_NAME + ':detail', kwargs={'slug': slug})
        self.assertEqual(url, s.get_absolute_url())

    def test_get_update_url(self):
        s = SpecimenFactory()
        slug = s.slug
        url = reverse(constants.APP_NAME + ':update', kwargs={'slug': slug})
        self.assertEqual(url, s.get_update_url())
