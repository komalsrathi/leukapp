# -*- coding: utf-8 -*-

# python
import string

# third party
import factory
from factory.fuzzy import FuzzyText

# leukapp
from leukapp.apps.participants.models import Participant

# local
from .models import Project


class ProjectFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Project

    name = FuzzyText(length=10, chars=string.ascii_lowercase)
    description = FuzzyText(length=10, chars=string.ascii_lowercase)
    pi = factory.Iterator(Participant.objects.all())
    analyst = factory.Iterator(Participant.objects.all())
    requestor = factory.Iterator(Participant.objects.all())
    cost_center_no = FuzzyText(length=12, chars=string.hexdigits)
    fund_no = FuzzyText(length=12, chars=string.hexdigits)
    protocol_no = FuzzyText(length=12, chars=string.hexdigits)
