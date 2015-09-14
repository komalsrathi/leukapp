from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from ..views import home_page

# Create your tests here.


class ListsPageTest(TestCase):

    def test_root_url_resolves_to_lists_page_view(self):
        found = resolve('/lists/')
        self.assertEqual(found.func, home_page)

    def test_lists_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('lists/list_home.html')
        self.assertEqual(response.content.decode(), expected_html)
        self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))
