# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults

from .views import ConfigTemplateView

urlpatterns = [
    url(
        r'^$',
        ConfigTemplateView.as_view(template_name='pages/home.html'),
        name="home"
    ),

    # Django Admin
    url(
        r'^admin/',
        include(admin.site.urls)
    ),

    # User management
    url(
        r'^users/',
        include("leukapp.apps.users.urls",
        namespace="users")
    ),

    url(
        r'^accounts/',
        include('allauth.urls')),

    # autocomplete
    url(r'^autocomplete/', include('autocomplete_light.urls')),

    # Your stuff: custom urls includes go here
    url(
        r'^lists/',
        include("leukapp.apps.lists.urls",
        namespace="lists")
    ),

    url(
        r'^projects/',
        include("leukapp.apps.projects.urls",
        namespace="projects")
    ),

    url(
        r'^aliquots/',
        include("leukapp.apps.aliquots.urls",
        namespace="aliquots")
    ),

    url(
        r'^specimens/',
        include("leukapp.apps.specimens.urls",
        namespace="specimens")
    ),

    url(
        r'^individuals/',
        include("leukapp.apps.individuals.urls",
        namespace="individuals")
    ),

    url(
        r'^participants/',
        include("leukapp.apps.participants.urls",
        namespace="participants")
    ),

    url(
        r'^runs/',
        include("leukapp.apps.runs.urls",
        namespace="runs")
    ),

    url(
        r'^leukforms/',
        include("leukapp.apps.leukforms.urls",
        namespace="leukforms")
    ),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
