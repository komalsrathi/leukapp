# -*- coding: utf-8 -*-

# django
from django.test import TestCase
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

# leukapp
from leukapp.apps.aliquots.utils import AliquotFactory

# local
from ..utils import SampleFactory
from ..models import Sample
from .. import constants


class SamplesModelTest(TestCase):

    def test_saving_and_retrieving_samples(self):
        s = SampleFactory()
        samples = Sample.objects.all()
        self.assertEqual(samples.count(), 1)
        self.assertEqual(samples[0], s)

    def test_ext_id_uses_validator(self):
        with self.assertRaises(ValidationError):
            SampleFactory(ext_id="1234 % ''10").full_clean()

    def test_unique_together_functionality(self):
        s = SampleFactory()
        with self.assertRaises(IntegrityError):
            Sample.objects.create(aliquot=s.aliquot, ext_id=s.ext_id)

    def test_if_new_adds_one_to_aliquots_samples_created(self):
        self.assertEqual(1, SampleFactory().aliquot.samples_created)

    def test_if_aliquots_created_keep_count_correctly(self):
        a = AliquotFactory()
        SampleFactory(aliquot=a)
        SampleFactory(aliquot=a)
        self.assertEqual(2, a.samples_created)

    def test_if_aliquots_created_is_correct_after_delete_aliquots(self):
        a = AliquotFactory()
        SampleFactory(aliquot=a).delete()
        SampleFactory(aliquot=a).delete()
        SampleFactory(aliquot=a).delete()
        self.assertEqual(3, a.samples_created)

    def test_int_id_returns_expected_value(self):
        a = AliquotFactory()
        s = SampleFactory(aliquot=a)
        int_id = str(a.samples_created)
        self.assertEqual(s.int_id, int_id)

    def test_str_returns_slug(self):
        s = SampleFactory()
        slug = '-'.join([s.int_id])
        self.assertEqual(slug, s.__str__())

    def test_get_absolute_url(self):
        s = SampleFactory()
        slug = s.slug
        url = reverse(constants.APP_NAME + ':detail', kwargs={'slug': slug})
        self.assertEqual(url, s.get_absolute_url())

    def test_get_update_url(self):
        s = SampleFactory()
        slug = s.slug
        url = reverse(constants.APP_NAME + ':update', kwargs={'slug': slug})
        self.assertEqual(url, s.get_update_url())
