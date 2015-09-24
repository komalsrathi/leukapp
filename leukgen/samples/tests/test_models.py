# django imports
from django.test import TestCase

# local imports
from ..models import Individual


class IndividualsTest(TestCase):

    """docstring for IndividualTest"""

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
