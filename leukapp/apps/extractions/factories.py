# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: leukapp.apps.extractions

Testing factories for the :mod:`~leukapp.apps.extractions`. This module relies
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

    :param Aliquot aliquot: The ``Extraction's`` parent model.
    :param str analyte: See :data:`~.constants.ANALYTE` for choices.
    :param str ext_id: ID used extrernally to track the ``Extraction``.
    :return: :class:`~models.Extraction` instance.

    Examples::

        # No arguments, attributes will be assigned randomly
        extraction = ExtractionFactory()

        # Passing specific values to specific attributes
        extraction = ExtractionFactory(aliquot=AliquotFactory(), analyte='DNA')

    .. warning::
        Everytime ``ExtractionFactory`` is used without passing the
        :attr:`~ExtractionFactory.aliquot` attribute, a new
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

    analyte = FuzzyChoice([e[0] for e in constants.ANALYTE])
    """
    If not passed, picks a random choice from :data:`~.constants.ANALYTE`.
    To learn more see `FuzzyChoice`_.

    .. _FuzzyChoice:
        https://factoryboy.readthedocs.org/en/latest/fuzzy.html#fuzzychoice
    """

    ext_id = FuzzyText(length=12, chars=string.hexdigits)
    """
    If not passed, creates a random ID. To learn more see `FuzzyText`_.

    .. _FuzzyText:
        https://factoryboy.readthedocs.org/en/latest/fuzzy.html#fuzzytext
    """


# ROUTINE PROTECTION
# =============================================================================

if __name__ == '__main__':
    pass
