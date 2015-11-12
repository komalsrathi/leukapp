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
        kw = {
            'specimen': SpecimenFactory(),
            'ext_id': '1',
            }
        with self.assertRaises(IntegrityError):
            AliquotFactory(**kw)
            Aliquot.objects.create(**kw)

    def test_if_aliquots_counters_keep_count_correctly(self):
        s = SpecimenFactory()
        for i in range(3):
            AliquotFactory(specimen=s)
        self.assertEqual(3, s.aliquots_count)

    def test_if_aliquots_created_is_correct_after_delete_aliquots(self):
        s = SpecimenFactory()
        for i in range(3):
            AliquotFactory(specimen=s).delete()
        self.assertEqual(3, s.aliquots_count)

    def test_int_id_returns_expected_value(self):
        s = SpecimenFactory()
        a = AliquotFactory(specimen=s)
        a_int_id = str(s.aliquots_count)
        self.assertEqual(a.int_id, a_int_id)

    def test_str_returns_slug(self):
        a = AliquotFactory()
        slug = '-'.join([a.specimen.slug, a.int_id])
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

    def test__if_new_initializes_runs_count_with_zero(self):
        a = AliquotFactory()
        self.assertEqual(a.dna_runs_count, 0)
        self.assertEqual(a.rna_runs_count, 0)
