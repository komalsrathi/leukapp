# -*- coding: utf-8 -*-

"""
Most of these views inherits from Django's `Class Based Views`. See:
    • https://docs.djangoproject.com/en/1.8/topics/class-based-views/
    • http://ccbv.co.uk/projects/Django/1.8/
    • http://www.pydanny.com/stay-with-the-django-cbv-defaults.html
    • http://www.pydanny.com/tag/class-based-views.html

The `views.LoginRequiredMixin` is also used:
    • http://django-braces.readthedocs.org/en/latest/access.html
"""

# python
from __future__ import absolute_import, unicode_literals

# djano
from django import forms
from django.core.urlresolvers import reverse
from django.views.generic import \
    DetailView, ListView, RedirectView, UpdateView, CreateView

# third party
from braces import views

# local
from .models import Project
from . import constants


class ProjectDetailView(views.LoginRequiredMixin, DetailView):

    """
    Render a "detail" view of an object. By default this is a model instance
    looked up from `self.queryset`, but the view will support display of *any*
    object by overriding `self.get_object()`.
    See: http://ccbv.co.uk/DetailView/
    """

    model = Project


class ProjectListView(views.LoginRequiredMixin, ListView):

    """
    Render some list of objects, set by `self.model` or `self.queryset`.
    `self.queryset` can actually be any iterable of items, not just a queryset.
    See: http://ccbv.co.uk/ListView/
    """

    model = Project
    paginate_by = 20

    def get_context_data(self, **kwargs):
            context = super(ProjectListView, self).get_context_data(**kwargs)
            context['APP_NAME'] = constants.APP_NAME
            context['CREATE_URL'] = constants.PROJECT_CREATE_URL
            context['LIST_URL'] = constants.PROJECT_LIST_URL
            return context

    def get_queryset(self):
        email = self.request.user.email
        return Project.objects.filter(participants__email=email)


class ProjectRedirectView(views.LoginRequiredMixin, RedirectView):

    """
    A view that provides a redirect on any GET request.
    See: http://ccbv.co.uk/RedirectView/
    """

    permanent = False

    def get_redirect_url(self):
        return reverse(constants.PROJECT_LIST_URL)


class ProjectCreateView(views.MultiplePermissionsRequiredMixin,
                        views.LoginRequiredMixin,
                        CreateView):

    """
    View for creating a new object, with a response rendered by template.
    See: http://ccbv.co.uk/CreateView/
    """

    model = Project
    fields = constants.PROJECT_CREATE_FIELDS

    # required
    raise_exception = True
    permissions = {
        "all": ('add_user', ),
        "any": ()
    }

    def get_form(self, form_class=None):
        form = super(ProjectCreateView, self).get_form(form_class)
        return update_project_form_widgets(form)

    def post(self, request, *args, **kwargs):
        request = clean_participants_in_request(request)
        return super(ProjectCreateView, self).post(
            self, request, *args, **kwargs)

    def form_valid(self, form):
        """ Add created_by to form """
        obj = form.save()
        obj.created_by = self.request.user
        obj.save()
        return super(ProjectCreateView, self).form_valid(form)


class ProjectUpdateView(views.LoginRequiredMixin, UpdateView):

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


# -----------------------------------------------------------------------------
# HELPER FUNCTIONS

def update_project_form_widgets(form):
    form.fields['pi'].widget = forms.TextInput()
    form.fields['analyst'].widget = forms.TextInput()
    form.fields['requestor'].widget = forms.TextInput()
    form.fields['participants'].widget = forms.TextInput()
    form.fields['description'].widget = forms.Textarea(attrs={'rows': 3})
    return form


def clean_participants_in_request(request):
    try:
        POST = request.POST
        participants = POST['participants'].split(',')
        participants += [POST['pi'], POST['analyst'], POST['requestor']]
        request.POST['participants'] = [int(p) for p in participants]
    except Exception:
        pass
    return request
