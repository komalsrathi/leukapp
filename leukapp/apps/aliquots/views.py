# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import \
    DetailView, ListView, RedirectView, UpdateView, CreateView

from braces.views import LoginRequiredMixin

from .models import Aliquot
from .constants import \
    APP_NAME, CREATE_URL, LIST_URL, UPDATE_FIELDS, CREATE_FIELDS


class AliquotDetailView(LoginRequiredMixin, DetailView):
    model = Aliquot


class AliquotListView(LoginRequiredMixin, ListView):
    model = Aliquot

    def get_context_data(self, **kwargs):
            context = super(AliquotListView, self).get_context_data(**kwargs)

            # Add new context
            context['APP_NAME'] = APP_NAME
            context['CREATE_URL'] = CREATE_URL
            context['LIST_URL'] = LIST_URL
            return context


class AliquotRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse(APP_NAME + ":detail",
                       kwargs={"slug": self.request.object.slug})


class AliquotCreateView(LoginRequiredMixin, CreateView):

    # we already imported Aliquot in the view code above, remember?
    model = Aliquot
    fields = CREATE_FIELDS
    succes_msg = "Aliquot Created!"


class AliquotUpdateView(LoginRequiredMixin, UpdateView):

    # we already imported Aliquot in the view code above, remember?
    model = Aliquot
    fields = UPDATE_FIELDS
    succes_msg = "Aliquot Updated!"
