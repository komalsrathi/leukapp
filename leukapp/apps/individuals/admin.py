# -*- coding: utf-8 -*-

"""
Admin settings for the :mod:`~leukapp.apps.individuals` application.
To learn more see the `Django admin site`_ documentation.

.. _Django admin site: https://docs.djangoproject.com/en/1.8/ref/contrib/admin/
"""

# django
from django.contrib import admin

# leukapp
from leukapp.apps.specimens.models import Specimen

# local
from .models import Individual


class SpecimenInline(admin.StackedInline):

    """
    .. py:currentmodule:: leukapp.apps.individuals

    Enable the creation of :attr:`~admin.SpecimenInline.extra`
    :class:`Specimens <~leukapp.apps.specimens.models.Specimen>`.

    The admin interface has the ability to edit models on the same page as a
    parent model. These are called inlines. See `InLineModelAdmin` objects.

    .. _InLineModelAdmin: https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#inlinemodeladmin-objects

    """

    model = Specimen    #: Name of InLine model.
    extra = 2           #: Number of extra ``Specimens`` that can be created.


class IndividualAdmin(admin.ModelAdmin):

    """
    Class to manage :class:`Individuals <models.Indiviual>` from the admin
    site.
    """

    inlines = [SpecimenInline]  #: List InLine objects to be added.


# Individual Admin Registration
# =============================================================================

admin.site.register(Individual, IndividualAdmin)
