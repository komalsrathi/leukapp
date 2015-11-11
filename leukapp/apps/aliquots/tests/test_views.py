# -*- coding: utf-8 -*-

# django imports
from django.test import TestCase, RequestFactory

# leukapp
from leukapp.apps.core.tests.test_views import LeukappViewsTest

# local imports
from .. import views
from .. import constants
from ..factories import AliquotFactory


class AliquotViewsTest(LeukappViewsTest, TestCase):

    """ See LeukappViewsTest for more information. """

    # factories
    objectfactory = AliquotFactory
    requestfactory = RequestFactory()

    # views
    listview = views.AliquotListView
    createview = views.AliquotCreateView
    updateview = views.AliquotUpdateView
    redirectview = views.AliquotRedirectView

    # fields
    CREATE_FIELDS = constants.ALIQUOT_CREATE_FIELDS
    UPDATE_FIELDS = constants.ALIQUOT_UPDATE_FIELDS

    # urls
    URL = 'fake/url'
    LIST_URL = constants.ALIQUOT_LIST_URL
    CREATE_URL = constants.ALIQUOT_CREATE_URL

    # permissions
    createpermissions = constants.ALIQUOT_CREATE_PERMISSIONS
    updatepermissions = constants.ALIQUOT_UPDATE_PERMISSIONS

    # APP Info and messages
    APP_NAME = constants.APP_NAME
    SUCCESS_MESSAGE = constants.SUCCESS_MESSAGE
