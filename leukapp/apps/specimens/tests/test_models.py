# -*- coding: utf-8 -*-

# django imports
from django.test import TestCase
from django.db.utils import IntegrityError
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

# apps imports
from leukapp.apps.individuals.models import Individual

# local imports
from ..models import Specimen
from .. import constants


class SpecimenModelTest(TestCase):

    def setUp(self):
        self.individual_a = Individual.objects.create(
            institution="MSK",
            species="H",
            ext_id="12345678910",
        )

        self.specimen_a = Specimen.objects.create(
            individual=self.individual_a,
            source='T',
            ext_id='123456789',
        )

    def test_saving_and_retrieving_specimens(self):
        saved_specimens = Specimen.objects.all()
        self.assertEqual(saved_specimens.count(), 1)

        first_saved_specimen = saved_specimens[0]
        self.assertEqual(first_saved_specimen.individual, self.individual_a)
        self.assertEqual(first_saved_specimen.source, 'T')
        self.assertEqual(first_saved_specimen.ext_id, '123456789')

    def test_ext_id_uses_validator(self):
        self.specimen_a.ext_id = "1234 % ''10"

        with self.assertRaises(ValidationError):
            self.specimen_a.full_clean()

    def test_unique_together_functionality(self):
        with self.assertRaises(IntegrityError):
            self.specimen_b = Specimen.objects.create(
                individual=self.individual_a,
                source='T',
                ext_id='123456789',
            )

    def test_if_new_adds_one_to_individual_specimens_created(self):
        self.assertEqual(1, self.specimen_a.individual.specimens_created)

    def test_if_individual_specimens_created_keep_count_correctly(self):
        self.specimen_b = Specimen.objects.create(
            individual=self.individual_a,
            source='T',
            ext_id='123456789051',
        )
        self.assertEqual(2, self.specimen_a.individual.specimens_created)

    def test_if_specimens_created_is_correct_after_delete_specimens(self):
        self.specimen_b = Specimen.objects.create(
            individual=self.individual_a,
            source='T',
            ext_id='123456789051',
        )
        self.specimen_c = Specimen.objects.create(
            individual=self.individual_a,
            source='T',
            ext_id='123456789051456',
        )
        self.specimen_b.delete()
        self.specimen_c.delete()
        self.assertEqual(3, self.specimen_a.individual.specimens_created)

    def test_int_id_returns_expected_value(self):
        self.specimen_b = Specimen.objects.create(
            individual=self.individual_a,
            source='T',
            ext_id='123456789051',
        )
        int_id = str(self.individual_a.specimens_created)
        self.assertEqual(self.specimen_b.int_id, int_id)

    def test_str_returns_slug(self):
        slug = '-'.join([
            self.specimen_a.individual.slug,
            self.specimen_a.source,
            self.specimen_a.int_id])
        self.assertEqual(slug, self.specimen_a.__str__())

    def test_if_new_initializes_aliquots_created_with_zero(self):
            self.assertEqual(self.specimen_a.aliquots_created, 0)

    def test_get_absolute_url(self):
        slug = self.specimen_a.slug
        url = reverse(constants.APP_NAME + ':detail', kwargs={'slug': slug})
        self.assertEqual(url, self.specimen_a.get_absolute_url())

    def test_get_update_url(self):
        slug = self.specimen_a.slug
        url = reverse(constants.APP_NAME + ':update', kwargs={'slug': slug})
        self.assertEqual(url, self.specimen_a.get_update_url())
