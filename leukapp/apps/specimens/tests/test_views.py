# -*- coding: utf-8 -*-

# django imports
from django.test import TestCase, RequestFactory

# leukapp
from leukapp.apps.core.tests.test_views import LeukappViewsTest

# local imports
from .. import views
from .. import constants
from ..factories import SpecimenFactory


class SpecimenViewsTest(LeukappViewsTest, TestCase):

    """ See LeukappViewsTest for more information. """

    # factories
    objectfactory = SpecimenFactory
    requestfactory = RequestFactory()

    # views
    listview = views.SpecimenListView
    createview = views.SpecimenCreateView
    updateview = views.SpecimenUpdateView
    redirectview = views.SpecimenRedirectView

    # fields
    CREATE_FIELDS = constants.SPECIMEN_CREATE_FIELDS
    UPDATE_FIELDS = constants.SPECIMEN_UPDATE_FIELDS

    # urls
    URL = 'fake/url'
    LIST_URL = constants.SPECIMEN_LIST_URL
    CREATE_URL = constants.SPECIMEN_CREATE_URL

    # permissions
    createpermissions = constants.SPECIMEN_CREATE_PERMISSIONS
    updatepermissions = constants.SPECIMEN_UPDATE_PERMISSIONS

    # APP Info and messages
    APP_NAME = constants.APP_NAME
    SUCCESS_MESSAGE = constants.SUCCESS_MESSAGE
