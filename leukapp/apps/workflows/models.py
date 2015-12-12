# -*- coding: utf-8 -*-

"""
Models/database schemas for the :mod:`~leukapp.apps.workflows`
application.

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
from leukapp.apps.core.db import CharNullField
from leukapp.apps.core.constants import UNKNOWN, DEFAULT
from leukapp.apps.extractions.models import Extraction
from leukapp.apps.projects.models import Project

# local
from . import constants
from . import validators


class Workflow(LeukappModel):

    """
    :class:`Extraction's <leukapp.apps.extractions.models.Extraction>`
    sequence workflow.
    """

    #: Name of the application where :class:`Workflow` is contained.
    APP_NAME = constants.APP_NAME

    # EXTERNAL FIELDS
    # =========================================================================
    extraction = models.ForeignKey(
        Extraction,
        verbose_name=_("extraction"),
        null=True,
        )
    """
    `ForeignKey`_ to the :class:`~leukapp.apps.extractions.models.Extraction`
    model.

    .. _ForeignKey: https://docs.djangoproject.com/en/1.8/topics/db/examples/many_to_one/#many-to-one-relationships
    """

    ext_id = CharNullField(
        verbose_name=_("Extraction ID provided by sequencing center."),
        max_length=100,
        validators=[ext_id_validator],
        default=UNKNOWN,
        blank=True,
        null=True,
        )
    """
    ID used by the sequencing :data:`~.constants.CENTER` to identify the
    :class:`.Workflow`.

    The default value is :data:`~leukapp.apps.core.constants.UNKNOWN`
    because most likely, scientist don't know this ID when they are submitting
    :class:`Workflows <.Workflow>` to **leukgen**.

    .. important::
        This field is a :class:`~leukapp.apps.core.db.CharNullField`. This
        particular field class enables the ability to have multiple NULL
        values but unique non-NULL records.
    """

    # PROJECTS
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    projects = models.ManyToManyField(
        Project,
        verbose_name=_("projects"),
        blank=True,
        )
    """
    Many to many relationship with the model
    :class:`~leukapp.apps.projects.models.Project`.
    """

    projects_string = models.CharField(
        verbose_name=_("list of projetcs"),
        max_length=100,
        validators=[validators.projects_string_validator],
        help_text=_("Include the projects keys separated by a '|' character"),
        blank=True,
        null=True,
        )
    """
    String used by :meth:`_get_projects_from_string` to link
    :class:`Projects <leukapp.apps.projects.models.Project>` and
    :class:`Workflows <.Workflow>`::

        # This will add projects 101 and 102 to Workflow when saving
        projects_string = '101|102|103'
    """

    # SEQUENCING WORKFLOW
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    sequencing_center = models.CharField(
        verbose_name=_("sequencing center"),
        max_length=100,
        choices=constants.WORKFLOW_CHOICES["CENTER"],
        null=True,
        )
    """
    See choices: :data:`~.constants.CENTER`.
    """

    sequencing_technology = models.CharField(
        verbose_name=_("sequencing technology"),
        choices=constants.WORKFLOW_CHOICES["TECHNOLOGY"],
        max_length=100,
        null=True,
        )
    """
    See choices: :data:`~.constants.TECHNOLOGY`.
    """

    technology_type = models.CharField(
        verbose_name=_("sequencing technology type"),
        choices=constants.WORKFLOW_CHOICES["TECHNOLOGY_TYPE"],
        default=DEFAULT,
        max_length=100,
        null=True,
        )
    """
    See choices: :data:`~.constants.TECHNOLOGY_TYPE`.
    """

    sequencing_platform = models.CharField(
        verbose_name=_("sequencing platform"),
        choices=constants.WORKFLOW_CHOICES["PLATFORM"],
        max_length=100,
        null=True,
        )
    """
    Sequencing :data:`~.constants.PLATFORM`.
    """

    read_length = models.CharField(
        verbose_name=_("read length"),
        choices=constants.WORKFLOW_CHOICES["READ_LENGTH"],
        max_length=100,
        null=True,
        )
    """
    See choices: :data:`~.constants.READ_LENGTH`.
    """

    read_type = models.CharField(
        verbose_name=_("read type"),
        choices=constants.WORKFLOW_CHOICES["READ_TYPE"],
        max_length=100,
        null=True,
        )
    """
    See choices: :data:`~.constants.READ_TYPE`.
    """

    # INTERNAL FIELDS
    # =========================================================================
    int_id = models.CharField(
        verbose_name=_("internal ID"),
        max_length=100,
        editable=False,
        null=True,
        )
    """
    Internal ID used to describe the :class:`Workflow` object.

    This value is generated by :meth:`_get_int_id` and it includes positions
    ``[7-11]`` of the **leukid** (e.g. ``1-1A-S100-x10-CMO``):

    7.  ``1`` count of ``Workflows`` per ``Extraction``, see
        :attr:`~leukapp.apps.extractions.models.Extraction.workflows_count`.
    8.  ``1A`` :attr:`technology`/:attr:`technology_type` internal code based
        on the custom dictionary :data:`~.constants.INT_ID_TECHNOLOGY`.
    9.  ``S100`` Internal code for the :attr:`read_length` / :attr:`read_type`
        combination. See :data:`~.constants.INT_ID_READ_LENGTH` and
        :data:`~.constants.INT_ID_READ_TYPE`.
    10.  ``X10`` :attr:`sequencing_platform` internal code. See
         :data:`~.constants.INT_ID_PLATFORM`.
    11.  ``CMO`` :attr:`sequencing_center` internal code. See
         :data:`~.constants.INT_ID_CENTER`.

    .. important::
        The :attr:`int_id` is generated only once. If there was a mistake a new
        :class:`Workflow` instance must be created.
    """

    slug = models.SlugField(
        verbose_name=_("slug"),
        unique=True,
        editable=False,
        null=True,
        )
    """
    :class:`Workflow's <.Workflow>` unique identifier (**leukid**).

    The :attr:`int_id` is added to the ``Aliquot.slug`` to generate the
    :attr:`slug`.

    .. important::
        As the :attr:`int_id`, the :attr:`slug` is generated only once. If
        there was a mistake a new :class:`Workflow` instance must be created.
    """

    # META CLASS
    # =========================================================================
    class Meta:
        verbose_name = _(constants.APP_NAME[:-1])
        verbose_name_plural = _(constants.APP_NAME)
        unique_together = (constants.WORKFLOW_UNIQUE_TOGETHER)
        index_together = (constants.WORKFLOW_UNIQUE_TOGETHER)

    # PUBLIC METHODS
    # =========================================================================
    def __str__(self):
        """
        Returns the :attr:`slug` when ``str`` is requested.
        """
        return self.slug

    def clean(self):
        """
        Calls parent ``Model.clean()`` method and validates the
        analyte/sequencing_technology/technology_type combination. This
        function will also handle errors during form submissions.

        .. todo:: add test to determine if this methods is called in forms.
        """
        cleaned_data = super(Workflow, self).clean()

        # validates analyte/sequencing_technology/technology_type combination.
        kwargs = {
            'analyte': self.extraction.analyte,
            'sequencing_technology': self.sequencing_technology,
            'technology_type': self.technology_type,
            }
        validators.technology_type_validator(**kwargs)

        return cleaned_data

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
        self.slug = '-'.join([self.extraction.slug, self.int_id])

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
        self._get_projects_from_string()

    def _get_projects_from_string(self):
        """
        Links :class:`Workflows <.Workflow>` to
        :class:`Projects <leukapp.apps.projects.models.Project>`` using
        :attr:`projects_string`.

        Projects primary keys (``pk``s) must be separated by a ``|`` character.
        """
        try:
            projects = [int(p) for p in self.projects_string.split("|")]
            [self.projects.add(p) for p in projects]
        except Exception:
            pass

    def _get_int_id(self):
        """
        Computes the :attr:`int_id`.

        The :attr:`int_id` generation is based on a count of ``Workflows``
        per :class:`~leukapp.apps.extractions.models.Extraction`, and the
        sequencing setting.

        Steps:

        * Check if the caller function is :meth:`~Workflow._if_new`.
        * if ``technology_type`` is ``DEFAULT``, replace for default value.
        * validates analyte/sequencing_technology/technology_type combination.
        * ``1``: adds count of ``Workflows`` per ``Extraction`` section.
        * ``1A``: adds the :attr:`technology`/:attr:`technology_type` section.
        * ``S100``: adds the :attr:`read_length`/:attr:`read_type` section.
        * ``X10``: adds the :attr:`sequencing_platform` internal code section.
        * ``CMO``: adds the :attr:`sequencing_center` internal code section.

        .. note::
            This method can only be called from
            :meth:`~Workflow._if_new` and is protected by
            :meth:`~leukapp.apps.core.models.LeukappModel._check_if_caller_is_if_new`.
        """
        self._check_if_caller_is_if_new()

        # set default value to technology_type incase it wasn't provided
        if (not self.technology_type) or (self.technology_type == DEFAULT):
            technologies = constants.INT_ID_TECHNOLOGY[self.extraction.analyte]
            technology_types = technologies[self.sequencing_technology]
            self.technology_type = technology_types["DEFAULT_TECHNOLOGY"]

        # validates analyte/sequencing_technology/technology_type combination
        self.clean()

        # ``1`` workflows count section
        self.extraction.workflows_count += 1
        self.int_id = str(self.extraction.workflows_count) + '-'
        self.extraction.save()

        # ``1A`` technology and technology type section
        technologies = constants.INT_ID_TECHNOLOGY[self.extraction.analyte]
        technology_types = technologies[self.sequencing_technology]
        technology_code = technology_types[self.technology_type]
        self.int_id += technology_code + '-'

        # ``S100`` read_length and read_type section.
        read_type_code = constants.INT_ID_READ_TYPE[self.read_type]
        read_lentgh_code = constants.INT_ID_READ_LENGTH[self.read_length]
        self.int_id += read_type_code + read_lentgh_code + '-'

        # ``X10`` platform section.
        platform_code = constants.INT_ID_PLATFORM[self.sequencing_platform]
        self.int_id += platform_code + '-'

        # ``CMO`` sequencing center section.
        center_code = constants.INT_ID_CENTER[self.sequencing_center]
        self.int_id += center_code

        return self.int_id
