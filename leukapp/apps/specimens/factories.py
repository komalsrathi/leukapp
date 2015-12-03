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
    source = FuzzyChoice([e[0] for e in constants.SOURCE])
    source_type = FuzzyChoice([e[0] for e in constants.SOURCE_TYPE])
    ext_id = FuzzyText(length=12, chars=string.hexdigits)
