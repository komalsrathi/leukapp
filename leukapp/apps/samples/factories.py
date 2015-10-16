# -*- coding: utf-8 -*-

# python
import string

# third party
import factory
from factory.fuzzy import FuzzyChoice, FuzzyText

# leukapp
from leukapp.apps.aliquots.factories import AliquotFactory
from leukapp.apps.projects.factories import ProjectFactory

# local
from .models import Sample
from . import constants


class SampleFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Sample
        django_get_or_create = constants.SAMPLE_GET_OR_CREATE_FIELDS

    aliquot = factory.SubFactory(AliquotFactory)
    platform = FuzzyChoice(constants.PLATFORM_SHORT)
    technology = FuzzyChoice(constants.TECHNOLOGY_SHORT)
    center = FuzzyChoice(constants.CENTER_SHORT)
    ext_id = FuzzyText(length=12, chars=string.hexdigits)

    @factory.post_generation
    def projects(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of project were passed in, use them
            for project in extracted:
                self.projects.add(project)
        # else:
        #     [self.projects.add(ProjectFactory()) for i in range(3)]
