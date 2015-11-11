# -*- coding: utf-8 -*-

# django imports
from django.test import TestCase, RequestFactory
from django import forms

# leukapp
from leukapp.apps.core.tests.test_views import LeukappViewsTest

# local imports
from .. import views
from .. import constants
from ..factories import ProjectFactory


class ProjectViewsTest(LeukappViewsTest, TestCase):

    """ See LeukappViewsTest for more information. """

    # factories
    objectfactory = ProjectFactory
    requestfactory = RequestFactory()

    # views
    listview = views.ProjectListView
    createview = views.ProjectCreateView
    updateview = views.ProjectUpdateView
    redirectview = views.ProjectRedirectView

    # fields
    CREATE_FIELDS = constants.PROJECT_CREATE_FIELDS
    UPDATE_FIELDS = constants.PROJECT_UPDATE_FIELDS

    # urls
    URL = 'fake/url'
    LIST_URL = constants.PROJECT_LIST_URL
    CREATE_URL = constants.PROJECT_CREATE_URL

    # permissions
    createpermissions = constants.PROJECT_CREATE_PERMISSIONS
    updatepermissions = constants.PROJECT_UPDATE_PERMISSIONS

    # APP Info and messages
    APP_NAME = constants.APP_NAME
    SUCCESS_MESSAGE = constants.SUCCESS_MESSAGE

    def test_update_project_form_widgets(self):
        view = views.ProjectCreateView(request=RequestFactory().get(self.URL))
        form = view.get_form()
        for i in ['pi', 'analyst', 'requestor', 'participants']:
            expected = type(forms.TextInput()).__name__
            obtained = type(form.fields[i].widget).__name__
            self.assertEqual(expected, obtained)
        expected = type(forms.Textarea()).__name__
        obtained = type(form.fields['description'].widget).__name__
        self.assertEqual(expected, obtained)

    def test_clean_participants_in_request(self):
        request = self.requestfactory.post(self.URL)
        request.POST = request.POST.copy()
        request.POST['participants'] = '1,2,3'
        request.POST['pi'] = '31'
        request.POST['analyst'] = '12'
        request.POST['requestor'] = '1'
        request = views.clean_participants_in_request(request)
        obtained = request.POST['participants']
        self.assertCountEqual(obtained, [1, 2, 3, 31, 12, 1])
