# -*- coding: utf-8 -*-

# python
import string

# third party
import factory
from factory.fuzzy import FuzzyText

# local
from .models import User
from . import constants


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User
        django_get_or_create = constants.USER_UNIQUE_TOGETHER

    first_name = FuzzyText(length=3, chars=string.ascii_lowercase)
    last_name = FuzzyText(length=3, chars=string.ascii_lowercase)
    email = factory.LazyAttribute(lambda obj: '%s@mskcc.org' % obj.first_name)
    phone = FuzzyText(length=10, chars=string.digits)
