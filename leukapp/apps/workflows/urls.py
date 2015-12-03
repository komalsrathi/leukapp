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
        view=views.WorkflowDetailView.as_view(),
        name='detail'
    ),

    # URL pattern for the WorkflowListView
    url(
        regex=r'^$',
        view=views.WorkflowListView.as_view(),
        name='list'
    ),

    # URL pattern for the WorkflowRedirectView
    url(
        regex=r'^~redirect/$',
        view=views.WorkflowRedirectView.as_view(),
        name='redirect'
    ),

    # URL pattern for the WorkflowUpdateView
    url(
        regex=r'^~create/$',
        view=views.WorkflowCreateView.as_view(),
        name='create'
    ),

    # URL pattern for the WorkflowUpdateView
    url(
        regex=r'^~update/(?P<slug>[\w.@+-]+)/$',
        view=views.WorkflowUpdateView.as_view(),
        name='update'
    ),

]
