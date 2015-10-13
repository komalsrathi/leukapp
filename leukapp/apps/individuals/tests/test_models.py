# -*- coding: utf-8 -*-

# django
from django.test import TestCase
from django.db.utils import IntegrityError
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

# local
from ..models import Individual
from .. import constants


class IndividualModelTest(TestCase):

    def setUp(self):
        self.individual_a = Individual()
        self.individual_a.institution = "MSK"
        self.individual_a.species = "H"
        self.individual_a.ext_id = "12345678910"
        self.individual_a.save()

        self.individual_b = Individual()
        self.individual_b.institution = "O"
        self.individual_b.species = "M"
        self.individual_b.ext_id = "1234567891K"
        self.individual_b.save()

    def test_saving_and_retrieving_individuals(self):
        saved_objects = Individual.objects.all()
        self.assertEqual(saved_objects.count(), 2)

        first_saved_object = saved_objects[0]
        second_saved_object = saved_objects[1]
        self.assertEqual(first_saved_object.institution, "MSK")
        self.assertEqual(first_saved_object.species, "H")
        self.assertEqual(first_saved_object.ext_id, "12345678910")
        self.assertEqual(second_saved_object.institution, "O")
        self.assertEqual(second_saved_object.species, "M")
        self.assertEqual(second_saved_object.ext_id, "1234567891K")

    def test_check_institution_return_internal(self):
        self.assertEqual(self.individual_a.check_institution(), 'I')

    def test_check_institution_return_external(self):
        self.assertEqual(self.individual_b.check_institution(), 'E')

    def test_unique_together_functionality(self):
        self.individual_b.institution = "MSK"
        self.individual_b.species = "H"
        self.individual_b.ext_id = "12345678910"

        with self.assertRaises(IntegrityError):
            self.individual_b.save()

    def test_int_id_returns_expected_value(self):
        int_id = str(self.individual_a.pk + 100000)
        self.assertEqual(self.individual_a.int_id, int_id)

    def test_institution_verbose_name(self):
        verbose_name = \
            Individual._meta.get_field_by_name('institution')[0].verbose_name
        self.assertEqual(verbose_name, _("institution"))

    def test_str_returns_slug(self):
        slug = "-".join([
            self.individual_a.check_institution(),
            self.individual_a.species,
            self.individual_a.int_id,
        ])
        self.assertEqual(slug, self.individual_a.__str__())

    def test_if_new_initializes_specimens_created_with_zero(self):
            self.assertEqual(self.individual_a.specimens_created, 0)

    def test_ext_id_uses_validator(self):
        self.individual_b.institution = "MSK"
        self.individual_b.species = "H"
        self.individual_b.ext_id = "1234 % ''10"

        with self.assertRaises(ValidationError):
            self.individual_b.full_clean()

    def test_get_absolute_url(self):
        slug = self.individual_a.slug
        url = reverse(constants.APP_NAME + ':detail', kwargs={'slug': slug})
        self.assertEqual(url, self.individual_a.get_absolute_url())

    def test_get_update_url(self):
        slug = self.individual_a.slug
        url = reverse(constants.APP_NAME + ':update', kwargs={'slug': slug})
        self.assertEqual(url, self.individual_a.get_update_url())
