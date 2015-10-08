# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import \
    DetailView, ListView, RedirectView, UpdateView, CreateView

from braces.views import LoginRequiredMixin

from .models import Individual
from .constants import \
    APP_NAME, CREATE_URL, LIST_URL, CREATE_FIELDS, UPDATE_FIELDS


class IndividualDetailView(LoginRequiredMixin, DetailView):
    model = Individual


class IndividualListView(LoginRequiredMixin, ListView):
    model = Individual

    def get_context_data(self, **kwargs):
            context = super(
                IndividualListView, self).get_context_data(**kwargs)

            # Add new context
            context['APP_NAME'] = APP_NAME
            context['CREATE_URL'] = CREATE_URL
            context['LIST_URL'] = LIST_URL
            return context


class IndividualRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse(APP_NAME + ":detail",
                       kwargs={"slug": self.request.object.slug})


class IndividualCreateView(LoginRequiredMixin, CreateView):

    # we already imported Individual in the view code above, remember?
    model = Individual
    fields = CREATE_FIELDS
    succes_msg = "Individual Created!"


class IndividualUpdateView(LoginRequiredMixin, UpdateView):

    # we already imported Individual in the view code above, remember?
    model = Individual
    fields = UPDATE_FIELDS
    succes_msg = "Individual Updated!"
