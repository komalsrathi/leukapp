# -*- coding: utf-8 -*-

# python
import random
import os
import datetime
import csv
import io

# django
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings

# leukapp
from leukapp.apps.projects.factories import ProjectFactory
from leukapp.apps.individuals.factories import IndividualFactory
from leukapp.apps.specimens.factories import SpecimenFactory
from leukapp.apps.aliquots.factories import AliquotFactory
from leukapp.apps.runs.factories import RunFactory
from leukapp.apps.individuals.constants import INDIVIDUAL_LEUKFORM_FIELDS
from leukapp.apps.specimens.constants import SPECIMEN_LEUKFORM_FIELDS
from leukapp.apps.aliquots.constants import ALIQUOT_LEUKFORM_FIELDS
from leukapp.apps.runs.constants import RUN_LEUKFORM_FIELDS

# local
from .constants import LEUKFORM_CSV_FIELDS, MODELS


class LeukformCsvFactory(object):

    """
    Class used as a runs factory.

    Attributes:
        individuals (list): list of all individuals created
        specimens (list): list of all specimens created
        aliquots (list): list of all aliquots created
        rows (list of dictionaries): simulates the leukform
    Methods:
        create_batch: creates a batch of runs
        get_rows: creates `rows` simulating leukform based on batch
        create_csv_from_rows: creates csv from rows
        create_stringio_from_rows: creates StringIO from rows
    """

    leukform_fields = {
        'Individual': INDIVIDUAL_LEUKFORM_FIELDS,
        'Specimen': SPECIMEN_LEUKFORM_FIELDS,
        'Aliquot': ALIQUOT_LEUKFORM_FIELDS,
        'Run': RUN_LEUKFORM_FIELDS,
        }

    def __init__(self):
        super(LeukformCsvFactory, self).__init__()
        self.individuals = []
        self.specimens = []
        self.aliquots = []
        self.runs = []
        self.rows = []
        self.row = {}
        self.instances = {
            'Individual': self.individuals,
            'Specimen': self.specimens,
            'Aliquot': self.aliquots,
            'Run': self.runs,
            }

    def create_batch(self, individuals=2, specimens=3, aliquots=2, runs=2,
            delete=True):
        """
        Creates a batch of runs.

        Input:
            individuals (int): number of individuals
            specimens (int): number of specimens per individual
            aliquots (int): number of aliquots per specimen
            runs (int): number of runs per aliquot
        Raises:
            ImproperlyConfigured if batch has already been created
        """
        if self.individuals:
            msg = "Batch has already been created, run .__init__() to reset"
            raise ImproperlyConfigured(msg)

        self.rows = []
        self.delete = delete
        projects = [ProjectFactory(name=str(i)) for i in range(10)]

        for i in range(individuals):
            self.row = {}
            i = IndividualFactory()
            last = (specimens == 0)
            self._write_row(i, 'Individual', last)
            self.individuals.append(i)
            for o in range(specimens):
                s = SpecimenFactory(individual=i, order=o)
                last = (aliquots == 0)
                self._write_row(s, 'Specimen', last)
                self.specimens.append(s)
                for NOTUSED in range(aliquots):
                    a = AliquotFactory(specimen=s)
                    last = (runs == 0)
                    self._write_row(a, 'Aliquot', last)
                    self.aliquots.append(a)
                    for NOTUSED in range(runs):
                        p = random.sample(projects, 3)
                        r = RunFactory(aliquot=a, projects=p)
                        self._write_row(r, 'Run', True)
                        self.runs.append(r)
            if delete:
                i.delete()

        return self.rows

    def _write_row(self, instance, model, last=False):
        """ NOTTESTED """
        if not self.delete and not last:
            self.row[model + '.leukid'] = instance.slug
        else:
            for field in self.leukform_fields[model]:
                column = "%s.%s" % (model, field)
                if model == 'Run' and field == 'projects':
                    p = '|'.join([str(e.pk) for e in instance.projects.all()])
                    self.row[column] = p
                    continue
                value = 'instance.%s' % field
                self.row[column] = eval(value)
        if last:
            self.rows.append(self.row)
        return self.row

    def get_rows(self, ordered=True):
        """ return rows """
        if not ordered:
            random.shuffle(self.rows)
        return self.rows

    def create_csv_from_rows(self):
        """
        Creates a csv from rows.
        Returns: Path of csv
        Raises: ImproperlyConfigured("create rows first")
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
        Returns:Path of csv
        Raises:ImproperlyConfigured("create rows first")
        """
        if not self.rows:
            raise ImproperlyConfigured("create rows first")

        keys = LEUKFORM_CSV_FIELDS
        out = io.StringIO()
        dict_writer = csv.DictWriter(out, keys)
        dict_writer.writeheader()
        dict_writer.writerows(self.out)
        out.seek(0)

        return out
