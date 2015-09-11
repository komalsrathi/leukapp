from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from ..views import lists_page

# Create your tests here.


class ListsPageTest(TestCase):

    def test_root_url_resolves_to_lists_page_view(self):
        found = resolve('/lists/')
        self.assertEqual(found.func, lists_page)

    def test_lists_page_returns_correct_html(self):
        request = HttpRequest()
        response = lists_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
