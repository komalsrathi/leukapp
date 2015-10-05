# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import \
    DetailView, ListView, RedirectView, UpdateView, CreateView

from braces.views import LoginRequiredMixin

from .models import Aliquot
from .forms import AliquotForm
from .constants import APP_NAME


class AliquotDetailView(LoginRequiredMixin, DetailView):
    model = Aliquot


class AliquotListView(LoginRequiredMixin, ListView):
    model = Aliquot


class AliquotRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse(APP_NAME + ":detail",
                       kwargs={"slug": self.request.object.slug})


class AliquotCreateView(LoginRequiredMixin, CreateView):

    # we already imported Aliquot in the view code above, remember?
    model = Aliquot
    form_class = AliquotForm
    succes_msg = "Aliquot Created!"


class AliquotUpdateView(LoginRequiredMixin, UpdateView):

    # we already imported Aliquot in the view code above, remember?
    model = Aliquot
    form_class = AliquotForm
