# -*- coding: utf-8 -*-

# python
import string

# third party
import factory
from factory.fuzzy import FuzzyChoice, FuzzyText

# leukapp
from leukapp.apps.aliquots.factories import AliquotFactory

# local
from .models import Run
from . import constants


class RunFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Run
        django_get_or_create = constants.RUN_UNIQUE_TOGETHER

    aliquot = factory.SubFactory(AliquotFactory)
    analyte = FuzzyChoice(constants.ANALYTE_VALUE)
    platform = FuzzyChoice(constants.PLATFORM_VALUE)
    technology = FuzzyChoice(constants.TECHNOLOGY_VALUE)
    center = FuzzyChoice(constants.CENTER_VALUE)
    ext_id = FuzzyText(length=12, chars=string.hexdigits)
    projects_list = ''

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
