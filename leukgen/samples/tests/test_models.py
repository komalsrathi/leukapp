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

    def SetUp(self):
        self.first_individual = Individual()
        self.first_individual.source = "MSK"
        self.first_individual.species = "H"
        self.first_individual.ext_id = "12345678910"
        self.first_individual.save()

        self.second_individual = Individual()
        self.second_individual.source = "O"
        self.second_individual.species = "M"
        self.second_individual.ext_id = "1234567891K"
        self.second_individual.save()

    def test_saving_and_retrieving_individuals(self):
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
        self.assertEqual(self.first_individual.check_source(), 'I')

    def test_if_check_source_method_return_external(self):
        self.assertEqual(self.second_individual.check_source(), 'E')

    def test_unique_together_functionality(self):
        self.second_individual.source = "MSK"
        self.second_individual.species = "H"
        self.second_individual.ext_id = "12345678910"

        with self.assertRaises(IntegrityError):
            self.second_individual.save()


# class SpecimenModelTest(TimeStampedModelTest, TestCase):

#     """docstring for SpecimenModelTest"""

#     model = Specimen

#     def create_instance(self, **kwargs):
#         return Individual.objects.create(**kwargs)
