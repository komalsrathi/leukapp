# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import \
    DetailView, ListView, RedirectView, UpdateView, CreateView

from braces.views import LoginRequiredMixin

from .models import Specimen
from .constants import \
    APP_NAME, CREATE_URL, LIST_URL, CREATE_FIELDS, UPDATE_FIELDS


class SpecimenDetailView(LoginRequiredMixin, DetailView):
    model = Specimen


class SpecimenListView(LoginRequiredMixin, ListView):
    model = Specimen

    def get_context_data(self, **kwargs):
            context = super(
                SpecimenListView, self).get_context_data(**kwargs)

            # Add new context
            context['APP_NAME'] = APP_NAME
            context['CREATE_URL'] = CREATE_URL
            context['LIST_URL'] = LIST_URL
            return context


class SpecimenRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse(APP_NAME + ":detail",
                       kwargs={"slug": self.request.object.slug})


class SpecimenCreateView(LoginRequiredMixin, CreateView):

    # we already imported Specimen in the view code above, remember?
    model = Specimen
    fields = CREATE_FIELDS
    succes_msg = "Specimen Created!"


class SpecimenUpdateView(LoginRequiredMixin, UpdateView):

    # we already imported Specimen in the view code above, remember?
    model = Specimen
    fields = UPDATE_FIELDS
    succes_msg = "Specimen Created!"
