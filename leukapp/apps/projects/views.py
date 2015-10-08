# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import \
    DetailView, ListView, RedirectView, UpdateView, CreateView

from braces.views import LoginRequiredMixin

from .models import Project
from .forms import ProjectForm
from .constants import APP_NAME, CREATE_URL, LIST_URL


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project

    def get_context_data(self, **kwargs):
            context = super(ProjectListView, self).get_context_data(**kwargs)

            # Add new context
            context['APP_NAME'] = APP_NAME
            context['CREATE_URL'] = CREATE_URL
            context['LIST_URL'] = LIST_URL
            return context


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
