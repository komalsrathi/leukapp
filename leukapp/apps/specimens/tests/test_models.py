# -*- coding: utf-8 -*-

"""Tests for the specimens.models module."""

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

    """Tests for the specimens.models module."""

    def test_saving_and_retrieving_specimens(self):
        """Test saving_and_retrieving_specimens."""
        s = SpecimenFactory()
        specimens = Specimen.objects.all()
        self.assertEqual(specimens.count(), 1)
        self.assertEqual(specimens[0], s)

    def test_ext_id_uses_validator(self):
        """Test ext_id_uses_validator."""
        with self.assertRaises(ValidationError):
            SpecimenFactory(ext_id="1234 % ''10").full_clean()

    def test_unique_together_functionality(self):
        """Test unique_together_functionality."""
        s = SpecimenFactory()
        with self.assertRaises(IntegrityError):
            Specimen.objects.create(
                individual=s.individual,
                ext_id=s.ext_id,
                source_type=s.source_type)

    def test_if_specimen_counters_keep_count_correctly(self):
        """Test if_specimen_counters_keep_count_correctly."""
        i = IndividualFactory()
        for c in range(2):
            SpecimenFactory(individual=i, source_type=constants.TUMOR)
            SpecimenFactory(individual=i, source_type=constants.NORMAL)
            SpecimenFactory(individual=i, source_type=constants.QUERY)
        self.assertEqual(2, i.tumors_count)
        self.assertEqual(2, i.normals_count)
        self.assertEqual(2, i.queries_count)

    def test_if_specimen_counters_are_correct_after_delete_specimens(self):
        """Test if_specimen_counters_are_correct_after_delete_specimens."""
        i = IndividualFactory()
        for c in range(2):
            SpecimenFactory(
                individual=i, source_type=constants.TUMOR).delete()
            SpecimenFactory(
                individual=i, source_type=constants.NORMAL).delete()
            SpecimenFactory(
                individual=i, source_type=constants.QUERY).delete()
        self.assertEqual(2, i.tumors_count)
        self.assertEqual(2, i.normals_count)
        self.assertEqual(2, i.queries_count)

    def test_int_id_returns_expected_value(self):
        """Test int_id_returns_expected_value."""
        i = IndividualFactory()
        st = SpecimenFactory(individual=i, source_type=constants.TUMOR)
        sn = SpecimenFactory(individual=i, source_type=constants.NORMAL)
        sq = SpecimenFactory(individual=i, source_type=constants.QUERY)
        st_int_id = constants.INT_ID_SOURCE_TYPE[constants.TUMOR]
        st_int_id += str(i.tumors_count)
        sn_int_id = constants.INT_ID_SOURCE_TYPE[constants.NORMAL]
        sn_int_id += str(i.normals_count)
        sq_int_id = constants.INT_ID_SOURCE_TYPE[constants.QUERY]
        sq_int_id += str(i.queries_count)
        self.assertEqual(st.int_id, st_int_id)
        self.assertEqual(sn.int_id, sn_int_id)
        self.assertEqual(sq.int_id, sq_int_id)

    def test_str_returns_slug(self):
        """Test str_returns_slug."""
        s = SpecimenFactory()
        slug = '-'.join([s.individual.slug, s.int_id])
        self.assertEqual(slug, s.__str__())

    def test__if_new_initializes_aliquots_counters_with_zero(self):
        """Test _if_new_initializes_aliquots_counters_with_zero."""
        self.assertEqual(SpecimenFactory().aliquots_count, 0)

    def test_get_absolute_url(self):
        """Test get_absolute_url."""
        s = SpecimenFactory()
        slug = s.slug
        url = reverse(constants.APP_NAME + ':detail', kwargs={'slug': slug})
        self.assertEqual(url, s.get_absolute_url())

    def test_get_update_url(self):
        """Test get_update_url."""
        s = SpecimenFactory()
        slug = s.slug
        url = reverse(constants.APP_NAME + ':update', kwargs={'slug': slug})
        self.assertEqual(url, s.get_update_url())
