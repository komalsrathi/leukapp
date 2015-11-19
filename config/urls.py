# -*- coding: utf-8 -*-

# python
from __future__ import unicode_literals

# django
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

# local
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
        include('allauth.urls')
    ),

    # autocomplete // NOTUSED
    url(r'^autocomplete/', include('autocomplete_light.urls')),

    url(
        r'^api-auth/',
        include('rest_framework.urls',
                namespace='rest_framework')
    ),

    # leukapp
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
        r'^extractions/',
        include("leukapp.apps.extractions.urls",
                namespace="extractions")
    ),

    url(
        r'^leukforms/',
        include("leukapp.apps.leukforms.urls",
                namespace="leukforms")
    ),

    url(
        r'^api/',
        include("leukapp.apps.core.api",
                namespace="api")
    ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
