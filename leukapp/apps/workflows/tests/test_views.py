# -*- coding: utf-8 -*-

# django imports
from django.test import TestCase, RequestFactory

# leukapp
from leukapp.apps.core.tests.test_views import LeukappViewsTest

# local imports
from .. import views
from .. import constants
from ..factories import WorkflowFactory


class WorkflowViewsTest(LeukappViewsTest, TestCase):

    """ See LeukappViewsTest for more information. """

    # factories
    objectfactory = WorkflowFactory
    requestfactory = RequestFactory()

    # views
    listview = views.WorkflowListView
    createview = views.WorkflowCreateView
    updateview = views.WorkflowUpdateView
    redirectview = views.WorkflowRedirectView

    # fields
    CREATE_FIELDS = constants.WORKFLOW_CREATE_FIELDS
    UPDATE_FIELDS = constants.WORKFLOW_UPDATE_FIELDS

    # urls
    URL = 'fake/url'
    LIST_URL = constants.WORKFLOW_LIST_URL
    CREATE_URL = constants.WORKFLOW_CREATE_URL

    # permissions
    createpermissions = constants.WORKFLOW_CREATE_PERMISSIONS
    updatepermissions = constants.WORKFLOW_UPDATE_PERMISSIONS

    # APP Info and messages
    APP_NAME = constants.APP_NAME
    SUCCESS_MESSAGE = constants.SUCCESS_MESSAGE
