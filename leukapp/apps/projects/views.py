# -*- coding: utf-8 -*-

"""
Most of these views inherits from Django's `Class Based Views`. See:
    • https://docs.djangoproject.com/en/1.8/topics/class-based-views/
    • http://ccbv.co.uk/projects/Django/1.8/
    • http://www.pydanny.com/stay-with-the-django-cbv-defaults.html
    • http://www.pydanny.com/tag/class-based-views.html

The `LoginRequiredMixin` is also used:
    • http://django-braces.readthedocs.org/en/latest/access.html
"""

# python
from __future__ import absolute_import, unicode_literals

# djano
from django import forms
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.core.urlresolvers import reverse
from django.views.generic import \
    DetailView, ListView, RedirectView, UpdateView, CreateView

# third party
from braces.views import LoginRequiredMixin

# local
from .models import Project
from . import constants


class ProjectDetailView(LoginRequiredMixin, DetailView):

    """
    Render a "detail" view of an object. By default this is a model instance
    looked up from `self.queryset`, but the view will support display of *any*
    object by overriding `self.get_object()`.
    See: http://ccbv.co.uk/DetailView/
    """

    model = Project


class ProjectListView(LoginRequiredMixin, ListView):

    """
    Render some list of objects, set by `self.model` or `self.queryset`.
    `self.queryset` can actually be any iterable of items, not just a queryset.
    See: http://ccbv.co.uk/ListView/
    """

    model = Project
    paginate_by = 20

    def get_context_data(self, **kwargs):
            context = super(ProjectListView, self).get_context_data(**kwargs)

            # Add new context
            context['APP_NAME'] = constants.APP_NAME
            context['CREATE_URL'] = constants.PROJECT_CREATE_URL
            context['LIST_URL'] = constants.PROJECT_LIST_URL
            return context


class ProjectRedirectView(LoginRequiredMixin, RedirectView):

    """
    A view that provides a redirect on any GET request.
    See: http://ccbv.co.uk/RedirectView/
    """

    permanent = False

    def get_redirect_url(self):
        return reverse(constants.PROJECT_LIST_URL)


class ProjectCreateView(LoginRequiredMixin, CreateView):

    """
    View for creating a new object, with a response rendered by template.
    See: http://ccbv.co.uk/CreateView/
    """

    model = Project
    fields = constants.PROJECT_CREATE_FIELDS

    def get_form(self, form_class=None):
        form = super(ProjectCreateView, self).get_form(form_class)
        return update_project_form_widgets(form)

    def post(self, request, *args, **kwargs):
        request = clean_participants_in_request(request)
        return super(ProjectCreateView, self).post(
            self, request, *args, **kwargs)


class ProjectUpdateView(LoginRequiredMixin, UpdateView):

    """
    View for updating an object, with a response rendered by template.
    See: http://ccbv.co.uk/UpdateView/
    """

    model = Project
    fields = constants.PROJECT_UPDATE_FIELDS
    # form_class = ProjectUpdateForm

    def get_form(self, form_class=None):
        form = super(ProjectUpdateView, self).get_form(form_class)
        return update_project_form_widgets(form)

    def post(self, request, *args, **kwargs):
        request = clean_participants_in_request(request)
        return super(ProjectUpdateView, self).post(
            self, request, *args, **kwargs)

    def get_object(self, queryset=None):
        """ force obj.save() on updated model """
        obj = super(ProjectUpdateView, self).get_object()
        obj.save()
        return obj


# HELPER FUNCTIONS
# -----------------------------------------------------------------------------

def update_project_form_widgets(form):
    form.fields['pi'].widget = forms.TextInput()
    form.fields['analyst'].widget = forms.TextInput()
    form.fields['requestor'].widget = forms.TextInput()
    form.fields['participants'].widget = forms.TextInput()
    form.fields['description'].widget = forms.Textarea(attrs={'rows': 3})
    return form


def clean_participants_in_request(request):
    try:
        participants = request.POST['participants'].split(',')
        request.POST['participants'] = [int(p) for p in participants]
    except Exception:
        pass
    return request
