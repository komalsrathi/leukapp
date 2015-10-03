# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import \
    DetailView, ListView, RedirectView, UpdateView, CreateView

from braces.views import LoginRequiredMixin

from .models import Individual
from .forms import IndividualForm


class IndividualDetailView(LoginRequiredMixin, DetailView):
    model = Individual


class IndividualListView(LoginRequiredMixin, ListView):
    model = Individual


class IndividualRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("individuals:detail",
                       kwargs={"slug": self.request.individual.slug})


class IndividualCreateView(LoginRequiredMixin, CreateView):

    # we already imported Individual in the view code above, remember?
    model = Individual
    form_class = IndividualForm
    succes_msg = "Individual Created!"


class IndividualUpdateView(LoginRequiredMixin, UpdateView):

    # we already imported Individual in the view code above, remember?
    model = Individual
    form_class = IndividualForm
