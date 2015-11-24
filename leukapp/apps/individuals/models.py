# -*- coding: utf-8 -*-

"""
ORM models for the :mod:`~leukapp.apps.individuals` application.

See `Django's Model Documentation`_ for more information.

.. _Django's Model Documentation:
    https://docs.djangoproject.com/en/1.9/topics/db/models/
"""

# django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# leukapp
from leukapp.apps.core.models import LeukappModel
from leukapp.apps.core.validators import ext_id_validator

# local
from . import constants


class Individual(LeukappModel):

    """
    requirements: https://docs.google.com/spreadsheets/d/17TJ6zQ3OzwE-AZVZykFzzbHxtDM88aM7vvCPxJQ8-_M/edit#gid=288765627
    """

    APP_NAME = constants.APP_NAME
    CHOICES = constants.INDIVIDUAL_CHOICES

    # EXTERNAL FIELDS
    # -------------------------------------------------------------------------
    institution = models.CharField(
        _("institution"),
        max_length=100,
        choices=CHOICES["INSTITUTION"],
        null=True,
        )
    """
    .. py:currentmodule:: leukapp.apps.individuals
    Indicates whether the :class:`~models.Indiviual` comes from MSK or not.
    See the available choices: :class:`~constants.INSTITUTION`.
    """

    species = models.CharField(
        _("species"),
        max_length=100,
        choices=CHOICES["SPECIES"],
        null=True,
        )
    """
    .. py:currentmodule:: leukapp.apps.individuals
    Indicates the :class:`~models.Indiviual` species.
    See the available choices: :class:`~constants.SPECIES`.
    """

    ext_id = models.CharField(
        _("external id"),
        max_length=100,
        validators=[ext_id_validator],
        help_text=_(
            "The external id should be unique at the "
            "Institution and Species levels. MRNs are not allowed for {0}S "
            "from {1}. Please use a pseudo MRN or other type of identifier."
            ).format(constants.HUMAN, constants.MSK),
        null=True,
        )
    """
    .. py:currentmodule:: leukapp.apps.individuals
    Indicates the :class:`~models.Indiviual` external id.
    This field is validated using the
    :obj:`~leukapp.apps.core.validators.ext_id_validator`.

    .. warning::
        **MRNs** are not allowed for ``HUMANS`` from ``MSK``. Please use a
        pseudo MRN or other type of identifier.
    """

    # INTERNAL FIELDS
    # -------------------------------------------------------------------------
    tumors_count = models.PositiveSmallIntegerField(
        _("number of tumor specimens created"),
        default=0,
        editable=False,
        null=True,
        )
    """
    """

    normals_count = models.PositiveSmallIntegerField(
        _("number of normal specimens created"),
        default=0,
        editable=False,
        null=True,
        )
    """
    """

    int_id = models.CharField(
        _("internal id"),
        max_length=100,
        editable=False,
        null=True,
        )
    """
    """

    slug = models.SlugField(
        _("slug"),
        unique=True,
        editable=False,
        null=True,
        )
    """
    """


    # META
    # -------------------------------------------------------------------------
    class Meta:
        verbose_name = _(constants.APP_NAME[:-1])
        verbose_name_plural = _(constants.APP_NAME)
        unique_together = (constants.INDIVIDUAL_UNIQUE_TOGETHER)
        index_together = (constants.INDIVIDUAL_UNIQUE_TOGETHER)

    # METHODS
    # -------------------------------------------------------------------------

    def __str__(self):
        return self.slug

    def check_institution(self):
        """ Determines whether or not the Individual comes from MSK or not. """
        if self.institution == constants.MSK:
            return 'I'
        else:
            return 'E'

    def _if_new(self, **kwargs):
        """ _if_new is executed the first time the object is created """

        # This function can only be called from save()
        self._check_if_caller_is_save()

        # get internal id
        self._get_int_id()

    def _if_save(self):
        """ _if_save() is executed everytime the object is saved """

        # This function can only be called from save()
        self._check_if_caller_is_save()

        # update object slug
        self.slug = self.int_id

    def _get_int_id(self):
        """ returns Individual internal ID """

        # This function can only be called from _if_new()
        self._check_if_caller_is_if_new()

        # get internal id
        species_id = constants.LEUKID_SPECIES[self.species]
        institution_id = self.check_institution()
        join = [institution_id, species_id, str(self.pk)]
        self.int_id = "-".join(join)
        return self.int_id
