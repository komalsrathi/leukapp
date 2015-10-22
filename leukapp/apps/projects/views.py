# -*- coding: utf-8 -*-

# python
from __future__ import absolute_import, unicode_literals

# djano
from django import forms
from django.core.urlresolvers import reverse
from django.views.generic import \
    DetailView, ListView, RedirectView, UpdateView, CreateView

# third party
from braces.views import LoginRequiredMixin

# local
from .forms import ProjectUpdateForm, ProjectCreateForm
from .models import Project
from . import constants


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project


class ProjectListView(LoginRequiredMixin, ListView):

    model = Project
    paginate_by = 20

    def get_context_data(self, **kwargs):
            context = super(ProjectListView, self).get_context_data(**kwargs)

            # Add new context
            context['APP_NAME'] = constants.APP_NAME
            context['CREATE_URL'] = constants.CREATE_URL
            context['LIST_URL'] = constants.LIST_URL
            return context


class ProjectRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse(constants.APP_NAME + ":detail",
                       kwargs={"slug": self.request.object.slug})


class ProjectCreateView(LoginRequiredMixin, CreateView):

    # we already imported Project in the view code above, remember?
    model = Project
    form_class = ProjectCreateForm

    def get_form(self, form_class):
        form = super(ProjectCreateView, self).get_form(form_class)
        form.fields['pi'].widget = forms.TextInput()
        form.fields['analyst'].widget = forms.TextInput()
        form.fields['requestor'].widget = forms.TextInput()
        form.fields['participants'].widget = forms.TextInput()
        form.fields['description'].widget = forms.Textarea(
            attrs={'rows': 3})
        return form


class ProjectUpdateView(LoginRequiredMixin, UpdateView):

    # we already imported Project in the view code above, remember?
    model = Project
    form_class = ProjectUpdateForm

    def get_form(self, form_class):
        form = super(ProjectUpdateView, self).get_form(form_class)
        form.fields['pi'].widget = forms.TextInput()
        form.fields['analyst'].widget = forms.TextInput()
        form.fields['requestor'].widget = forms.TextInput()
        form.fields['participants'].widget = forms.TextInput()
        form.fields['description'].widget = forms.Textarea(
            attrs={'rows': 3})
        return form
