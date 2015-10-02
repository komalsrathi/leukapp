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

    # These next two lines tell the view to index lookups by leukid
    slug_field = "leukid"
    slug_url_kwarg = "leukid"


class IndividualRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("individuals:detail",
                       kwargs={"leukid": self.request.individual.leukid})


class IndividualUpdateView(LoginRequiredMixin, UpdateView):

    # we already imported Individual in the view code above, remember?
    model = Individual
    form_class = IndividualForm

    slug_field = "leukid"
    slug_url_kwarg = "leukid"

    # send the individual back to their own page after a successful update
    def get_success_url(self):
        return reverse("individuals:detail",
                       kwargs={"leukid": self.get_object().leukid})


class IndividualCreateView(LoginRequiredMixin, CreateView):

    # we already imported Individual in the view code above, remember?
    succes_msg = "Individual Created!"
    model = Individual
    form_class = IndividualForm

    slug_field = "leukid"
    slug_url_kwarg = "leukid"

    # # send the individual back to their own page after a successful update
    # def get_success_url(self):
    #     return reverse("individuals:detail",
    #                    kwargs={"leukid": self.get_object().leukid})


class IndividualListView(LoginRequiredMixin, ListView):
    model = Individual

    # These next two lines tell the view to index lookups by leukid
    slug_field = "leukid"
    slug_url_kwarg = "leukid"
