# django imports
from django.test import TestCase
from django.db.utils import IntegrityError
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

# apps imports
from leukapp.apps.individuals.models import Individual
from leukapp.apps.specimens.models import Specimen

# local imports
from ..models import Aliquot
from .. import constants


class AliquotModelTest(TestCase):

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

        self.aliquot_a = Aliquot.objects.create(
            specimen=self.specimen_a,
            bio_source='D',
            ext_id='123456789',
        )

    def test_saving_and_retrieving_specimens(self):
        saved_aliquots = Aliquot.objects.all()
        self.assertEqual(saved_aliquots.count(), 1)

        first_saved_aliquot = saved_aliquots[0]
        self.assertEqual(first_saved_aliquot.specimen, self.specimen_a)
        self.assertEqual(first_saved_aliquot.bio_source, 'D')
        self.assertEqual(first_saved_aliquot.ext_id, '123456789')

    def test_ext_id_uses_validator(self):
        self.specimen_a.ext_id = "1234 % ''10"

        with self.assertRaises(ValidationError):
            self.specimen_a.full_clean()

    def test_unique_together_functionality(self):
        with self.assertRaises(IntegrityError):
            self.aliquot_b = Aliquot.objects.create(
                specimen=self.specimen_a,
                ext_id='123456789',
            )

    def test_if_new_adds_one_to_specimen_aliquots_created(self):
        self.assertEqual(1, self.specimen_a.aliquots_created)

    def test_if_specimens_created_keep_count_correctly(self):
        self.aliquot_b = Aliquot.objects.create(
            specimen=self.specimen_a,
            bio_source='R',
            ext_id='123456789051',
        )
        self.assertEqual(2, self.specimen_a.aliquots_created)

    def test_if_aliquots_created_is_correct_after_delete_aliquots(self):
        self.aliquot_b = Aliquot.objects.create(
            specimen=self.specimen_a,
            bio_source='R',
            ext_id='123456789051',
        )
        self.aliquot_c = Aliquot.objects.create(
            specimen=self.specimen_a,
            bio_source='R',
            ext_id='123456789054651',
        )
        self.aliquot_b.delete()
        self.aliquot_c.delete()
        self.assertEqual(3, self.specimen_a.aliquots_created)

    def test_int_id_returns_expected_value(self):
        self.aliquot_b = Aliquot.objects.create(
            specimen=self.specimen_a,
            bio_source='R',
            ext_id='123456789051',
        )
        int_id = str(self.specimen_a.aliquots_created)
        self.assertEqual(self.aliquot_b.int_id, int_id)

    def test_str_returns_slug(self):
        slug = '-'.join([
            self.aliquot_a.specimen.slug,
            self.aliquot_a.bio_source,
            self.aliquot_a.int_id
            ])
        self.assertEqual(slug, self.aliquot_a.__str__())

    def test_get_absolute_url(self):
        slug = self.aliquot_a.slug
        url = reverse(constants.APP_NAME + ':detail', kwargs={'slug': slug})
        self.assertEqual(url, self.aliquot_a.get_absolute_url())

    def test_get_update_url(self):
        slug = self.aliquot_a.slug
        url = reverse(constants.APP_NAME + ':update', kwargs={'slug': slug})
        self.assertEqual(url, self.aliquot_a.get_update_url())
