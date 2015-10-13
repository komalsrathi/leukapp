# -*- coding: utf-8 -*-

# django imports
from django.test import TestCase

# local imports
from .. import utils


class SamplesUtilsTest(TestCase):

    def test_create_samples_batch(self):
        batch = utils.create_samples_batch(10, 2, 2)
        self.assertEqual(len(batch['individuals'], 10)
