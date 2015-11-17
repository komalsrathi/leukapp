# -*- coding: utf-8 -*-

"""
Url patterns for the leukapp API. See:
    • https://github.com/tomchristie/django-rest-framework
"""

# django
from django.conf.urls import url

# leukapp
from leukapp.apps.participants.views import ParticipantCreateReadView

urlpatterns = [

    # Participants API
    url(
        r'^v0/participants/$',
        ParticipantCreateReadView.as_view(),
        name="particpants"
    ),
]
