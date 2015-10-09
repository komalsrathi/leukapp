# django imports
from django.test import TestCase
from django.core.urlresolvers import reverse

# local imports
from .. import views
from .. import constants


class SpecimensViewsTest(TestCase):

    def test_specimen_list_view_adds_app_name_to_context(self):
        view = views.SpecimenListView()

        # initiialize object_list
        view.object_list = []

        context = view.get_context_data()
        self.assertEqual(context["APP_NAME"], constants.APP_NAME)

    def test_specimen_list_view_adds_create_url_to_context(self):
        view = views.SpecimenListView()

        # initiialize object_list
        view.object_list = []

        context = view.get_context_data()
        url = constants.SPECIMEN_CREATE_URL
        self.assertEqual(context["CREATE_URL"], url)

    def test_redirect_view(self):
        view = views.SpecimenRedirectView()

        url = reverse(constants.SPECIMEN_LIST_URL)
        self.assertEqual(url, view.get_redirect_url())

    def test_create_view_fields(self):
        view = views.SpecimenCreateView()

        fields = constants.SPECIMEN_CREATE_FIELDS
        self.assertEqual(fields, view.fields)

    def test_update_view_fields(self):
        view = views.SpecimenUpdateView()

        fields = constants.SPECIMEN_UPDATE_FIELDS
        self.assertEqual(fields, view.fields)
