# -*- coding: utf-8 -*-

"""
Tests for workflows models.
"""

# python
from unittest import skipIf

# django
from django.test import TestCase
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

# leukapp
from leukapp.apps.core import constants as coreconstants
from leukapp.apps.extractions.factories import ExtractionFactory
from leukapp.apps.extractions.constants import DNA

# local
from ..factories import WorkflowFactory
from ..models import Workflow
from .. import constants


class WorkflowsModelTest(TestCase):

    def test_saving_and_retrieving_workflows(self):
        w = WorkflowFactory()
        workflows = Workflow.objects.all()
        self.assertEqual(workflows.count(), 1)
        self.assertEqual(workflows[0], w)

    def test_ext_id_uses_validator(self):
        with self.assertRaises(ValidationError):
            WorkflowFactory(ext_id="1234 % ''10").full_clean()

    @skipIf((not constants.WORKFLOW_UNIQUE_TOGETHER), "not unique fields")
    def test_unique_together_functionality(self):
        with self.assertRaises(IntegrityError):
            w, kwargs = WorkflowFactory(), {}
            for field in constants.WORKFLOW_CREATE_FIELDS:
                kwargs[field] = getattr(w, field)
            Workflow.objects.create(**kwargs)

    def test_if_workflows_count_keep_count_correctly(self):
        e = ExtractionFactory()
        for i in range(2):
            WorkflowFactory(extraction=e)
        self.assertEqual(2, e.workflows_count)

    def test_if_workflows_count_is_correct_after_delete_workflows(self):
        e = ExtractionFactory()
        for i in range(2):
            WorkflowFactory(extraction=e).delete()
        self.assertEqual(2, e.workflows_count)

    def test_str_returns_slug(self):
        w = WorkflowFactory()
        slug = '-'.join([w.extraction.slug, w.int_id])
        self.assertEqual(slug, w.__str__())

    def test_get_absolute_url(self):
        w = WorkflowFactory()
        slug = w.slug
        url = reverse(constants.APP_NAME + ':detail', kwargs={'slug': slug})
        self.assertEqual(url, w.get_absolute_url())

    def test_get_update_url(self):
        w = WorkflowFactory()
        slug = w.slug
        url = reverse(constants.APP_NAME + ':update', kwargs={'slug': slug})
        self.assertEqual(url, w.get_update_url())

    def test_int_id_returns_expected_value(self):
        w = WorkflowFactory()
        w_int_id = str(w.extraction.workflows_count) + '-'
        technologies = constants.INT_ID_TECHNOLOGY[w.extraction.analyte]
        technology_types = technologies[w.sequencing_technology]
        technology_code = technology_types[w.technology_type]
        w_int_id += technology_code + '-'
        read_type_code = constants.INT_ID_READ_TYPE[w.read_type]
        read_lentgh_code = constants.INT_ID_READ_LENGTH[w.read_length]
        w_int_id += read_type_code + read_lentgh_code + '-'
        platform_code = constants.INT_ID_PLATFORM[w.sequencing_platform]
        w_int_id += platform_code + '-'
        center_code = constants.INT_ID_CENTER[w.sequencing_center]
        w_int_id += center_code
        self.assertEqual(w.int_id, w_int_id)

    def test_none_technology_type_is_replaced_with_default_value(self):
        w = WorkflowFactory(technology_type=None)
        technologies = constants.INT_ID_TECHNOLOGY[w.extraction.analyte]
        expected = technologies[w.sequencing_technology]["DEFAULT_TECHNOLOGY"]
        self.assertEqual(w.technology_type, expected)

    def test_default_technology_type_is_replaced_with_default_value(self):
        w = WorkflowFactory(technology_type=coreconstants.DEFAULT)
        technologies = constants.INT_ID_TECHNOLOGY[w.extraction.analyte]
        expected = technologies[w.sequencing_technology]["DEFAULT_TECHNOLOGY"]
        self.assertEqual(w.technology_type, expected)

    def test_unique_together_functionality_not_raised_empty_ext_id(self):
        w, kwargs = WorkflowFactory(ext_id=None), {}
        for field in constants.WORKFLOW_CREATE_FIELDS:
            kwargs[field] = getattr(w, field)
        self.assertNotEqual(w, Workflow.objects.create(**kwargs))

    def test_char_null_field_returns_unknown_for_ext_id(self):
        w = WorkflowFactory(ext_id=None)
        w = Workflow.objects.get(pk=w.pk)
        self.assertEqual(w.ext_id, coreconstants.UNKNOWN)

    def test_clean_method(self):
        with self.assertRaises(ValidationError):
            WorkflowFactory(
                sequencing_technology=constants.WHOLEEXOME,
                technology_type=constants.THREEPRIMEEND,
                )
