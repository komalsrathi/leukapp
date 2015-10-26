# -*- coding: utf-8 -*-

# django
from django.test import TestCase
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

# leukapp
from leukapp.apps.aliquots.factories import AliquotFactory

# local
from ..utils import RunFactory
from ..models import Run
from .. import constants


class RunsModelTest(TestCase):

    def test_saving_and_retrieving_runs(self):
        s = RunFactory()
        runs = Run.objects.all()
        self.assertEqual(runs.count(), 1)
        self.assertEqual(runs[0], s)

    def test_ext_id_uses_validator(self):
        with self.assertRaises(ValidationError):
            RunFactory(ext_id="1234 % ''10").full_clean()

    def test_unique_together_functionality(self):
        s = RunFactory()
        with self.assertRaises(IntegrityError):
            Run.objects.create(aliquot=s.aliquot, ext_id=s.ext_id)

    def test_if_runs_count_keep_count_correctly(self):
        a = AliquotFactory()
        RunFactory(aliquot=a)
        RunFactory(aliquot=a)
        self.assertEqual(2, a.runs_count)

    def test_if_runs_count_is_correct_after_delete_runs(self):
        a = AliquotFactory()
        RunFactory(aliquot=a).delete()
        RunFactory(aliquot=a).delete()
        RunFactory(aliquot=a).delete()
        self.assertEqual(3, a.runs_count)

    def test_int_id_returns_expected_value(self):
        a = AliquotFactory()
        s = RunFactory(aliquot=a)
        int_id = str(a.runs_count)
        self.assertEqual(s.int_id, int_id)

    def test_str_returns_slug(self):
        s = RunFactory()
        slug = '-'.join([s.aliquot.slug, s.int_id])
        self.assertEqual(slug, s.__str__())

    def test_get_absolute_url(self):
        s = RunFactory()
        slug = s.slug
        url = reverse(constants.APP_NAME + ':detail', kwargs={'slug': slug})
        self.assertEqual(url, s.get_absolute_url())

    def test_get_update_url(self):
        s = RunFactory()
        slug = s.slug
        url = reverse(constants.APP_NAME + ':update', kwargs={'slug': slug})
        self.assertEqual(url, s.get_update_url())
