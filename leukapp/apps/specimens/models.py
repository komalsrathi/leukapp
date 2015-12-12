# -*- coding: utf-8 -*-

"""
Models/database schemas for the :mod:`~leukapp.apps.specimens` application.

See `Django's Model Documentation`_ for more information.

.. _Django's Model Documentation:
    https://docs.djangoproject.com/en/1.9/topics/db/models/
"""

# django imports
from django.db import models
from django.utils.translation import ugettext_lazy as _

# apps imports
from leukapp.apps.core.constants import UNKNOWN
from leukapp.apps.core.models import LeukappModel
from leukapp.apps.core.validators import ext_id_validator
from leukapp.apps.individuals.models import Individual

# local imports
from . import constants


class Specimen(LeukappModel):

    """
    :class:`Individual's <leukapp.apps.individuals.models.Individual>` tissue
    collected on a particular day and location.
    """

    #: Name of the application where :class:`Specimen` is contained.
    APP_NAME = constants.APP_NAME

    # EXTERNAL FIELDS
    # =========================================================================
    individual = models.ForeignKey(
        Individual,
        verbose_name=_("individual"),
        )
    """
    `ForeignKey`_ to the :class:`~leukapp.apps.individuals.models.Individual`
    model.

    .. _ForeignKey: https://docs.djangoproject.com/en/1.8/topics/db/examples/many_to_one/#many-to-one-relationships
    """

    ext_id = models.CharField(
        verbose_name=_("external id"),
        validators=[ext_id_validator],
        default=UNKNOWN,
        max_length=100,
        blank=True,
        help_text=_(
            "The external id should be unique at the Individual "
            "and Source type levels."
            ),
        )
    """
    ID used by the Institution or Scientist to track the
    :class:`.Specimen`.

    The default value is :data:`~leukapp.apps.core.constants.UNKNOWN`
    because it's likely that scientist don't know this ID.

    .. important:: Only one ``UNKNOWN`` Specimen is allowed.
    """

    source = models.CharField(
        verbose_name=_("source"),
        choices=constants.SPECIMEN_CHOICES["SOURCE"],
        max_length=100,
        blank=True,
        null=True,
        )
    """
    Source of the tissue. See :data:`~.constants.SOURCE` for
    available choices.
    """

    source_type = models.CharField(
        verbose_name=_("source_type"),
        choices=constants.SPECIMEN_CHOICES["SOURCE_TYPE"],
        max_length=100,
        null=True,
        )
    """
    Type of the specimen, whether it's NORMAL or TUMOR.
    See :data:`~.constants.SOURCE` for available choices.
    """

    order = models.PositiveSmallIntegerField(
        verbose_name=_("desired order"),
        default=0,
        blank=True,
        null=True,
        )
    """
    This field is used in the :class:`~leukapp.apps.leukforms.models.Leukform`
    submission to sort ``Specimens`` so their **leukid** follows a sequential
    order.
    """

    # INTERNAL FIELDS
    # =========================================================================
    aliquots_count = models.PositiveSmallIntegerField(
        verbose_name=_("number of aliquots created"),
        default=0,
        editable=False,
        null=True,
        )
    """
    Count of the total number of
    :class:`aliquots <leukapp.apps.aliquots.models.Aliquot>`
    that has been linked to the current :class:`Specimen`.
    """

    int_id = models.CharField(
        verbose_name=_("internal id"),
        max_length=8,
        editable=False,
        null=True,
        )
    """
    Internal ID used to describe the :class:`Specimen` instance.

    This value is generated by :meth:`_get_int_id` and it includes the position
    ``[4]`` of the **leukid** (e.g. ``T1``):

    4.  ``T1`` indicates that the current :class:`Specimen` is the first
        **TUMOR** extracted from the parent
        :class:`~leukapp.apps.individuals.models.Individual`. The letter is
        assigned according the :data:`~.constants.INT_ID_SOURCE_TYPE` variable.

    .. important::
        The :attr:`int_id` is generated only once. If there was a mistake a new
        :class:`Specimen` instance must be created.
    """

    slug = models.SlugField(
        verbose_name=_("slug"),
        unique=True,
        editable=False,
        null=True,
        )
    """
    :class:`Specimen's <.Specimen>` unique identifier (**leukid**).

    The :attr:`int_id` is added to the ``Individual.slug`` to generate the
    Specimen's :attr:`slug`.

    .. important::
        As the :attr:`int_id`, the :attr:`slug` is generated only once. If
        there was a mistake a new :class:`Specimen` instance must be created.
    """

    # META CLASS
    # =========================================================================
    class Meta:
        verbose_name = _(constants.APP_NAME[:-1])
        verbose_name_plural = _(constants.APP_NAME)
        unique_together = (constants.SPECIMEN_UNIQUE_TOGETHER)
        index_together = (constants.SPECIMEN_UNIQUE_TOGETHER)

    # PUBLIC METHODS
    # =========================================================================
    def __str__(self):
        """
        Returns the :attr:`slug` when ``str`` is requested.
        """
        return self.slug

    # PRIVATE METHODS
    # =========================================================================
    def _if_new(self, **kwargs):
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
        self._get_int_id()
        self.slug = '-'.join([self.individual.slug, self.int_id])

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

        # when blank is submitted, save UNKNOWN instead
        if self.ext_id == '':
            self.ext_id = UNKNOWN

    def _get_int_id(self):
        """
        Computes the :attr:`int_id`.

        The :attr:`int_id` generation is based on a count of ``Specimens`` per
        :class:`~leukapp.apps.individuals.models.Individual`.

        Steps:

            * Check if the caller function is :meth:`_if_new()`.
            * Retrieve the ID character assigned to the ``source_type`` field.
              updates the specimens count, saves the Parent class,
              and builds the ID (e.g. ``T1``).

        .. note::
            This method can only be called from
            :meth:`_if_new` and is protected by
            :meth:`~leukapp.apps.core.models.LeukappModel._check_if_caller_is_if_new`.
        """
        self._check_if_caller_is_if_new()

        source_type_id = constants.INT_ID_SOURCE_TYPE[self.source_type]
        if self.source_type == constants.TUMOR:
            self.individual.tumors_count += 1
            self.int_id = source_type_id + str(self.individual.tumors_count)
        elif self.source_type == constants.NORMAL:
            self.individual.normals_count += 1
            self.int_id = source_type_id + str(self.individual.normals_count)
        self.individual.save()
        return self.int_id
