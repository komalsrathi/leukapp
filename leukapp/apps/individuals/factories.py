# -*- coding: utf-8 -*-

# python
import string

# third party
import factory
from factory.fuzzy import FuzzyChoice, FuzzyText

# local
from .models import Individual
from . import constants


class IndividualFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Individual
        django_get_or_create = constants.INDIVIDUAL_UNIQUE_TOGETHER

    institution = FuzzyChoice(constants.INSTITUTION_VALUE)
    species = FuzzyChoice(constants.SPECIES_VALUE)
    ext_id = FuzzyText(length=12, chars=string.hexdigits)
