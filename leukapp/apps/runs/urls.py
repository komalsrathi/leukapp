# -*- coding: utf-8 -*-

# python
from __future__ import absolute_import, unicode_literals

# django
from django.conf.urls import url

# local
from . import views

urlpatterns = [

    # URL pattern for the AliquotDetailView
    url(
        regex=r'^(?P<slug>[\w.@+-]+)/$',
        view=views.RunDetailView.as_view(),
        name='detail'
    ),

    # URL pattern for the RunListView
    url(
        regex=r'^$',
        view=views.RunListView.as_view(),
        name='list'
    ),

    # URL pattern for the RunRedirectView
    url(
        regex=r'^~redirect/$',
        view=views.RunRedirectView.as_view(),
        name='redirect'
    ),

    # URL pattern for the RunUpdateView
    url(
        regex=r'^~create/$',
        view=views.RunCreateView.as_view(),
        name='create'
    ),

    # URL pattern for the RunUpdateView
    url(
        regex=r'^~update/(?P<slug>[\w.@+-]+)/$',
        view=views.RunUpdateView.as_view(),
        name='update'
    ),

]
