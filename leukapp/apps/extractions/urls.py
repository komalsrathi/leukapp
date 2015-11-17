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
        view=views.ExtractionDetailView.as_view(),
        name='detail'
    ),

    # URL pattern for the ExtractionListView
    url(
        regex=r'^$',
        view=views.ExtractionListView.as_view(),
        name='list'
    ),

    # URL pattern for the ExtractionRedirectView
    url(
        regex=r'^~redirect/$',
        view=views.ExtractionRedirectView.as_view(),
        name='redirect'
    ),

    # URL pattern for the ExtractionUpdateView
    url(
        regex=r'^~create/$',
        view=views.ExtractionCreateView.as_view(),
        name='create'
    ),

    # URL pattern for the ExtractionUpdateView
    url(
        regex=r'^~update/(?P<slug>[\w.@+-]+)/$',
        view=views.ExtractionUpdateView.as_view(),
        name='update'
    ),

]
