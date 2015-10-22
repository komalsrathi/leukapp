# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [

    # URL pattern for the ParticipantDetailView
    url(
        regex=r'^(?P<slug>[\w.@+-]+)/$',
        view=views.ParticipantDetailView.as_view(),
        name='detail'
    ),

    # URL pattern for the ParticipantListView
    url(
        regex=r'^$',
        view=views.ParticipantListView.as_view(),
        name='list'
    ),

    # URL pattern for the ParticipantRedirectView
    url(
        regex=r'^~redirect/$',
        view=views.ParticipantRedirectView.as_view(),
        name='redirect'
    ),

    # URL pattern for the ParticipantUpdateView
    url(
        regex=r'^~create/$',
        view=views.ParticipantCreateView.as_view(),
        name='create'
    ),

    # URL pattern for the ParticipantCreateModal
    url(
        regex=r'^~createmodal/$',
        view=views.ParticipantCreateModal.as_view(),
        name='createmodal'
    ),

    # URL pattern for the search_participant
    url(
        regex=r'^~search/$',
        view=views.search_participant,
        name='search'
    ),

    # URL pattern for the ParticipantUpdateView
    url(
        regex=r'^~update/(?P<slug>[\w.@+-]+)/$',
        view=views.ParticipantUpdateView.as_view(),
        name='update'
    ),

]
