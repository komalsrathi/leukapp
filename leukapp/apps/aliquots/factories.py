# -*- coding: utf-8 -*-

# python
import string

# third party
import factory
from factory.fuzzy import FuzzyChoice, FuzzyText

# leukapp
from leukapp.apps.specimens.factories import SpecimenFactory

# local
from .models import Aliquot
from . import constants


class AliquotFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Aliquot
        django_get_or_create = constants.ALIQUOT_UNIQUE_TOGETHER

    specimen = factory.SubFactory(SpecimenFactory)
    bio_source = FuzzyChoice(constants.BIO_SOURCE_SHORT)
    ext_id = FuzzyText(length=12, chars=string.hexdigits)
