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

    # URL pattern for unit testing
    url(
        regex=r'^(\d+)/$',
        view=views.view_list,
        name='view_list'
    ),

    # URL pattern for the views.new_list
    url(
        regex=r'^new$',
        view=views.new_list,
        name='new_list'
    ),

    # URL pattern for the views.new_list
    url(
        regex=r'^(\d+)/add_item$',
        view=views.add_item,
        name='add_item'
    ),

]
