# -*- coding: utf-8 -*-

"""
Most of these views inherits from Django's `Class Based Views`. See:
    • https://docs.djangoproject.com/en/1.8/topics/class-based-views/
    • http://ccbv.co.uk/projects/Django/1.8/
    • http://www.pydanny.com/stay-with-the-django-cbv-defaults.html
    • http://www.pydanny.com/tag/class-based-views.html

The `LoginRequiredMixin` is also used:
    • http://django-braces.readthedocs.org/en/latest/access.html
"""

# python
from __future__ import absolute_import, unicode_literals
import csv

# django
from django.views.decorators.cache import never_cache
from django.template.defaulttags import register
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic import \
    DetailView, ListView, RedirectView, UpdateView, CreateView

# third party
from braces.views import LoginRequiredMixin

# local
from .models import Leukform
from . import constants


class LeukformDetailView(LoginRequiredMixin, DetailView):

    """
    Render a "detail" view of an object. By default this is a model instance
    looked up from `self.queryset`, but the view will support display of *any*
    object by overriding `self.get_object()`.
    See: http://ccbv.co.uk/DetailView/
    """

    model = Leukform

    def get_context_data(self, **kwargs):
        super_function = super(LeukformDetailView, self).get_context_data
        context = super_function(**kwargs)

        obj = self.get_object()
        path = obj.result.file.name
        with open(path, 'r') as result:
            reader = csv.reader(result)
            columns = list(next(reader))
            result.seek(0)
            result = list(csv.DictReader(result, delimiter=","))

        context['MODELS'] = constants.MODELS_LIST
        context['COLUMNS'] = columns
        context['RESULT'] = result
        context['SUMMARY'] = eval(obj.summary)
        context['SUMMARY_COLS'] = ['valid', 'existed', 'rejected']
        context['APP_NAME'] = constants.APP_NAME
        context['CREATE_URL'] = constants.LEUKFORM_CREATE_URL
        return context


class LeukformListView(LoginRequiredMixin, ListView):

    """
    Render some list of objects, set by `self.model` or `self.queryset`.
    `self.queryset` can actually be any iterable of items, not just a queryset.
    See: http://ccbv.co.uk/ListView/
    """

    model = Leukform
    paginated_by = 20

    def get_context_data(self, **kwargs):
        context = super(LeukformListView, self).get_context_data(**kwargs)
        context['APP_NAME'] = constants.APP_NAME
        context['CREATE_URL'] = constants.LEUKFORM_CREATE_URL
        return context

    def get_queryset(self):
        return Leukform.objects.filter(created_by=self.request.user)


class LeukformRedirectView(LoginRequiredMixin, RedirectView):

    """
    A view that provides a redirect on any GET request.
    See: http://ccbv.co.uk/RedirectView/
    """

    permanent = False

    def get_redirect_url(self):
        return reverse(constants.LEUKFORM_LIST_URL)


class LeukformCreateView(LoginRequiredMixin, CreateView):

    """
    View for creating a new object, with a response rendered by template.
    See: http://ccbv.co.uk/CreateView/
    """

    model = Leukform
    fields = constants.LEUKFORM_CREATE_FIELDS
    succes_msg = "Leukform Created!"

    def form_valid(self, form):
        """ Add created_by to form """
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.save()
        return super(LeukformCreateView, self).form_valid(form)


class LeukformUpdateView(LoginRequiredMixin, UpdateView):

    """
    View for updating an object, with a response rendered by template.
    See: http://ccbv.co.uk/UpdateView/
    """

    model = Leukform
    fields = constants.LEUKFORM_UPDATE_FIELDS
    succes_msg = "Leukform Updated!"


def download_result(request, slug):
    """ FBV to download leukform results """
    leukform = Leukform.objects.get(slug=slug)
    filename = leukform.result.name.split('/')[-1]
    response = HttpResponse(leukform.result, content_type='text/csv')
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


# -----------------------------------------------------------------------------
# HELPER FUNCTIONS

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
