# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import \
    DetailView, ListView, RedirectView, UpdateView, CreateView

from braces.views import LoginRequiredMixin

from .models import Specimen
from .forms import SpecimenForm


class SpecimenDetailView(LoginRequiredMixin, DetailView):
    model = Specimen

    # These next two lines tell the view to index lookups by leukid
    # slug_field = "leukid"
    # slug_url_kwarg = "slug"


class SpecimenListView(LoginRequiredMixin, ListView):
    model = Specimen

    # These next two lines tell the view to index lookups by leukid
    slug_field = "leukid"
    slug_url_kwarg = "leukid"


class SpecimenRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("specimens:detail",
                       kwargs={"leukid": self.request.specimen.leukid})


class SpecimenCreateView(LoginRequiredMixin, CreateView):

    # we already imported Specimen in the view code above, remember?
    succes_msg = "Specimen Created!"
    model = Specimen
    form_class = SpecimenForm

    slug_field = "leukid"
    slug_url_kwarg = "leukid"


class SpecimenUpdateView(LoginRequiredMixin, UpdateView):

    # we already imported Specimen in the view code above, remember?
    model = Specimen
    form_class = SpecimenForm

    slug_field = "leukid"
    slug_url_kwarg = "leukid"
