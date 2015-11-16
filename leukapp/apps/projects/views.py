# -*- coding: utf-8 -*-

"""
Most of these views inherits from Django's `Class Based Views`. See:
    • https://docs.djangoproject.com/en/1.8/topics/class-based-views/
    • http://ccbv.co.uk/projects/Django/1.8/
    • http://www.pydanny.com/stay-with-the-django-cbv-defaults.html
    • http://www.pydanny.com/tag/class-based-views.html
"""

# python
from __future__ import absolute_import, unicode_literals

# django
from django import forms
from django.views import generic
from django.contrib.auth import mixins
from django.core.urlresolvers import reverse
from django.contrib.messages.views import SuccessMessageMixin

# local
from .models import Project
from . import constants


class ProjectDetailView(mixins.LoginRequiredMixin,
                        generic.DetailView):

    """
    Render a "detail" view of an object. By default this is a model instance
    looked up from `self.queryset`, but the view will support display of *any*
    object by overriding `self.get_object()`.
    See: http://ccbv.co.uk/DetailView/
    """

    model = Project


class ProjectListView(mixins.LoginRequiredMixin,
                      generic.ListView):

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
        if self.request.user.is_superuser:
            return super(ProjectListView, self).get_queryset()
        else:
            email = self.request.user.email
            return Project.objects.filter(participants__email=email)


class ProjectRedirectView(mixins.LoginRequiredMixin,
                          generic.RedirectView):

    """
    A view that provides a redirect on any GET request.
    See: http://ccbv.co.uk/RedirectView/
    """

    permanent = False

    def get_redirect_url(self):
        return reverse(constants.PROJECT_LIST_URL)


class ProjectCreateView(SuccessMessageMixin,
                        mixins.PermissionRequiredMixin,
                        mixins.LoginRequiredMixin,
                        generic.CreateView):

    """
    View for creating a new object, with a response rendered by template.
    See: http://ccbv.co.uk/CreateView/
    """

    model = Project
    fields = constants.PROJECT_CREATE_FIELDS
    success_message = constants.SUCCESS_MESSAGE

    # Permission configuration
    permission_required = ('projects.add_project')
    permission_denied_message = constants.PERMISSION_DENIED_MESSAGE
    raise_exception = True

    def get_form(self, form_class=None):
        form = super(ProjectCreateView, self).get_form(form_class)
        return update_project_form_widgets(form)

    def post(self, request, *args, **kwargs):
        request = clean_participants_in_request(request)
        return super(ProjectCreateView, self).post(
            self, request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save()
        obj.created_by = self.request.user
        obj.save()
        return super(ProjectCreateView, self).form_valid(form)


class ProjectUpdateView(SuccessMessageMixin,
                        mixins.PermissionRequiredMixin,
                        mixins.LoginRequiredMixin,
                        generic.UpdateView):

    """
    View for updating an object, with a response rendered by template.
    See: http://ccbv.co.uk/UpdateView/
    """

    model = Project
    fields = constants.PROJECT_UPDATE_FIELDS
    success_message = constants.SUCCESS_MESSAGE

    # Permissions
    permission_required = ('projects.change_project')
    permission_denied_message = constants.PERMISSION_DENIED_MESSAGE
    raise_exception = True

    def get_form(self, form_class=None):
        form = super(ProjectUpdateView, self).get_form(form_class)
        return update_project_form_widgets(form)

    def post(self, request, *args, **kwargs):
        request = clean_participants_in_request(request)
        return super(ProjectUpdateView, self).post(
            self, request, *args, **kwargs)


# HELPER FUNCTIONS
# -----------------------------------------------------------------------------

def update_project_form_widgets(form):
    """ Prepare form widgets for tokeninput. """

    form.fields['pi'].widget = forms.TextInput()
    form.fields['analyst'].widget = forms.TextInput()
    form.fields['requestor'].widget = forms.TextInput()
    form.fields['participants'].widget = forms.TextInput()
    form.fields['description'].widget = forms.Textarea(attrs={'rows': 3})
    return form


def clean_participants_in_request(request):
    """ Clean participants list returned by tokeninput. """

    try:
        POST = request.POST
        participants = POST['participants'].split(',')
        participants += [POST['pi'], POST['analyst'], POST['requestor']]
        request.POST['participants'] = [int(p) for p in participants]
    except Exception:
        pass
    return request
