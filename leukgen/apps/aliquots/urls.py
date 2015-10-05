# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [

    # URL pattern for the AliquotDetailView
    url(
        regex=r'^(?P<slug>[\w.@+-]+)/$',
        view=views.AliquotDetailView.as_view(),
        name='detail'
    ),

    # URL pattern for the AliquotListView
    url(
        regex=r'^$',
        view=views.AliquotListView.as_view(),
        name='list'
    ),

    # URL pattern for the AliquotRedirectView
    url(
        regex=r'^~redirect/$',
        view=views.AliquotRedirectView.as_view(),
        name='redirect'
    ),

    # URL pattern for the AliquotUpdateView
    url(
        regex=r'^~create/$',
        view=views.AliquotCreateView.as_view(),
        name='create'
    ),

    # URL pattern for the AliquotUpdateView
    url(
        regex=r'^~update/(?P<slug>[\w.@+-]+)/$',
        view=views.AliquotUpdateView.as_view(),
        name='update'
    ),

]
