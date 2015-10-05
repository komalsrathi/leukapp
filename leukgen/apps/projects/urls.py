# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [

    # URL pattern for the ProjectDetailView
    url(
        regex=r'^(?P<slug>[\w.@+-]+)/$',
        view=views.ProjectDetailView.as_view(),
        name='detail'
    ),

    # URL pattern for the ProjectListView
    url(
        regex=r'^$',
        view=views.ProjectListView.as_view(),
        name='list'
    ),

    # URL pattern for the ProjectRedirectView
    url(
        regex=r'^~redirect/$',
        view=views.ProjectRedirectView.as_view(),
        name='redirect'
    ),

    # URL pattern for the ProjectUpdateView
    url(
        regex=r'^~create/$',
        view=views.ProjectCreateView.as_view(),
        name='create'
    ),

    # URL pattern for the ProjectUpdateView
    url(
        regex=r'^~update/(?P<slug>[\w.@+-]+)/$',
        view=views.ProjectUpdateView.as_view(),
        name='update'
    ),

]
