# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

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
        r'^samples/',
        include("leukapp.apps.samples.urls",
        namespace="samples")
    ),

    url(
        r'^leukforms/',
        include("leukapp.apps.leukforms.urls",
        namespace="leukforms")
    ),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', 'django.views.defaults.bad_request'),
        url(r'^403/$', 'django.views.defaults.permission_denied'),
        url(r'^404/$', 'django.views.defaults.page_not_found'),
        url(r'^500/$', 'django.views.defaults.server_error'),
    ]
