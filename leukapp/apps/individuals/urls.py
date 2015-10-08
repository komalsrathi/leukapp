# -*- coding: utf-8 -*-

# python
from __future__ import absolute_import, unicode_literals

# django
from django.conf.urls import url

# local
from . import views

urlpatterns = [

    # URL pattern for the IndividualDetailView
    url(
        regex=r'^(?P<slug>[\w.@+-]+)/$',
        view=views.IndividualDetailView.as_view(),
        name='detail'
    ),

    # URL pattern for the IndividualListView
    url(
        regex=r'^$',
        view=views.IndividualListView.as_view(),
        name='list'
    ),

    # URL pattern for the IndividualRedirectView
    url(
        regex=r'^~redirect/$',
        view=views.IndividualRedirectView.as_view(),
        name='redirect'
    ),

    # URL pattern for the IndividualUpdateView
    url(
        regex=r'^~create/$',
        view=views.IndividualCreateView.as_view(),
        name='create'
    ),

    # URL pattern for the IndividualUpdateView
    url(
        regex=r'^~update/(?P<slug>[\w.@+-]+)/$',
        view=views.IndividualUpdateView.as_view(),
        name='update'
    ),

]
