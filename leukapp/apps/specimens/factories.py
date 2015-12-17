# -*- coding: utf-8 -*-

"""Factories for the :mod:`~leukapp.apps.specimens` application."""

# python
import string

# third party
import factory
from factory.fuzzy import FuzzyChoice, FuzzyText

# leukapp
from leukapp.apps.individuals.factories import IndividualFactory

# local
from .models import Specimen
from . import constants


class SpecimenFactory(factory.django.DjangoModelFactory):

    """Class used to generate specimen objects."""

    class Meta:
        model = Specimen
        django_get_or_create = constants.SPECIMEN_UNIQUE_TOGETHER

    #: If this field isn't provided, it generates a new Individual object.
    individual = factory.SubFactory(IndividualFactory)

    #: Randomly selected from :data:`.constants.SOURCE`.
    source = FuzzyChoice([e[0] for e in constants.SOURCE])

     #: Randomly selected from :data:`.constants.SOURCE_TYPE`.
    source_type = FuzzyChoice([e[0] for e in constants.SOURCE_TYPE])

    #: Random 12 digits string.
    ext_id = FuzzyText(length=12, chars=string.hexdigits)
