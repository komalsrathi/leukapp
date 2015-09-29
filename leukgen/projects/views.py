# -*- coding: utf-8 -*-
# django imports
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import CreateView

from braces.views import LoginRequiredMixin

from .models import Project


class ProjectCreateView(LoginRequiredMixin, CreateView):

    """docstring for ProjectCreateView"""

    model = Project
    fields = (
        'pi', 'scientist', 'data_analyst', 'name', 'description'
    )

    def get_success_url(self):
        return reverse("home")
