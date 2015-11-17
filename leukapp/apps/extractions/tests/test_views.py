# -*- coding: utf-8 -*-

# django imports
from django.test import TestCase, RequestFactory

# leukapp
from leukapp.apps.core.tests.test_views import LeukappViewsTest

# local imports
from .. import views
from .. import constants
from ..factories import ExtractionFactory


class ExtractionViewsTest(LeukappViewsTest, TestCase):

    """ See LeukappViewsTest for more information. """

    # factories
    objectfactory = ExtractionFactory
    requestfactory = RequestFactory()

    # views
    listview = views.ExtractionListView
    createview = views.ExtractionCreateView
    updateview = views.ExtractionUpdateView
    redirectview = views.ExtractionRedirectView

    # fields
    CREATE_FIELDS = constants.EXTRACTION_CREATE_FIELDS
    UPDATE_FIELDS = constants.EXTRACTION_UPDATE_FIELDS

    # urls
    URL = 'fake/url'
    LIST_URL = constants.EXTRACTION_LIST_URL
    CREATE_URL = constants.EXTRACTION_CREATE_URL

    # permissions
    createpermissions = constants.EXTRACTION_CREATE_PERMISSIONS
    updatepermissions = constants.EXTRACTION_UPDATE_PERMISSIONS

    # APP Info and messages
    APP_NAME = constants.APP_NAME
    SUCCESS_MESSAGE = constants.SUCCESS_MESSAGE
