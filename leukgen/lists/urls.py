# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the views.home_page
    url(
        regex=r'^$',
        view=views.home_page,
        name='home'
    ),

    # URL pattern for the views.home_page
    url(
        regex=r'^the-only/$',
        view=views.view_list,
        name='view_list'
    ),

]
