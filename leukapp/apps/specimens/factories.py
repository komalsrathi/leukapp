# -*- coding: utf-8 -*-

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

    class Meta:
        model = Specimen
        django_get_or_create = constants.SPECIMEN_UNIQUE_TOGETHER

    individual = factory.SubFactory(IndividualFactory)
    source = FuzzyChoice(constants.SOURCE_VALUE)
    source_type = FuzzyChoice(constants.SOURCE_TYPE_VALUE)
    ext_id = FuzzyText(length=12, chars=string.hexdigits)
