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
            'bio_source': constants.DNA
            }
        with self.assertRaises(IntegrityError):
            AliquotFactory(**kw)
            Aliquot.objects.create(**kw)

    def test_if_aliquots_counters_keep_count_correctly(self):
        s = SpecimenFactory()
        for i in range(3):
            AliquotFactory(specimen=s, bio_source=constants.DNA)
        for i in range(2):
            AliquotFactory(specimen=s, bio_source=constants.RNA)
        self.assertEqual(3, s.dna_count)
        self.assertEqual(2, s.rna_count)

    def test_if_aliquots_created_is_correct_after_delete_aliquots(self):
        s = SpecimenFactory()
        for i in range(3):
            AliquotFactory(specimen=s, bio_source=constants.DNA).delete()
            AliquotFactory(specimen=s, bio_source=constants.RNA).delete()
        self.assertEqual(3, s.dna_count)
        self.assertEqual(3, s.rna_count)

    def test_int_id_returns_expected_value(self):
        s = SpecimenFactory()
        ad = AliquotFactory(specimen=s, bio_source=constants.DNA)
        ar = AliquotFactory(specimen=s, bio_source=constants.RNA)
        ad_int_id = constants.LEUKID_BIO_SOURCE[ad.bio_source]
        ad_int_id += str(s.dna_count)
        ar_int_id = constants.LEUKID_BIO_SOURCE[ar.bio_source]
        ar_int_id += str(s.rna_count)
        self.assertEqual(ad.int_id, ad_int_id)
        self.assertEqual(ar.int_id, ar_int_id)

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
        self.assertEqual(a.runs_count, 0)
