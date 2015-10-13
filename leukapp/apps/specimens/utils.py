# -*- coding: utf-8 -*-

# python
import string

# third party
import factory
from factory.fuzzy import FuzzyChoice, FuzzyText

# leukapp
from leukapp.apps.individuals.models import Individual

# local
from .models import Specimen
from . import constants


class SpecimenFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Specimen
        django_get_or_create = constants.SPECIMEN_GET_OR_CREATE_FIELDS

    individual = factory.Iterator(Individual.objects.all())
    source = FuzzyChoice(constants.SOURCE_SHORT)
    ext_id = FuzzyText(length=12, chars=string.hexdigits)
