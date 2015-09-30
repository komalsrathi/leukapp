# django imports
from django.test import TestCase
from django.db.utils import IntegrityError
from django.utils.translation import ugettext_lazy as _

# apps imports
from core.tests.test_models import TimeStampedModelTest

# local imports
from ..models import Individual


class IndividualModelTest(TimeStampedModelTest, TestCase):

    # required due to ModelMixin
    # http://blog.kevinastone.com/django-model-behaviors.html
    model = Individual

    # required due to ModelMixin, see:
    # http://blog.kevinastone.com/django-model-behaviors.html
    def create_instance(self, **kwargs):
        return Individual.objects.create(**kwargs)

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
        saved_individuals = Individual.objects.all()
        self.assertEqual(saved_individuals.count(), 2)

        first_saved_individual = saved_individuals[0]
        second_saved_individual = saved_individuals[1]
        self.assertEqual(first_saved_individual.institution, "MSK")
        self.assertEqual(first_saved_individual.species, "H")
        self.assertEqual(first_saved_individual.ext_id, "12345678910")
        self.assertEqual(second_saved_individual.institution, "O")
        self.assertEqual(second_saved_individual.species, "M")
        self.assertEqual(second_saved_individual.ext_id, "1234567891K")

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
        self.assertEqual(int_id, self.individual_a.int_id())

    def test_institution_verbose_name(self):
        verbose_name = \
            Individual._meta.get_field_by_name('institution')[0].verbose_name
        self.assertEqual(verbose_name, _("Source Institution"))

    def test_str_returns_int_id(self):
        int_id = \
            self.individual_a.species + "-" + self.individual_a.int_id()
        self.assertEqual(int_id, self.individual_a.__str__())
