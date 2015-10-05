# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import \
    DetailView, ListView, RedirectView, UpdateView, CreateView

from braces.views import LoginRequiredMixin

from .models import Participant
from .forms import ParticipantForm
from .constants import APP_NAME


class ParticipantDetailView(LoginRequiredMixin, DetailView):
    model = Participant


class ParticipantListView(LoginRequiredMixin, ListView):
    model = Participant


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
