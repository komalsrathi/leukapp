# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the views.home_page
    url(
        regex=r'^$',
        view=views.ProjectCreateView.as_view(),
        name='create'
    ),

]
