# -*- coding: utf-8 -*-

# python
import json

# django imports
from django.test import TestCase, RequestFactory

# leukapp
from leukapp.apps.core.tests.test_views import LeukappViewsTest

# local imports
from .. import views
from .. import constants
from ..factories import ParticipantFactory
from ..forms import ParticipantForm


class ParticipantViewsTest(LeukappViewsTest, TestCase):

    """ See LeukappViewsTest for more information. """

    # factories
    objectfactory = ParticipantFactory
    requestfactory = RequestFactory()

    # views
    listview = views.ParticipantListView
    createview = views.ParticipantCreateView
    updateview = views.ParticipantUpdateView
    redirectview = views.ParticipantRedirectView

    # fields
    CREATE_FIELDS = constants.PARTICIPANT_CREATE_FIELDS
    UPDATE_FIELDS = constants.PARTICIPANT_UPDATE_FIELDS

    # urls
    URL = 'fake/url'
    LIST_URL = constants.PARTICIPANT_LIST_URL
    CREATE_URL = constants.PARTICIPANT_CREATE_URL

    # permissions
    createpermissions = constants.PARTICIPANT_CREATE_PERMISSIONS
    updatepermissions = constants.PARTICIPANT_UPDATE_PERMISSIONS

    # APP Info and messages
    APP_NAME = constants.APP_NAME
    SUCCESS_MESSAGE = constants.SUCCESS_MESSAGE

    def test_search_participant(self):
        """
        search_participant must return a JsonResponse with a list of results
        """
        p = ParticipantFactory()
        request = self.requestfactory.get(self.URL)
        request.GET = request.GET.copy()
        request.GET['q'] = p.email[:2]
        expected = [{'id': str(p.pk), 'name': p.email}]
        obtained = views.search_participant(request).content.decode("utf-8")
        obtained = json.loads(obtained)
        self.assertCountEqual(expected, obtained)

    def test_create_modal_has_correct_form(self):
        """
        CreateModalView must have ParticipantForm as form_class
        """
        view = views.ParticipantCreateModal()
        self.assertEqual(view.form_class, ParticipantForm)
