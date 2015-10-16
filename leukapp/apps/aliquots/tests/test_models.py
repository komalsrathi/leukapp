# django imports
from django.test import TestCase
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

# apps imports
from leukapp.apps.specimens.factories import SpecimenFactory

# local imports
from ..factories import AliquotFactory
from ..models import Aliquot
from .. import constants


class AliquotModelTest(TestCase):

    def test_saving_and_retrieving_aliquots(self):
        a = AliquotFactory()
        aliquots = Aliquot.objects.all()
        self.assertEqual(aliquots.count(), 1)
        self.assertEqual(aliquots[0], a)

    def test_ext_id_uses_validator(self):
        with self.assertRaises(ValidationError):
            AliquotFactory(ext_id="1234 % ''10").full_clean()

    def test_unique_together_functionality(self):
        kw = {'specimen': SpecimenFactory(), 'ext_id': '1'}
        with self.assertRaises(IntegrityError):
            AliquotFactory(**kw)
            Aliquot.objects.create(**kw)

    def test_if_new_adds_one_to_specimen_aliquots_created(self):
        self.assertEqual(1, AliquotFactory().specimen.aliquots_created)

    def test_if_aliquots_created_keep_count_correctly(self):
        s = SpecimenFactory()
        AliquotFactory(specimen=s)
        AliquotFactory(specimen=s)
        self.assertEqual(2, s.aliquots_created)

    def test_if_aliquots_created_is_correct_after_delete_aliquots(self):
        s = SpecimenFactory()
        AliquotFactory(specimen=s).delete()
        AliquotFactory(specimen=s).delete()
        AliquotFactory(specimen=s).delete()
        self.assertEqual(3, s.aliquots_created)

    def test_int_id_returns_expected_value(self):
        s = SpecimenFactory()
        a = AliquotFactory(specimen=s)
        int_id = str(s.aliquots_created)
        self.assertEqual(a.int_id, int_id)

    def test_str_returns_slug(self):
        a = AliquotFactory()
        slug = '-'.join([a.specimen.slug, a.bio_source, a.int_id])
        self.assertEqual(slug, a.__str__())

    def test_get_absolute_url(self):
        a = AliquotFactory()
        slug = a.slug
        url = reverse(constants.APP_NAME + ':detail', kwargs={'slug': slug})
        self.assertEqual(url, a.get_absolute_url())

    def test_get_update_url(self):
        a = AliquotFactory()
        slug = a.slug
        url = reverse(constants.APP_NAME + ':update', kwargs={'slug': slug})
        self.assertEqual(url, a.get_update_url())

    def test_if_new_initializes_samples_created_with_zero(self):
        a = AliquotFactory()
        self.assertEqual(a.samples_created, 0)
