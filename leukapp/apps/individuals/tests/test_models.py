# django imports
from django.test import TestCase
from django.db.utils import IntegrityError
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

# apps imports
from leukapp.apps.core.tests.test_models import TimeStampedModelTest

# local imports
from ..models import Individual
from .. import constants


class IndividualModelTest(TimeStampedModelTest, TestCase):

    # required due to ModelMixin
    # http://blog.kevinastone.com/django-model-behaviors.html
    model = Individual

    # required due to ModelMixin, see:
    # http://blog.kevinastone.com/django-model-behaviors.html
    def create_instance(self, **kwargs):
        return self.model.objects.create(**kwargs)

    def setUp(self):
        self.object_a = Individual()
        self.object_a.institution = "MSK"
        self.object_a.species = "H"
        self.object_a.ext_id = "12345678910"
        self.object_a.save()

        self.object_b = Individual()
        self.object_b.institution = "O"
        self.object_b.species = "M"
        self.object_b.ext_id = "1234567891K"
        self.object_b.save()

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
        self.assertEqual(self.object_a.check_institution(), 'I')

    def test_check_institution_return_external(self):
        self.assertEqual(self.object_b.check_institution(), 'E')

    def test_unique_together_functionality(self):
        self.object_b.institution = "MSK"
        self.object_b.species = "H"
        self.object_b.ext_id = "12345678910"

        with self.assertRaises(IntegrityError):
            self.object_b.save()

    def test_int_id_returns_expected_value(self):
        int_id = str(self.object_a.pk + 100000)
        self.assertEqual(self.object_a.int_id, int_id)

    def test_institution_verbose_name(self):
        verbose_name = \
            Individual._meta.get_field_by_name('institution')[0].verbose_name
        self.assertEqual(verbose_name, _("individual's institution"))

    def test_str_returns_slug(self):
        leukid = "-".join([
            self.object_a.check_institution(),
            self.object_a.species,
            self.object_a.int_id,
        ])
        self.assertEqual(leukid, self.object_a.__str__())

    def test_if_new_initializes_specimen_count_with_zero(self):
            self.assertEqual(self.object_a.specimens_count, 0)

    def test_ext_id_uses_validator(self):
        self.object_b.institution = "MSK"
        self.object_b.species = "H"
        self.object_b.ext_id = "1234 % ''10"

        with self.assertRaises(ValidationError):
            self.object_b.full_clean()

    def test_get_absolute_url(self):
        slug = self.object_a.slug
        url = reverse(constants.APP_NAME + ':detail', kwargs={'slug': slug})
        self.assertEqual(url, self.object_a.get_absolute_url())

    def test_get_update_url(self):
        slug = self.object_a.slug
        url = reverse(constants.APP_NAME + ':update', kwargs={'slug': slug})
        self.assertEqual(url, self.object_a.get_update_url())
