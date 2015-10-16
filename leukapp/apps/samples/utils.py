# -*- coding: utf-8 -*-

# python
import random
import os
import datetime
import csv
import string

# django
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings

# third party
import factory
from factory.fuzzy import FuzzyChoice, FuzzyText

# leukapp
from leukapp.apps.individuals.utils import IndividualFactory
from leukapp.apps.specimens.utils import SpecimenFactory
from leukapp.apps.aliquots.utils import AliquotFactory
from .constants import LEUKFORM_FIELDS

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


class LeukformFactory(object):

    """
    Class used as a samples factory.

    Attributes:
        `individuals`: list of all individuals created
        `specimens`: list of all specimens created
        `aliquots`: list of all aliquots created
        `rows`: simulates the leukform
    """

    def __init__(self):
        super(LeukformFactory, self).__init__()
        self.individuals = []
        self.specimens = []
        self.aliquots = []
        self.samples = []
        self.rows = []

    def create_batch(self, i, s, a, sa):
        """
        Creates a batch of samples.

        Input Args:
            i (int): number of individuals
            s (int): number of specimens per individual
            a (int): number of aliquots per specimen
            sa (int): number of samples per aliquot
        Raises:
            not defined yet

        tests: test_samples_factory_create_batch
        """
        self.individuals += IndividualFactory.create_batch(i)

        for individual in self.individuals:
            kwargs = {'individual': individual}
            self.specimens += SpecimenFactory.create_batch(s, **kwargs)

        for specimen in self.specimens:
            kwargs = {'specimen': specimen}
            self.aliquots += AliquotFactory.create_batch(a, **kwargs)

        for aliquot in self.aliquots:
            kwargs = {'aliquot': aliquot}
            self.samples += SampleFactory.create_batch(sa, **kwargs)

    def create_rows(self):
        """
        rows simulates the leukform

        Raises:
            ImproperlyConfigured("create rows first")
        tests: test_samples_factory_create_rows
        """

        if not self.individuals:
            raise ImproperlyConfigured("create batch first")

        for i in self.individuals:
            for s in i.specimen_set.all():
                for a in s.aliquot_set.all():
                    for sa in a.sample_set.all():
                        row = {
                            'Project.pk': str(random.randint(1, 1000)),
                            'Individual.institution': i.institution,
                            'Individual.species': i.species,
                            'Individual.ext_id': i.ext_id,
                            'Specimen.source': s.source,
                            'Specimen.source_type': s.source_type,
                            'Specimen.ext_id': s.ext_id,
                            'Aliquot.bio_source': a.bio_source,
                            'Aliquot.ext_id': a.ext_id,
                            'Sample.platform': sa.platform,
                            'Sample.technology': sa.technology,
                            'Sample.center': sa.center,
                            'Sample.ext_id': sa.ext_id,
                            }
                        self.rows.append(row)

    def create_csv_from_rows(self):
        """
        Creates a csv from rows.

        Returns:
            Path of csv
        Raises:
            ImproperlyConfigured("create rows first")
        tests: test_csv_from_rows
        """
        if not self.rows:
            raise ImproperlyConfigured("create rows first")

        timestamp = datetime.datetime.now().isoformat()
        file_name = 'test_leukform_' + timestamp + '.csv'
        path = os.path.join(settings.MEDIA_ROOT, 'csv', 'outrows', file_name)
        keys = LEUKFORM_FIELDS

        with open(path, 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(self.rows)

        return path
