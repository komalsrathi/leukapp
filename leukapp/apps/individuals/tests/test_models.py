# -*- coding: utf-8 -*-

# django
from django.test import TestCase
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

# local
from ..models import Individual
from .. import constants
from ..factories import IndividualFactory


class IndividualModelTest(TestCase):

    def test_saving_and_retrieving_individuals(self):
        i_a, i_b = IndividualFactory(), IndividualFactory()
        objects = Individual.objects.all().order_by('created')
        self.assertEqual(objects.count(), 2)
        self.assertEqual(objects[0], i_a)
        self.assertEqual(objects[1], i_b)

    def test_check_institution_return_internal(self):
        i = IndividualFactory(institution='MSK')
        self.assertEqual(i.check_institution(), 'I')

    def test_check_institution_return_external(self):
        i = IndividualFactory(institution='O')
        self.assertEqual(i.check_institution(), 'E')

    def test_unique_together_functionality(self):
        i = IndividualFactory()
        with self.assertRaises(IntegrityError):
            Individual.objects.create(
                species=i.species, institution=i.institution, ext_id=i.ext_id)

    def test_int_id_returns_expected_value(self):
        i = IndividualFactory(institution='MSK')
        self.assertEqual(i.int_id, str(i.pk + 100000))

    def test_str_returns_slug(self):
        i = IndividualFactory(institution='MSK', species='H', ext_id='1')
        slug = "-".join([i.check_institution(), i.species, i.int_id])
        self.assertEqual(slug, i.__str__())

    def test_if_new_initializes_specimens_created_with_zero(self):
        self.assertEqual(IndividualFactory().specimens_created, 0)

    def test_ext_id_uses_validator(self):
        i = IndividualFactory(ext_id="1234 % ''10")
        with self.assertRaises(ValidationError):
            i.full_clean()

    def test_get_absolute_url(self):
        i = IndividualFactory()
        slug = i.slug
        url = reverse(constants.APP_NAME + ':detail', kwargs={'slug': slug})
        self.assertEqual(url, i.get_absolute_url())

    def test_get_update_url(self):
        i = IndividualFactory()
        slug = i.slug
        url = reverse(constants.APP_NAME + ':update', kwargs={'slug': slug})
        self.assertEqual(url, i.get_update_url())
