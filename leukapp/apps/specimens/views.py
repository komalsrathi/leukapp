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
from django.views import generic
from django.contrib.auth import mixins
from django.core.urlresolvers import reverse
from django.contrib.messages.views import SuccessMessageMixin

# local
from .models import Specimen
from . import constants


class SpecimenDetailView(mixins.LoginRequiredMixin,
                         generic.DetailView):

    """
    Render a "detail" view of an object. By default this is a model instance
    looked up from `self.queryset`, but the view will support display of *any*
    object by overriding `self.get_object()`.
    See: http://ccbv.co.uk/DetailView/
    """

    model = Specimen


class SpecimenListView(mixins.LoginRequiredMixin,
                       generic.ListView):

    """
    Render some list of objects, set by `self.model` or `self.queryset`.
    `self.queryset` can actually be any iterable of items, not just a queryset.
    See: http://ccbv.co.uk/ListView/
    """

    model = Specimen
    paginate_by = 20

    def get_context_data(self, **kwargs):
            context = super(SpecimenListView, self).get_context_data(**kwargs)
            context['APP_NAME'] = constants.APP_NAME
            context['CREATE_URL'] = constants.SPECIMEN_CREATE_URL
            return context


class SpecimenRedirectView(mixins.LoginRequiredMixin,
                           generic.RedirectView):

    """
    A view that provides a redirect on any GET request.
    See: http://ccbv.co.uk/RedirectView/
    """

    permanent = False

    def get_redirect_url(self):
        return reverse(constants.SPECIMEN_LIST_URL)


class SpecimenCreateView(SuccessMessageMixin,
                         mixins.PermissionRequiredMixin,
                         mixins.LoginRequiredMixin,
                         generic.CreateView):

    """
    View for creating a new object, with a response rendered by template.
    See: http://ccbv.co.uk/CreateView/
    """

    model = Specimen
    fields = constants.SPECIMEN_CREATE_FIELDS
    success_message = constants.SUCCESS_MESSAGE

    # Permissions
    permission_required = constants.SPECIMEN_CREATE_PERMISSIONS
    permission_denied_message = constants.PERMISSION_DENIED_MESSAGE
    raise_exception = True


class SpecimenUpdateView(SuccessMessageMixin,
                         mixins.PermissionRequiredMixin,
                         mixins.LoginRequiredMixin,
                         generic.UpdateView):

    """
    View for updating an object, with a response rendered by template.
    See: http://ccbv.co.uk/UpdateView/
    """

    model = Specimen
    fields = constants.SPECIMEN_UPDATE_FIELDS
    success_message = constants.SUCCESS_MESSAGE

    # Permissions
    permission_required = constants.SPECIMEN_UPDATE_PERMISSIONS
    permission_denied_message = constants.PERMISSION_DENIED_MESSAGE
    raise_exception = True
