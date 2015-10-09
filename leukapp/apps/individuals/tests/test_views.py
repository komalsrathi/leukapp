# django imports
from django.test import TestCase
from django.core.urlresolvers import reverse

# local imports
from .. import views
from .. import constants


class IndividualsViewsTest(TestCase):

    def test_individual_list_view_adds_app_name_to_context(self):
        view = views.IndividualListView()

        # initiialize object_list
        view.object_list = []

        context = view.get_context_data()
        self.assertEqual(context["APP_NAME"], constants.APP_NAME)

    def test_individual_list_view_adds_create_url_to_context(self):
        view = views.IndividualListView()

        # initiialize object_list
        view.object_list = []

        context = view.get_context_data()
        url = constants.INDIVIDUAL_CREATE_URL
        self.assertEqual(context["CREATE_URL"], url)

    def test_redirect_view(self):
        view = views.IndividualRedirectView()

        url = reverse(constants.INDIVIDUAL_LIST_URL)
        self.assertEqual(url, view.get_redirect_url())
