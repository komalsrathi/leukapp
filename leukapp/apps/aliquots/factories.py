
"""Aliquot objects factory."""

# python
import string

# third party
import factory
from factory.fuzzy import FuzzyText

# leukapp
from leukapp.apps.specimens.factories import SpecimenFactory

# local
from .models import Aliquot
from . import constants


class AliquotFactory(factory.django.DjangoModelFactory):

    """Create Aliquot instance."""

    class Meta:
        model = Aliquot
        django_get_or_create = constants.ALIQUOT_UNIQUE_TOGETHER

    specimen = factory.SubFactory(SpecimenFactory)
    ext_id = FuzzyText(length=12, chars=string.hexdigits)
