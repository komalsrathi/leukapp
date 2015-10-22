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
        view=views.LeukformDetailView.as_view(),
        name='detail'
    ),

    # URL pattern for the LeukformListView
    url(
        regex=r'^$',
        view=views.LeukformListView.as_view(),
        name='list'
    ),

    # URL pattern for the LeukformRedirectView
    url(
        regex=r'^~redirect/$',
        view=views.LeukformRedirectView.as_view(),
        name='redirect'
    ),

    # URL pattern for the LeukformUpdateView
    url(
        regex=r'^~create/$',
        view=views.LeukformCreateView.as_view(),
        name='create'
    ),

    # URL pattern for the LeukformUpdateView
    url(
        regex=r'^~update/(?P<slug>[\w.@+-]+)/$',
        view=views.LeukformUpdateView.as_view(),
        name='update'
    ),

    # URL pattern for the download_result
    url(
        regex=r'^~result/(?P<slug>[\w.@+-]+)/$',
        view=views.download_result,
        name='result'
    ),

]
