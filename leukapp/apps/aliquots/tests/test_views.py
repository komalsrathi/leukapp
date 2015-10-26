# -*- coding: utf-8 -*-

# django imports
from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse

# leukapp
from leukapp.apps.users.factories import UserFactory

# local imports
from .. import views
from .. import constants


class AliquotsViewsTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = UserFactory()

    def test_aliquot_list_view_adds_app_name_to_context(self):
        request = self.factory.get(reverse(constants.APP_NAME + ':list'))
        request.user = self.user
        view = views.AliquotListView.as_view()
        response = view(request)
        self.assertEqual(response.context_data["APP_NAME"], constants.APP_NAME)

    def test_aliquot_list_view_adds_create_url_to_context(self):
        request = self.factory.get(reverse(constants.APP_NAME + ':list'))
        request.user = self.user
        view = views.AliquotListView.as_view()
        response = view(request)
        url = constants.ALIQUOT_CREATE_URL
        self.assertEqual(response.context_data["CREATE_URL"], url)

    def test_redirect_view(self):
        view = views.AliquotRedirectView()
        url = reverse(constants.ALIQUOT_LIST_URL)
        self.assertEqual(url, view.get_redirect_url())

    def test_create_view_fields(self):
        view = views.AliquotCreateView()
        fields = constants.ALIQUOT_CREATE_FIELDS
        self.assertEqual(fields, view.fields)

    def test_update_view_fields(self):
        view = views.AliquotUpdateView()
        fields = constants.ALIQUOT_UPDATE_FIELDS
        self.assertEqual(fields, view.fields)
