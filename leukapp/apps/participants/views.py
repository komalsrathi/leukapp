# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import \
    DetailView, ListView, RedirectView, UpdateView, CreateView

from braces.views import LoginRequiredMixin

from .models import Participant
from .forms import ParticipantForm
from .constants import APP_NAME, CREATE_URL, LIST_URL


class ParticipantDetailView(LoginRequiredMixin, DetailView):
    model = Participant


class ParticipantListView(LoginRequiredMixin, ListView):
    model = Participant

    def get_context_data(self, **kwargs):
            context = super(
                ParticipantListView, self).get_context_data(**kwargs)

            # Add new context
            context['APP_NAME'] = APP_NAME
            context['CREATE_URL'] = CREATE_URL
            context['LIST_URL'] = LIST_URL
            return context


class ParticipantRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse(APP_NAME + ":detail",
                       kwargs={"slug": self.request.object.slug})


class ParticipantCreateView(LoginRequiredMixin, CreateView):

    # we already imported Participant in the view code above, remember?
    model = Participant
    form_class = ParticipantForm
    succes_msg = "Participant Created!"


class ParticipantUpdateView(LoginRequiredMixin, UpdateView):

    # we already imported Participant in the view code above, remember?
    model = Participant
    form_class = ParticipantForm
