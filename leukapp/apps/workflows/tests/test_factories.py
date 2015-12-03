# -*- coding: utf-8 -*-

"""
Tests for mod:`workflows.factories`.
"""

# django
from django.test import TestCase

# local
from ..models import Workflow
from ..factories import WorkflowFactory
from .. import constants


class WorkflowFactoriesTest(TestCase):

    """
    Tests for mod:`workflows.factories`.
    """

    def test_extractionfactory_creates_extraction(self):
        """
        WorkflowFactory must create instance correctly.
        """
        a = WorkflowFactory()
        b = Workflow.objects.get(pk=a.pk)
        self.assertEqual(a, b)

    def test_extractionfactory_doesnt_create_existing_extraction(self):
        e, kwargs = WorkflowFactory(), {}
        for field in constants.WORKFLOW_CREATE_FIELDS:
            kwargs[field] = getattr(e, field)
        self.assertEqual(e, WorkflowFactory(**kwargs))

    def test_extractionfactory_does_create_extraction(self):
        e, kwargs = WorkflowFactory(ext_id=None), {}
        for field in constants.WORKFLOW_CREATE_FIELDS:
            kwargs[field] = getattr(e, field)
        self.assertNotEqual(e, Workflow.objects.create(**kwargs))

    def test_extractionfactory_attributes_are_correct(self):
        """
        Instance attributes must have correct choices.
        """
        a = WorkflowFactory()
        self.assertEqual(len(a.ext_id), 12)
        self.assertIn(
            a.sequencing_center, [e[0] for e in constants.CENTER])
        self.assertIn(
            a.sequencing_technology, [e[0] for e in constants.TECHNOLOGY])
        self.assertIn(
            a.technology_type, [e[0] for e in constants.TECHNOLOGY_TYPE])
        self.assertIn(
            a.sequencing_platform, [e[0] for e in constants.PLATFORM])
        self.assertIn(
            a.read_length, [e[0] for e in constants.READ_LENGTH])
        self.assertIn(
            a.read_type, [e[0] for e in constants.READ_TYPE])
