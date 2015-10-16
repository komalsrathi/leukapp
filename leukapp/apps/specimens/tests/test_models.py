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

    def test_if_new_adds_one_to_individual_specimens_created(self):
        self.assertEqual(1, SpecimenFactory().individual.specimens_created)

    def test_if_individual_specimens_created_keep_count_correctly(self):
        i = IndividualFactory()
        SpecimenFactory(individual=i)
        SpecimenFactory(individual=i)
        self.assertEqual(2, i.specimens_created)

    def test_if_specimens_created_is_correct_after_delete_specimens(self):
        i = IndividualFactory()
        SpecimenFactory(individual=i).delete()
        SpecimenFactory(individual=i).delete()
        SpecimenFactory(individual=i).delete()
        self.assertEqual(3, i.specimens_created)

    def test_int_id_returns_expected_value(self):
        i = IndividualFactory()
        s = SpecimenFactory(individual=i)
        int_id = str(i.specimens_created)
        self.assertEqual(s.int_id, int_id)

    def test_str_returns_slug(self):
        s = SpecimenFactory()
        slug = '-'.join([s.individual.slug, s.source, s.int_id])
        self.assertEqual(slug, s.__str__())

    def test_if_new_initializes_aliquots_created_with_zero(self):
        self.assertEqual(SpecimenFactory().aliquots_created, 0)

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
