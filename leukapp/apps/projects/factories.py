# -*- coding: utf-8 -*-

# python
import string

# third party
import factory
from factory.fuzzy import FuzzyText

# leukapp
from leukapp.apps.participants.factories import ParticipantFactory

# local
from .models import Project


class ProjectFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Project

    name = FuzzyText(length=10, chars=string.ascii_lowercase)
    description = FuzzyText(length=140, chars=string.ascii_lowercase)
    pi = factory.SubFactory(ParticipantFactory)
    analyst = factory.SubFactory(ParticipantFactory)
    requestor = factory.SubFactory(ParticipantFactory)
    cost_center_no = FuzzyText(length=12, chars=string.hexdigits)
    fund_no = FuzzyText(length=12, chars=string.hexdigits)
    protocol_no = FuzzyText(length=12, chars=string.hexdigits)

    @factory.post_generation
    def participants(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of project were passed in, use them
            for participant in extracted:
                self.participants.add(participant)
