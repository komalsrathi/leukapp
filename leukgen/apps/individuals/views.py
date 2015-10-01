# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from braces.views import LoginRequiredMixin

from .models import Individual


class IndividualDetailView(LoginRequiredMixin, DetailView):
    model = Individual
    # These next two lines tell the view to index lookups by pk
    slug_field = "pk"
    slug_url_kwarg = "pk"


class IndividualRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("individuals:detail",
                       kwargs={"pk": self.request.individual.pk})


class IndividualUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['species', 'institution']

    # we already imported Individual in the view code above, remember?
    model = Individual

    slug_field = "pk"
    slug_url_kwarg = "pk"

    # send the individual back to their own page after a successful update
    def get_success_url(self):
        print(self.get_context_data())
        return reverse("individuals:detail",
                       kwargs={"pk": self.get_object().pk})


class IndividualListView(LoginRequiredMixin, ListView):
    model = Individual
    # These next two lines tell the view to index lookups by pk
    slug_field = "pk"
    slug_url_kwarg = "pk"
