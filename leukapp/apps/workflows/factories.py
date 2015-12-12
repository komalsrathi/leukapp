# -*- coding: utf-8 -*-

"""
.. currentmodule::
    leukapp.apps.workflows

Testing factories for the :mod:`~leukapp.apps.workflows`. This module relies
heavily on the `factory_boy`_ python package.

.. _factory_boy: https://factoryboy.readthedocs.org/en/latest/

"""

# python
import string
import random

# third party
import factory
from factory.fuzzy import FuzzyChoice, FuzzyText

# leukapp
from leukapp.apps.extractions.factories import ExtractionFactory

# local
from .models import Workflow
from . import constants


class WorkflowFactory(factory.django.DjangoModelFactory):

    """
    Creates an :class:`~models.Workflow` instance.

    Mainly used for testing purposes. If no keyword arguments are provided,
    this class will generate the appropriate field values using the
    rules described in the **attributes**. For more information see:
    `DjangoModelFactory`_.

    .. Attributes

    :param Extraction extraction: ForeignKey to the ``Extraction`` model.
    :param str ext_id: Sequencing Center's ID to track the ``Workflow``.
    :param list projects: list of ``Projects`` to be linked.
    :param str projects_string: String used to link projects to workflows.
    :param str sequencing_center: Sequencing center name.
    :param str sequencing_technology: Sequencing technology name.
    :param str technology_type: Sequencing technology type.
    :param str sequencing_platform: Sequencing platform used.
    :param str read_length: Workflow's read length.
    :param str read_type: Workflow's read type.

    .. Returns

    :return: :class:`~models.Workflow` instance.

    Examples::

        # No arguments, attributes will be assigned randomly
        workflow = WorkflowFactory()

        # Passing specific values to specific attributes
        workflow = WorkflowFactory(extraction=ExtractionFactory())

        # passing a list of projects for ManyToMany relationship
        projects = [ProjectFactory() for i in range(3)]
        workflow = WorkflowFactory(analyte=DNA, projects=projects)

    .. warning::
        Everytime ``WorkflowFactory`` is used without passing the
        :attr:`~factories.WorkflowFactory.aliquot` attribute, a new
        :class:`~leukapp.apps.extractions.models.Extraction` and its parents:
        :class:`~leukapp.apps.aliquots.models.Aliquot`,
        :class:`~leukapp.apps.specimens.models.Specimen` and
        :class:`~leukapp.apps.individuals.models.Individual`) will be created.

    .. _DjangoModelFactory:
        https://factoryboy.readthedocs.org/en/latest/orms.html#factory.django.DjangoModelFactory

    """

    class Meta:
        model = Workflow
        django_get_or_create = constants.WORKFLOW_UNIQUE_TOGETHER

    extraction = factory.SubFactory(ExtractionFactory)
    """
    If not passed, creates a new :class:`~leukapp.apps.aliquots.models.Aliquot`
    instance. To learn more see `SubFactory`_.

    .. _SubFactory:
        https://factoryboy.readthedocs.org/en/latest/reference.html#factory.SubFactory
    """

    ext_id = FuzzyText(length=12, chars=string.hexdigits)
    """
    If not passed, creates a random ID. To learn more see `FuzzyText`_.

    .. _FuzzyText:
        https://factoryboy.readthedocs.org/en/latest/fuzzy.html#fuzzytext
    """

    projects_string = ''
    """
    By default, this attribute is set to ``''``. However, pass a string with
    :class:`Projects <leukapp.apps.projects.models.Project>` primary keys
    separated by a ``|`` character to link the new :class:`~.models.Workflow`
    and the projects. To understand better this behavior see:
    :meth:`~.models.Workflow._get_projects_from_string`.
    """

    sequencing_platform = FuzzyChoice([e[0] for e in constants.PLATFORM])
    """
    If not passed, picks a random choice from :data:`~.constants.PLATFORM`.
    To learn more see `FuzzyChoice`_.

    .. _FuzzyChoice:
        https://factoryboy.readthedocs.org/en/latest/fuzzy.html#fuzzychoice
    """

    sequencing_center = FuzzyChoice([e[0] for e in constants.CENTER])
    """
    If not passed, picks a random choice from :data:`~.constants.CENTER`.
    To learn more see `FuzzyChoice`_.

    .. _FuzzyChoice:
        https://factoryboy.readthedocs.org/en/latest/fuzzy.html#fuzzychoice
    """

    read_length = FuzzyChoice([e[0] for e in constants.READ_LENGTH])
    """
    If not passed, picks a random choice from :data:`~.constants.READ_LENGTH`.
    To learn more see `FuzzyChoice`_.

    .. _FuzzyChoice:
        https://factoryboy.readthedocs.org/en/latest/fuzzy.html#fuzzychoice
    """

    read_type = FuzzyChoice([e[0] for e in constants.READ_TYPE])
    """
    If not passed, picks a random choice from :data:`~.constants.READ_TYPE`.
    To learn more see `FuzzyChoice`_.

    .. _FuzzyChoice:
        https://factoryboy.readthedocs.org/en/latest/fuzzy.html#fuzzychoice
    """

    # LAZY ATTRIBUTES
    # =========================================================================

    sequencing_technology = None
    """
    If not passed, picks a random choice from
    :data:`~.constants.INT_ID_TECHNOLOGY`
    using the method :meth:`sequencing_technology`.
    To learn more see the `lazy_attribute`_ decorator.

    .. _lazy_attribute:
        http://factoryboy.readthedocs.org/en/latest/reference.html?highlight=container#decorator
    """

    @factory.lazy_attribute
    def sequencing_technology(self):
        technologies = constants.INT_ID_TECHNOLOGY[self.extraction.analyte]
        return random.choice(list(technologies))

    technology_type = None
    """
    If not passed, picks a random choice from
    :data:`~.constants.INT_ID_TECHNOLOGY`
    using the method :meth:`technology_type`.
    To learn more see the `lazy_attribute`_ decorator.

    .. _lazy_attribute:
        http://factoryboy.readthedocs.org/en/latest/reference.html?highlight=container#decorator
    """

    @factory.lazy_attribute
    def technology_type(self):
        technologies = constants.INT_ID_TECHNOLOGY[self.extraction.analyte]
        technology_types = list(technologies[self.sequencing_technology])
        technology_types.remove("DEFAULT_TECHNOLOGY")
        return random.choice(technology_types)

    # POST GENERATED ATTRIBUTES
    # =========================================================================

    projects = None
    """
    Pass a list of projects to create ManyToMany relationships. To learn
    more see Factory's documentation for `simple ManyToMany relationship`_.

    .. _simple ManyToMany relationship: https://factoryboy.readthedocs.org/en/latest/recipes.html#simple-many-to-many-relationship
    """

    @factory.post_generation
    def projects(self, create, extracted, **kwargs):
        if not create:  # Simple build, do nothing.
            return
        if extracted:   # A list of project were passed in, use them
            [self.projects.add(p) for p in extracted]


# ROUTINE PROTECTION
# =============================================================================

if __name__ == '__main__':
    pass
