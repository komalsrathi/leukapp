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
from django.http import JsonResponse
from django.views import generic
from django.contrib.auth import mixins
from django.core.urlresolvers import reverse
from django.contrib.messages.views import SuccessMessageMixin

# third party
from django_modalview.generic.edit import ModalCreateView
from django_modalview.generic.component import ModalResponse, ModalButton
from rest_framework.generics import ListCreateAPIView

# local
from .models import Participant
from .forms import ParticipantForm
from .serializers import ParticipantCreateSerializer
from . import constants


# Class Based Views
# -----------------------------------------------------------------------------

class ParticipantDetailView(mixins.LoginRequiredMixin,
                            generic.DetailView):

    """
    Render a "detail" view of an object. By default this is a model instance
    looked up from `self.queryset`, but the view will support display of *any*
    object by overriding `self.get_object()`.
    See: http://ccbv.co.uk/DetailView/
    """

    model = Participant


class ParticipantListView(mixins.LoginRequiredMixin,
                          generic.ListView):

    """
    Render some list of objects, set by `self.model` or `self.queryset`.
    `self.queryset` can actually be any iterable of items, not just a queryset.
    See: http://ccbv.co.uk/ListView/
    """

    model = Participant

    def get_context_data(self, **kwargs):
        super_function = super(ParticipantListView, self).get_context_data
        context = super_function(**kwargs)
        context['APP_NAME'] = constants.APP_NAME
        context['CREATE_URL'] = constants.PARTICIPANT_CREATE_URL
        context['LIST_URL'] = constants.PARTICIPANT_LIST_URL
        return context


class ParticipantRedirectView(mixins.LoginRequiredMixin,
                              generic.RedirectView):

    """
    A view that provides a redirect on any GET request.
    See: http://ccbv.co.uk/RedirectView/
    """

    permanent = False

    def get_redirect_url(self):
        return reverse(constants.PARTICIPANT_LIST_URL)


class ParticipantCreateView(SuccessMessageMixin,
                            mixins.PermissionRequiredMixin,
                            mixins.LoginRequiredMixin,
                            generic.CreateView):

    """
    View for creating a new object, with a response rendered by template.
    See: http://ccbv.co.uk/CreateView/
    """

    model = Participant
    fields = constants.PARTICIPANT_CREATE_FIELDS
    success_message = constants.SUCCESS_MESSAGE

    # Permission configuration
    permission_required = constants.PARTICIPANT_CREATE_PERMISSIONS
    permission_denied_message = constants.PERMISSION_DENIED_MESSAGE
    raise_exception = True


class ParticipantUpdateView(SuccessMessageMixin,
                            mixins.PermissionRequiredMixin,
                            mixins.LoginRequiredMixin,
                            generic.UpdateView):

    """
    View for updating an object, with a response rendered by template.
    See: http://ccbv.co.uk/UpdateView/
    """

    model = Participant
    fields = constants.PARTICIPANT_UPDATE_FIELDS
    success_message = constants.SUCCESS_MESSAGE

    # Permission configuration
    permission_required = constants.PARTICIPANT_UPDATE_PERMISSIONS
    permission_denied_message = constants.PERMISSION_DENIED_MESSAGE
    raise_exception = True


class ParticipantCreateModal(mixins.PermissionRequiredMixin,
                             mixins.LoginRequiredMixin,
                             ModalCreateView):

    """
    Simple class based view to create participants in a modal window.
    See: https://github.com/optiflows/django-modalview
    """

    # Permission configuration
    permission_required = constants.PARTICIPANT_CREATE_PERMISSIONS
    permission_denied_message = constants.PERMISSION_DENIED_MESSAGE
    raise_exception = True

    def __init__(self, *args, **kwargs):
        super(ParticipantCreateModal, self).__init__(*args, **kwargs)
        self.title = "Create Participant"
        self.form_class = ParticipantForm
        self.submit_button = ModalButton("Submit", button_type='primary')
        self.close_button = None

    def form_valid(self, form, **kwargs):
        self.response = ModalResponse("Added", "success")
        return super(ParticipantCreateModal, self).form_valid(form, **kwargs)


# Function Based Views
# -----------------------------------------------------------------------------

def search_participant(request):
    """
    View used to return participants for a token-input jQuery plugin.
    See: http://loopj.com/jquery-tokeninput/
    """

    response = []
    try:
        q = request.GET.get('q')
        queryset = Participant.objects.filter(email__icontains=q)
        for i in queryset:
            out = {'id': str(i.pk), "name": i.email}
            response.append(out)
        return JsonResponse(response)
    except Exception:
        return JsonResponse(response, safe=False)


# API
# -----------------------------------------------------------------------------

class ParticipantCreateReadView(mixins.PermissionRequiredMixin,
                                mixins.LoginRequiredMixin,
                                ListCreateAPIView):

    """
    Concrete view for listing a queryset or creating a model instance.
    See: http://www.cdrf.co/3.3/rest_framework.generics/ListCreateAPIView.html
    """

    queryset = Participant.objects.all()
    serializer_class = ParticipantCreateSerializer
    lookup_field = 'slug'
    paginate_by = 10

    # Permission configuration
    permission_required = constants.PARTICIPANT_CREATE_PERMISSIONS
    permission_denied_message = constants.PERMISSION_DENIED_MESSAGE
    raise_exception = True
