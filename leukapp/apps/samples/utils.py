# -*- coding: utf-8 -*-

# python
import random
import os
import datetime
import csv

# django
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings

# leukapp
from leukapp.apps.individuals.utils import IndividualFactory
from leukapp.apps.specimens.utils import SpecimenFactory
from leukapp.apps.aliquots.utils import AliquotFactory
from .constants import LEUKFORM_FIELDS


class SamplesFactory(object):

    """
    Class used as a samples factory.

    Attributes:
        `individuals`: list of all individuals created
        `specimens`: list of all specimens created
        `aliquots`: list of all aliquots created
        `rows`: simulates the leukform
    """

    def __init__(self):
        super(SamplesFactory, self).__init__()
        self.individuals = []
        self.specimens = []
        self.aliquots = []
        self.rows = []

    def create_batch(self, i, s, a):
        """
        Creates a batch of samples.

        Input Args:
            i (int): number of individuals
            s (int): number of specimens per individual
            a (int): number of aliquots per specimen
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
                    row = {
                        'Project.pk': str(random.randint(1, 1000)),
                        'Individual.institution': i.institution,
                        'Individual.species': i.species,
                        'Individual.ext_id': i.ext_id,
                        'Specimen.source': s.source,
                        'Specimen.ext_id': s.ext_id,
                        'Aliquot.bio_source': a.bio_source,
                        'Aliquot.ext_id': a.ext_id,
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
