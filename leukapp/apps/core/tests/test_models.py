# -*- coding: utf-8 -*-

# python
import time

# django
from django.utils import timezone
from django.test import TestCase

# local
from ..models import LeukappTestModel


class BehaviorTestCaseMixin(object):

    def get_model(self):
            return getattr(self, 'model')

    def create_instance(self, **kwargs):
        raise NotImplementedError("Implement me")


class TimeStampedModelTest(BehaviorTestCaseMixin):

    def test_saving_and_retrieving_timestampedmodels(self):
        first_timestamped = self.create_instance()
        self.assertIn(first_timestamped, self.model.objects.all())

    def test_create_date_is_correct(self):
        first_timestamped = self.create_instance()
        self.assertTrue(first_timestamped.created <= timezone.now())

    def test_modified_date_works_correctly(self):
        first_timestamped = self.create_instance()
        time.sleep(0.01)
        first_timestamped.save()
        diff = first_timestamped.modified - first_timestamped.created
        self.assertTrue(diff.total_seconds() >= 0.01)


class LeukappTestModelTest(TimeStampedModelTest, TestCase):

    # required due to ModelMixin
    # http://blog.kevinastone.com/django-model-behaviors.html
    model = LeukappTestModel

    # required due to ModelMixin, see:
    # http://blog.kevinastone.com/django-model-behaviors.html
    def create_instance(self, **kwargs):
        return self.model.objects.create(**kwargs)

    def test_check_if_caller_is_if_new_raises_error(self):
        """
        Must raise error if calling _test outside the _if_new method.
        """
        msg = "This function can only be called from _if_new()."
        with self.assertRaisesMessage(Exception, expected_message=msg):
            self.create_instance()._test()

    def test_check_if_caller_is_save_raises_error(self):
        """
        Must raise error if calling _if_new outside the save method.
        """
        msg = "This function can only be called from save()."
        with self.assertRaisesMessage(Exception, expected_message=msg):
            self.create_instance()._if_new()
