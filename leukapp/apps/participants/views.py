# -*- coding: utf-8 -*-

# python
from __future__ import absolute_import, unicode_literals

# django
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.views.generic import \
    DetailView, ListView, RedirectView, UpdateView, CreateView

# third party
from braces.views import LoginRequiredMixin
from django_modalview.generic.edit import ModalCreateView
from django_modalview.generic.component import ModalResponse

# local
from .models import Participant
from .forms import ParticipantForm
from .constants import APP_NAME, CREATE_URL, LIST_URL


class ParticipantDetailView(LoginRequiredMixin, DetailView):
    model = Participant


class ParticipantListView(LoginRequiredMixin, ListView):
    model = Participant

    def get_context_data(self, **kwargs):
            context = super(
                ParticipantListView, self).get_context_data(**kwargs)

            # Add new context
            context['APP_NAME'] = APP_NAME
            context['CREATE_URL'] = CREATE_URL
            context['LIST_URL'] = LIST_URL
            return context


class ParticipantRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse(APP_NAME + ":detail",
                       kwargs={"slug": self.request.object.slug})


class ParticipantCreateView(LoginRequiredMixin, CreateView):

    # we already imported Participant in the view code above, remember?
    model = Participant
    form_class = ParticipantForm
    succes_msg = "Participant Created!"


class ParticipantUpdateView(LoginRequiredMixin, UpdateView):

    # we already imported Participant in the view code above, remember?
    model = Participant
    form_class = ParticipantForm


class ParticipantCreateModal(ModalCreateView):

    def __init__(self, *args, **kwargs):
        super(ParticipantCreateModal, self).__init__(*args, **kwargs)
        self.title = "Create Participant"
        self.form_class = ParticipantForm
        self.close_button = None

    def form_valid(self, form, **kwargs):
        self.response = ModalResponse("Added", "success")
        return super(ParticipantCreateModal, self).form_valid(form, **kwargs)


def search_participant(request):
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
