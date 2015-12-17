# -*- coding: utf-8 -*-

"""
Models/database schemas for the :mod:`~leukapp.apps.projects` application.

See `Django's Model Documentation`_ for more information.

.. _Django's Model Documentation:
    https://docs.djangoproject.com/en/1.9/topics/db/models/
"""

# django imports
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

# apps imports
from leukapp.apps.core.models import LeukappModel
from leukapp.apps.core.validators import object_name_validator
from leukapp.apps.participants.models import Participant

# local imports
from . import constants


class Project(LeukappModel):

    """Model used to track and manage Projects."""

    APP_NAME = constants.APP_NAME

    # EXTERNAL FIELDS
    # =========================================================================
    title = models.CharField(
        _("project title"),
        max_length=100,
        validators=[object_name_validator],
        unique=True,
        null=True,
        )
    description = models.CharField(
        _("project description"),
        max_length=500,
        null=True,
        )
    pi = models.ForeignKey(
        Participant,
        verbose_name=_("principal investigator"),
        related_name='projects_as_pi',
        help_text='Laboratory head or principal investigator',
        null=True,
        )
    analyst = models.ForeignKey(
        Participant,
        verbose_name=_("data analyst"),
        related_name='projects_as_analyst',
        null=True,
        )
    requestor = models.ForeignKey(
        Participant,
        verbose_name=_("requestor"),
        related_name='projects_as_requestor',
        null=True,
        )
    participants = models.ManyToManyField(
        Participant,
        verbose_name=_("participants"),
        related_name='projects_as_participant',
        blank=True,
        )
    cost_center_no = models.CharField(
        _("cost center number"),
        max_length=100,
        null=True,
        )
    fund_no = models.CharField(
        _("fund number"),
        max_length=100,
        null=True,
        )
    protocol_no = models.CharField(
        _("IRB protocol number"),
        max_length=100,
        null=True,
        )

    # INTERNAL FIELDS
    # =========================================================================
    slug = models.SlugField(
        _("slug"),
        unique=True,
        editable=False,
        null=True,
        )
    int_id = models.SlugField(
        _("int_id"),
        unique=True,
        editable=False,
        null=True,
        )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("created by"),
        blank=True,
        null=True,
        )

    # META CLASS
    # =========================================================================
    class Meta:
        verbose_name = _(constants.APP_NAME[:-1])
        verbose_name_plural = _(constants.APP_NAME)

    # PUBLIC METHODS
    # =========================================================================
    def __str__(self):
        """Return slug when str is called on object."""
        return self.slug

    # PRIVATE METHODS
    # =========================================================================
    def _if_new(self):
        """
        Executed only when the object is created.

        .. currentmodule::
            leukapp.apps.core
        .. note::
            This method can only be called from
            :meth:`~models.LeukappModel.save` and is protected by
            :meth:`~models.LeukappModel._check_if_caller_is_save`.
        """
        self._check_if_caller_is_save()

        # get internal id
        self.int_id = str(self.pk)

    def _if_save(self):
        """
        Executed everytime the object is saved.

        .. currentmodule::
            leukapp.apps.core
        .. note::
            This method can only be called from
            :meth:`~models.LeukappModel.save` and is protected by
            :meth:`~models.LeukappModel._check_if_caller_is_save`.
        """
        self._check_if_caller_is_save()

        # update object slug
        self.slug = self.int_id

        # update paticipants
        self.participants.add(self.pi, self.analyst, self.requestor)
