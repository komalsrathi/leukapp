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

# django
from django.core.urlresolvers import reverse
from django.views.generic import \
    DetailView, ListView, RedirectView, UpdateView, CreateView

# third party
from braces.views import LoginRequiredMixin

# local
from .models import Aliquot
from . import constants


class AliquotDetailView(LoginRequiredMixin, DetailView):

    """
    Render a "detail" view of an object. By default this is a model instance
    looked up from `self.queryset`, but the view will support display of *any*
    object by overriding `self.get_object()`.
    See: http://ccbv.co.uk/DetailView/
    """

    model = Aliquot


class AliquotListView(LoginRequiredMixin, ListView):

    """
    Render some list of objects, set by `self.model` or `self.queryset`.
    `self.queryset` can actually be any iterable of items, not just a queryset.
    See: http://ccbv.co.uk/ListView/
    """

    model = Aliquot

    def get_context_data(self, **kwargs):
            context = super(AliquotListView, self).get_context_data(**kwargs)

            # Add new context
            context['APP_NAME'] = constants.APP_NAME
            context['CREATE_URL'] = constants.ALIQUOT_CREATE_URL
            return context


class AliquotRedirectView(LoginRequiredMixin, RedirectView):

    """
    A view that provides a redirect on any GET request.
    See: http://ccbv.co.uk/RedirectView/
    """

    permanent = False

    def get_redirect_url(self):
        return reverse(constants.ALIQUOT_LIST_URL)


class AliquotCreateView(LoginRequiredMixin, CreateView):

    """
    View for creating a new object, with a response rendered by template.
    See: http://ccbv.co.uk/CreateView/
    """

    model = Aliquot
    fields = constants.ALIQUOT_CREATE_FIELDS
    succes_msg = "Aliquot Created!"


class AliquotUpdateView(LoginRequiredMixin, UpdateView):

    """
    View for updating an object, with a response rendered by template.
    See: http://ccbv.co.uk/UpdateView/
    """

    model = Aliquot
    fields = constants.ALIQUOT_UPDATE_FIELDS
    succes_msg = "Aliquot Updated!"