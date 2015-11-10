# -*- coding: utf-8 -*-

# django imports
from django.contrib.auth.models import AnonymousUser
from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import Permission

# leukapp
from leukapp.apps.users.factories import UserFactory

# local imports
from .. import views
from .. import constants
from ..factories import IndividualFactory


class ViewsTest(TestCase):

    # factories
    objectfactory = IndividualFactory
    requestfactory = RequestFactory()

    # views
    listview = views.IndividualListView
    createview = views.IndividualCreateView
    updateview = views.IndividualUpdateView
    redirectview = views.IndividualRedirectView
    views = [listview, createview, updateview, redirectview]

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

    def setUp(self):
        self.user = UserFactory()

    def test_list_view_adds_app_name_to_context(self):
        """
        ListView must add APP_NAME and CREATE_URL to context_data
        """
        request = self.requestfactory.get(self.URL)
        request.user = self.user
        view = self.listview.as_view()
        response = view(request)
        self.assertEqual(response.context_data["APP_NAME"], constants.APP_NAME)
        self.assertEqual(response.context_data["CREATE_URL"], self.CREATE_URL)

    def test_redirect_view(self):
        """
        RedirectView must redirect to LIST_URL
        """
        view, url = self.redirectview(), reverse(self.LIST_URL)
        self.assertEqual(url, view.get_redirect_url())

    def test_create_view_fields(self):
        """
        CreateView.fields must be the same as self.CREATE_FIELDS
        """
        view = self.createview
        fields = self.CREATE_FIELDS
        self.assertEqual(fields, view.fields)

    def test_update_view_fields(self):
        """
        UpdateView.fields must be the same as self.UPDATE_FIELDS
        """
        view = self.updateview
        fields = self.UPDATE_FIELDS
        self.assertEqual(fields, view.fields)

    def test_create_view_not_permission(self):
        """
        CreateView raise PermissionDenied if user doesnt have createpermissions
        """
        view = self.createview.as_view()
        request = self.requestfactory.get(self.URL)
        request.user = self.user
        with self.assertRaises(PermissionDenied):
            response = view(request)

    def test_update_view_not_permission(self):
        """
        UpdateView raise PermissionDenied if user doesnt have updatepermissions
        """
        obj = self.objectfactory()
        view = self.updateview.as_view()
        request = self.requestfactory.get(self.URL)
        request.user = self.user
        with self.assertRaises(PermissionDenied):
            response = view(request)

    def test_create_view_not_permission(self):
        """
        CreateView allows users with createpermissions
        """
        for p in self.createpermissions:
            app_label, codename = p.split('.')
            kw = {'content_type__app_label': app_label, 'codename': codename}
            permission = Permission.objects.get(**kw)
            self.user.user_permissions.add(permission)

        view = self.createview.as_view()
        request = self.requestfactory.get(self.URL)
        request.user = self.user
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_update_view_with_permission(self):
        """
        UpdateView allows users with updatepermissions
        """
        for p in self.updatepermissions:
            app_label, codename = p.split('.')
            kw = {'content_type__app_label': app_label, 'codename': codename}
            permission = Permission.objects.get(**kw)
            self.user.user_permissions.add(permission)

        obj = self.objectfactory()
        view = self.updateview.as_view()
        request = self.requestfactory.get(self.URL)
        request.user = self.user
        response = view(request, slug=obj.slug)
        self.assertEqual(response.status_code, 200)
