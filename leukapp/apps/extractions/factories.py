# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: leukapp.apps.extractions

Testing factories for the :mod:`~leukapp.apps.extractions`. This module relies
heavily on the `factory_boy`_ python package.

.. _factory_boy: https://factoryboy.readthedocs.org/en/latest/

"""

# python
import string

# third party
import factory
from factory.fuzzy import FuzzyChoice, FuzzyText

# leukapp
from leukapp.apps.aliquots.factories import AliquotFactory

# local
from .models import Extraction
from . import constants


class ExtractionFactory(factory.django.DjangoModelFactory):

    """
    .. py:currentmodule:: leukapp.apps.extractions

    Creates an :class:`~models.Extraction` instance.

    Mainly used for testing purposes. If no keyword arguments are provided,
    this class will generate the appropriate field values using the
    rules described in the **attributes**. For more information see:
    `DjangoModelFactory`_.

    :return: :class:`~models.Extraction` instance.

    Examples::

        # No arguments, attributes will be assigned randomly
        extraction = ExtractionFactory()

        # Passing specific values to specific attributes
        extraction = ExtractionFactory(aliquot=AliquotFactory(), analyte='DNA')

        # passing a list of projects for ManyToMany relationship
        projects = [ProjectFactory() for i in range(3)]
        extraction = ExtractionFactory(analyte=DNA, projects=projects)

    .. warning::
        Everytime ``ExtractionFactory`` is used without passing the
        :attr:`~factories.ExtractionFactory.aliquot` attribute, a new
        :class:`~leukapp.apps.aliquots.models.Aliquot` (and its parents
        :class:`~leukapp.apps.specimens.models.Specimen` and
        :class:`~leukapp.apps.individuals.models.Individual`) will be created.

    .. _DjangoModelFactory:
        https://factoryboy.readthedocs.org/en/latest/orms.html#factory.django.DjangoModelFactory

    """

    class Meta:
        model = Extraction
        django_get_or_create = constants.EXTRACTION_UNIQUE_TOGETHER

    aliquot = factory.SubFactory(AliquotFactory)
    """
    If not passed, creates a new :class:`~leukapp.apps.aliquots.models.Aliquot`
    instance. To learn more see `SubFactory`_.

    .. _SubFactory:
        https://factoryboy.readthedocs.org/en/latest/reference.html#factory.SubFactory
    """

    analyte = FuzzyChoice(constants.ANALYTE_VALUE)
    """
    If not passed, picks randomly one choice from
    :data:`~leukapp.apps.extractions.constants.ANALYTE`. To learn more see:
    `FuzzyChoice`_.

    .. _FuzzyChoice:
        https://factoryboy.readthedocs.org/en/latest/fuzzy.html#fuzzychoice
    """

    platform = FuzzyChoice(constants.PLATFORM_VALUE)
    """
    If not passed, picks randomly one choice from
    :data:`~leukapp.apps.extractions.constants.PLATFORM`. To learn more see:
    `FuzzyChoice`_.

    .. _FuzzyChoice:
        https://factoryboy.readthedocs.org/en/latest/fuzzy.html#fuzzychoice
    """

    technology = FuzzyChoice(constants.TECHNOLOGY_VALUE)
    """
    If not passed, picks randomly one choice from
    :data:`~leukapp.apps.extractions.constants.TECHNOLOGY`. To learn more see:
    `FuzzyChoice`_.

    .. _FuzzyChoice:
        https://factoryboy.readthedocs.org/en/latest/fuzzy.html#fuzzychoice
    """

    center = FuzzyChoice(constants.CENTER_VALUE)
    """
    If not passed, picks randomly one choice from
    :data:`~leukapp.apps.extractions.constants.CENTER`. To learn more see:
    `FuzzyChoice`_.

    .. _FuzzyChoice:
        https://factoryboy.readthedocs.org/en/latest/fuzzy.html#fuzzychoice
    """

    ext_id = FuzzyText(length=12, chars=string.hexdigits)
    """
    If not passed, creates a random ID. To learn more see:
    `FuzzyText`_.

    .. _FuzzyText:
        https://factoryboy.readthedocs.org/en/latest/fuzzy.html#fuzzytext
    """

    projects_string = ''
    """
    .. py:currentmodule:: leukapp.apps.extractions

    By default, this attribute is set to ``''``. However, pass a string with
    :class:`Projects <leukapp.apps.projects.models.Project>` primary keys
    separated by a ``|`` character to link the new :class:`~leukapp.apps.
    extractions.models.Extraction` to one or more
    :class:`Projects <leukapp.apps.projects.models.Project>`. To understand
    better this behavior see:
    :meth:`~models.Extraction._get_projects_from_string`.
    """

    projects = None
    """
    Pass a list of projects to create ManyToMany relationship. To learn
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
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    pass
