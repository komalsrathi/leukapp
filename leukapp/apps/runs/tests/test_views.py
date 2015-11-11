# -*- coding: utf-8 -*-

# django imports
from django.test import TestCase, RequestFactory

# leukapp
from leukapp.apps.core.tests.test_views import LeukappViewsTest

# local imports
from .. import views
from .. import constants
from ..factories import RunFactory


class RunViewsTest(LeukappViewsTest, TestCase):

    """ See LeukappViewsTest for more information. """

    # factories
    objectfactory = RunFactory
    requestfactory = RequestFactory()

    # views
    listview = views.RunListView
    createview = views.RunCreateView
    updateview = views.RunUpdateView
    redirectview = views.RunRedirectView

    # fields
    CREATE_FIELDS = constants.RUN_CREATE_FIELDS
    UPDATE_FIELDS = constants.RUN_UPDATE_FIELDS

    # urls
    URL = 'fake/url'
    LIST_URL = constants.RUN_LIST_URL
    CREATE_URL = constants.RUN_CREATE_URL

    # permissions
    createpermissions = constants.RUN_CREATE_PERMISSIONS
    updatepermissions = constants.RUN_UPDATE_PERMISSIONS

    # APP Info and messages
    APP_NAME = constants.APP_NAME
    SUCCESS_MESSAGE = constants.SUCCESS_MESSAGE
