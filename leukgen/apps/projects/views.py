# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import \
    DetailView, ListView, RedirectView, UpdateView, CreateView

from braces.views import LoginRequiredMixin

from .models import Project
from .forms import ProjectForm
from .constants import APP_NAME


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project


class ProjectRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse(APP_NAME + ":detail",
                       kwargs={"slug": self.request.object.slug})


class ProjectCreateView(LoginRequiredMixin, CreateView):

    # we already imported Project in the view code above, remember?
    model = Project
    form_class = ProjectForm
    succes_msg = "Project Created!"


class ProjectUpdateView(LoginRequiredMixin, UpdateView):

    # we already imported Project in the view code above, remember?
    model = Project
    form_class = ProjectForm
