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
        view=views.SampleDetailView.as_view(),
        name='detail'
    ),

    # URL pattern for the SampleListView
    url(
        regex=r'^$',
        view=views.SampleListView.as_view(),
        name='list'
    ),

    # URL pattern for the SampleRedirectView
    url(
        regex=r'^~redirect/$',
        view=views.SampleRedirectView.as_view(),
        name='redirect'
    ),

    # URL pattern for the SampleUpdateView
    url(
        regex=r'^~create/$',
        view=views.SampleCreateView.as_view(),
        name='create'
    ),

    # URL pattern for the SampleUpdateView
    url(
        regex=r'^~update/(?P<slug>[\w.@+-]+)/$',
        view=views.SampleUpdateView.as_view(),
        name='update'
    ),

]
