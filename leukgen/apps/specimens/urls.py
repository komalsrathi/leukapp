# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the SpecimenRedirectView
    url(
        regex=r'^~redirect/$',
        view=views.SpecimenRedirectView.as_view(),
        name='redirect'
    ),

    # URL pattern for the SpecimenDetailView
    url(
        regex=r'^(?P<slug>[\w.@+-]+)/$',
        view=views.SpecimenDetailView.as_view(),
        name='detail'
    ),

    # URL pattern for the SpecimenListView
    url(
        regex=r'^$',
        view=views.SpecimenListView.as_view(),
        name='list'
    ),

    # URL pattern for the SpecimenUpdateView
    url(
        regex=r'^~create/$',
        view=views.SpecimenCreateView.as_view(),
        name='create'
    ),

    # URL pattern for the SpecimenUpdateView
    url(
        regex=r'^~update/(?P<slug>[\w.@+-]+)/$',
        view=views.SpecimenUpdateView.as_view(),
        name='update'
    ),

]
