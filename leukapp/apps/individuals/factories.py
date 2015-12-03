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

    institution = FuzzyChoice([e[0] for e in constants.INSTITUTION])
    species = FuzzyChoice([e[0] for e in constants.SPECIES])
    ext_id = FuzzyText(length=12, chars=string.hexdigits)
