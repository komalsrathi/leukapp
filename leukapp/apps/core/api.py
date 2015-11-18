# -*- coding: utf-8 -*-

"""
Url patterns for the leukapp API. See:
    • https://github.com/tomchristie/django-rest-framework
"""

# django
from django.conf.urls import url

# leukapp
from leukapp.apps.participants import views as participant_views

urlpatterns = [

    # Participants API
    url(
        r'^v0/participants/$',
        participant_views.ParticipantCreateReadView.as_view(),
        name="participants"
    ),

    # URL pattern for the ParticipantUpdateView
    url(
        regex=r'^v0/participants/(?P<slug>[\w.@+-]+)/$',
        view=participant_views.ParticipantCreateReadView.as_view(),
        name='participants'
    ),
]
