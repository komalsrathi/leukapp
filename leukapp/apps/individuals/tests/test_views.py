# -*- coding: utf-8 -*-

# django imports
from django.test import TestCase, RequestFactory

# leukapp
from leukapp.apps.core.tests.test_views import LeukappViewsTest

# local imports
from .. import views
from .. import constants
from ..factories import IndividualFactory


class IndividualViewsTest(LeukappViewsTest, TestCase):

    """ See LeukappViewsTest for more information. """

    # factories
    objectfactory = IndividualFactory
    requestfactory = RequestFactory()

    # views
    listview = views.IndividualListView
    createview = views.IndividualCreateView
    updateview = views.IndividualUpdateView
    redirectview = views.IndividualRedirectView

    # fields
    CREATE_FIELDS = constants.INDIVIDUAL_CREATE_FIELDS
    UPDATE_FIELDS = constants.INDIVIDUAL_UPDATE_FIELDS

    # urls
    URL = 'fake/url'
    LIST_URL = constants.INDIVIDUAL_LIST_URL
    CREATE_URL = constants.INDIVIDUAL_CREATE_URL

    # permissions
    createpermissions = constants.INDIVIDUAL_CREATE_PERMISSIONS
    updatepermissions = constants.INDIVIDUAL_UPDATE_PERMISSIONS

    # APP Info and messages
    APP_NAME = constants.APP_NAME
    SUCCESS_MESSAGE = constants.SUCCESS_MESSAGE
