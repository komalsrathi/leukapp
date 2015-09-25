# django imports
from django.test import TestCase
from django.db.utils import IntegrityError

# apps imports
from core.tests.test_models import TimeStampedModelTest

# local imports
from ..models import Individual


class IndividualModelTest(TimeStampedModelTest, TestCase):

    """docstring for IndividualModelTest"""

    # required due to ModelMixin
    # http://blog.kevinastone.com/django-model-behaviors.html
    model = Individual

    # required due to ModelMixin
    def create_instance(self, **kwargs):
        return Individual.objects.create(**kwargs)

    def test_saving_and_retrieving_individuals(self):
        first_individual = Individual()
        first_individual.source = "MSK"
        first_individual.species = "H"
        first_individual.ext_id = "12345678910"
        first_individual.save()

        second_individual = Individual()
        second_individual.source = "O"
        second_individual.species = "M"
        second_individual.ext_id = "1234567891K"
        second_individual.save()

        saved_individuals = Individual.objects.all()
        self.assertEqual(saved_individuals.count(), 2)

        first_saved_individual = saved_individuals[0]
        second_saved_individual = saved_individuals[1]
        self.assertEqual(first_saved_individual.source, "MSK")
        self.assertEqual(first_saved_individual.species, "H")
        self.assertEqual(first_saved_individual.ext_id, "12345678910")
        self.assertEqual(second_saved_individual.source, "O")
        self.assertEqual(second_saved_individual.species, "M")
        self.assertEqual(second_saved_individual.ext_id, "1234567891K")

    def test_if_check_source_method_return_internal(self):
        individual = Individual()
        individual.source = "MSK"
        individual.species = "H"
        individual.ext_id = "12345678910"
        individual.save()

        saved_individuals = Individual.objects.all()
        self.assertEqual(saved_individuals[0].check_source(), 'I')

    def test_if_check_source_method_return_external(self):
        individual = Individual()
        individual.source = "O"
        individual.species = "H"
        individual.ext_id = "12345678910"
        individual.save()

        saved_individuals = Individual.objects.all()
        self.assertEqual(saved_individuals[0].check_source(), 'E')

    def test_unique_together_functionality(self):
        first_individual = Individual()
        first_individual.source = "MSK"
        first_individual.species = "H"
        first_individual.ext_id = "12345678910"
        first_individual.save()

        second_individual = Individual()
        second_individual.source = "MSK"
        second_individual.species = "H"
        second_individual.ext_id = "12345678910"

        with self.assertRaises(IntegrityError):
            second_individual.save()


class SpecimenModelTest(TimeStampedModelTest, TestCase):

    """docstring for SpecimenModelTest"""

    model = Specimen

    def create_instance(self, **kwargs):
        return Individual.objects.create(**kwargs)
