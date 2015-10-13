# -*- coding: utf-8 -*-

# python
import string

# third party
import factory
from factory.fuzzy import FuzzyChoice, FuzzyText

# leukapp
from leukapp.apps.specimens.models import Specimen

# local
from .models import Aliquot
from . import constants


class AliquotFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Aliquot
        django_get_or_create = constants.ALIQUOT_GET_OR_CREATE_FIELDS

    specimen = factory.Iterator(Specimen.objects.all())
    biological_material = FuzzyChoice(constants.BIOLOGICAL_MATERIAL_SHORT)
    ext_id = FuzzyText(length=12, chars=string.hexdigits)
