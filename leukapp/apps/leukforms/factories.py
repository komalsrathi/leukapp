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
from leukapp.apps.individuals.factories import IndividualFactory
from leukapp.apps.specimens.factories import SpecimenFactory
from leukapp.apps.aliquots.factories import AliquotFactory
from leukapp.apps.runs.factories import RunFactory
from leukapp.apps.projects.factories import ProjectFactory

# local
from .constants import LEUKFORM_CSV_FIELDS


class LeukformCsvFactory(object):

    """
    Class used as a runs factory.

    Attributes:
        individuals: list of all individuals created
        specimens: list of all specimens created
        aliquots: list of all aliquots created
        rows: simulates the leukform
    """

    def __init__(self):
        super(LeukformCsvFactory, self).__init__()
        self.individuals = []
        self.specimens = []
        self.aliquots = []
        self.runs = []
        self.rows = []
        self.instances = {
            'Individual': self.individuals,
            'Specimen': self.specimens,
            'Aliquot': self.aliquots,
            'Run': self.runs,
            }

    def create_batch(self, individuals, specimens, aliquots, runs):
        """
        Creates a batch of runs.

        Input Args:
            individuals (int): number of individuals
            specimens (int): number of specimens per individual
            aliquots (int): number of aliquots per specimen
            runs (int): number of runs per aliquot
        Raises:
            not defined yet
        """
        projects = [ProjectFactory(name=str(i)) for i in range(10)]
        self.individuals += IndividualFactory.create_batch(individuals)

        for individual in self.individuals:
            kwargs = {'individual': individual}
            self.specimens += SpecimenFactory.create_batch(specimens, **kwargs)

        for specimen in self.specimens:
            kwargs = {'specimen': specimen}
            self.aliquots += AliquotFactory.create_batch(aliquots, **kwargs)

        for aliquot in self.aliquots:
            projects_list = random.sample(projects, 3)
            kwargs = {'aliquot': aliquot, 'projects': projects_list}
            self.runs += RunFactory.create_batch(runs, **kwargs)

    def create_rows(self):
        """
        rows simulates the leukform

        Raises:
            ImproperlyConfigured("create rows first")
        tests: test_runs_factory_create_rows
        """

        if not self.individuals:
            raise ImproperlyConfigured("create batch first")

        for run in self.runs:

            # format projects in csv friendly style
            projects = '|'.join([str(e.pk) for e in run.projects.all()])

            # extract parent objects
            aliquot = run.aliquot
            specimen = aliquot.specimen
            individual = specimen.individual
            individual  # Just here to avoid unused error

            # initialize row
            row = {}

            # loop through leukform fields
            for col in LEUKFORM_CSV_FIELDS:
                model, field = col.split('.')
                if model == 'Run' and field == 'projects':
                    row[col] = projects
                else:
                    value = '{0}.{1}'.format(model.lower(), field)
                    row[col] = eval(value)

            # append row to rows
            self.rows.append(row)

        return self.rows

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
        keys = LEUKFORM_CSV_FIELDS

        with open(path, 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(self.rows)

        return path

    def create_stringio_from_rows(self):
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
        keys = LEUKFORM_CSV_FIELDS

        with open(path, 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(self.rows)

        return path
