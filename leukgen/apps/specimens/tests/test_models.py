# django imports
from django.test import TestCase
from django.db.utils import IntegrityError
from django.utils.translation import ugettext_lazy as _

# apps imports
from core.tests.test_models import TimeStampedModelTest
from individuals import Individual

# local imports
from ..models import Specimen


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
