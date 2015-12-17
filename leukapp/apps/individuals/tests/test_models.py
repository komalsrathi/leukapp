# -*- coding: utf-8 -*-

# django
from django.test import TestCase
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

# local
from ..models import Individual
from ..constants import APP_NAME, MSK, HUMAN, OTHER, INT_ID_SPECIES
from ..factories import IndividualFactory


class IndividualModelTest(TestCase):

    """Tests for the individuals.models module."""

    def test_saving_and_retrieving_individuals(self):
        """Test saving_and_retrieving_individuals."""
        i_a, i_b = IndividualFactory(), IndividualFactory()
        objects = Individual.objects.all().order_by('created')
        self.assertEqual(objects.count(), 2)
        self.assertEqual(objects[0], i_a)
        self.assertEqual(objects[1], i_b)

    def test_check_institution_return_internal(self):
        """Test check_institution_return_internal."""
        i = IndividualFactory(institution=MSK)
        self.assertEqual(i.check_institution(), 'I')

    def test_check_institution_return_external(self):
        """Test check_institution_return_external."""
        i = IndividualFactory(institution=OTHER)
        self.assertEqual(i.check_institution(), 'E')

    def test_unique_together_functionality(self):
        """Test unique_together_functionality."""
        i = IndividualFactory()
        with self.assertRaises(IntegrityError):
            Individual.objects.create(
                species=i.species, institution=i.institution, ext_id=i.ext_id)

    def test_int_id_returns_expected_value(self):
        """Test int_id_returns_expected_value."""
        i = IndividualFactory(institution=MSK)
        species = INT_ID_SPECIES[i.species]
        int_id = "-".join([i.check_institution(), species, str(i.pk)])
        self.assertEqual(i.int_id, int_id)

    def test_str_returns_slug(self):
        """Test str_returns_slug."""
        i = IndividualFactory(institution=MSK, species=HUMAN, ext_id='1')
        slug = i.int_id
        self.assertEqual(slug, i.__str__())

    def test_if_new_initializes_specimens_counts_with_zero(self):
        """Test if_new_initializes_specimens_counts_with_zero."""
        self.assertEqual(IndividualFactory().tumors_count, 0)
        self.assertEqual(IndividualFactory().normals_count, 0)
        self.assertEqual(IndividualFactory().queries_count, 0)

    def test_ext_id_uses_validator(self):
        """Test ext_id_uses_validator."""
        i = IndividualFactory(ext_id="1234 % ''10")
        with self.assertRaises(ValidationError):
            i.full_clean()

    def test_get_absolute_url(self):
        """Test get_absolute_url."""
        i = IndividualFactory()
        slug = i.slug
        url = reverse(APP_NAME + ':detail', kwargs={'slug': slug})
        self.assertEqual(url, i.get_absolute_url())

    def test_get_update_url(self):
        """Test get_update_url."""
        i = IndividualFactory()
        slug = i.slug
        url = reverse(APP_NAME + ':update', kwargs={'slug': slug})
        self.assertEqual(url, i.get_update_url())
