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
from .constants import LEUKFORM_CSV_FIELDS


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
        _create_csv_from_rows: creates csv from rows
        _create_stringio_from_rows: creates StringIO from rows
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
        self.projects = [ProjectFactory(name=str(i)) for i in range(10)]
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

        self.delete = delete
        self.last = False
        self.i = individuals
        self.s = specimens
        self.a = aliquots
        self.r = runs

        self.rows = []
        self._create_individuals()
        if delete:
            [i.delete() for i in self.individuals]
        return self.rows

    def get_rows(self, ordered=True):
        """ return rows """
        if not ordered:
            random.shuffle(self.rows)
        return self.rows

    def _create_individuals(self):
        """ NOTTESTED NOTDOCUMENTED """
        for NOTUSED in range(self.i):
            self.row = {}
            i, self.last = IndividualFactory(), (self.s == 0)
            self._write_row(i, 'Individual')
            self.individuals.append(i)
            self._create_specimens(i)

    def _create_specimens(self, i):
        """ NOTTESTED NOTDOCUMENTED """
        for order in range(self.s):
            s = SpecimenFactory(individual=i, order=order)
            self.last = (self.a == 0)
            self._write_row(s, 'Specimen')
            self.specimens.append(s)
            self._create_aliquots(s)

    def _create_aliquots(self, s):
        """ NOTTESTED NOTDOCUMENTED """
        for NOTUSED in range(self.a):
            a, self.last = AliquotFactory(specimen=s), (self.r == 0)
            self._write_row(a, 'Aliquot')
            self.aliquots.append(a)
            self._create_runs(a)

    def _create_runs(self, a):
        """ NOTTESTED NOTDOCUMENTED """
        for NOTUSED in range(self.r):
            ps = random.sample(self.projects, 3)
            pl = '|'.join(str(p.pk) for p in ps)
            r = RunFactory(aliquot=a, projects=ps)
            r.projects_list = pl
            self.last = True
            self._write_row(r, 'Run')
            self.runs.append(r)

    def _write_row(self, instance, model):
        """ NOTTESTED NOTDOCUMENTED """
        if (not self.delete) and (not self.last):
            self.row = {}
            self.row[model + '.slug'] = instance.slug
        else:
            for field in self.leukform_fields[model]:
                column = "%s.%s" % (model, field)
                value = 'instance.%s' % field
                self.row[column] = eval(value)
        if self.last:
            instance.delete()
            self.rows.append(self.row)
        return self.row

    def _create_csv_from_rows(self):
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
        keys = set(self.rows[0])

        with open(path, 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(self.rows)

        return path

    def _create_stringio_from_rows(self):
        """
        Creates a string from rows.
        Returns: stringio
        Raises:ImproperlyConfigured("create rows first")
        """
        if not self.rows:
            raise ImproperlyConfigured("create rows first")

        keys = set(self.rows[0])
        out = io.StringIO()
        dict_writer = csv.DictWriter(out, keys)
        dict_writer.writeheader()
        dict_writer.writerows(self.out)
        out.seek(0)

        return out
