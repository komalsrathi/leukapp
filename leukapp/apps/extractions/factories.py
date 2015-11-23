# -*- coding: utf-8 -*-

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
    Creates an :class:`~leukapp.apps.extractions.models.Extraction` instance.

    Mainly used for testing purposes. If no keyword arguments are provided,
    ``ExtractionFactory`` will generate the appropriate attributes using the
    rules described in the attributes definition. For more information see:
    `DjangoModelFactory`_.

    .. _DjangoModelFactory:
        https://factoryboy.readthedocs.org/en/latest/orms.html#factory.django.DjangoModelFactory

    .. returns
    :return: :class:`~leukapp.apps.extractions.models.Extraction` instance.

    Examples::

        # No arguments, attributes will be assigned randomly
        extraction = ExtractionFactory()

        # Passing specific values to specific attributes
        extraction = ExtractionFactory(aliquot=AliquotFactory(), analyte='DNA')

        # passing a list of projects for ManyToMany relationship
        projects = [ProjectFactory() for i in range(3)]
        extraction = ExtractionFactory(analyte=DNA, projects=projects)

    .. warning::
        Everytime ``ExtractionFactory`` is used without passing the ``Aliquot``
        attribute, a new aliquot and its parents will be created recursively.

    .. seealso::
        :func:`~leukapp.apps.extractions.models.Extraction`
        :func:`~leukapp.apps.aliquots.models.Aliquot`
        :func:`~leukapp.apps.aliquots.factories.AliquotFactory`
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
    By default, this attribute is set to ``''``. However, pass a string with
    :class:`~leukapp.apps.projects.models.Project`s pks separated by the ``|``
    character to link the :class:`~leukapp.apps.extractions.models.Extraction`
    instance to one or more :class:`~leukapp.apps.projects.models.Project`s.
    To understand better this behavior see:
    :method:`~leukapp.apps.extractions.models.Extraction._get_projects_from_string`.
    """

    @factory.post_generation
    def projects(self, create, extracted, **kwargs):
        """
        Pass a list of projects to create ManyToMany relationship. To learn
        more see Factory's documentation for `simple ManyToMany relationship`_.

        .. _simple ManyToMany relationship: https://factoryboy.readthedocs.org/en/latest/recipes.html#simple-many-to-many-relationship
        """
        if not create:  # Simple build, do nothing.
            return
        if extracted:   # A list of project were passed in, use them
            [self.projects.add(p) for p in extracted]


# ROUTINE PROTECTION
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    pass
