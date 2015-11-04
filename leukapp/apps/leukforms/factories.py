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

# local
from .constants import LEUKFORM_FIELDS, LEUKAPP_FACTORIES


class LeukformSamplesFactory(object):

    """
    Class used as a leukform samples factory.

    Attributes:
        instances (dict): keys are models, values are created instances
        request (dict): keys are models, values are requested instances
        delete (boolean): whether or not instances are deleted at the end
        rows (list): each element is a valid leukform dictionary
    Methods:
        create_batch: creates a batch of samples and returns rows
        get_rows: returns the rows shuffled
        create_csv_from_rows: creates csv from rows
        create_stringio_from_rows: creates StringIO from rows
    """

    def __init__(self):
        super(LeukformSamplesFactory, self).__init__()

        # delete created instances
        self.delete = True

        # initialize rows
        self.rows = []
        self._row = {}

        # created instances
        self.instances = {
            'Individual': [],
            'Specimen': [],
            'Aliquot': [],
            'Run': [],
            }

        # requested instances
        self.request = {
            'Individual': 0,
            'Specimen': 0,
            'Aliquot': 0,
            'Run': 0,
            }

        # projects used
        ProjectFactory = LEUKAPP_FACTORIES['Project']
        self.projects = [ProjectFactory(name=str(i)) for i in range(10)]

    def create_batch(self, individuals, specimens=0, aliquots=0, runs=0,
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
        if self.instances['Individual']:
            self.__init__()

        self.delete = delete
        self.request = {
            'Individual': individuals,
            'Specimen': specimens,
            'Aliquot': aliquots,
            'Run': runs,
            }

        self.i = individuals
        self.s = specimens
        self.a = aliquots
        self.r = runs

        self._create_instances(model='Individual')

        if self.delete:
            [i.delete() for i in self.instances['Individual']]

        return self.rows

    def get_rows(self, ordered=True):
        """ if ordered, returns shuffled rows; else, returns rows """
        if not ordered:
            random.shuffle(self.rows)
        return self.rows

    def _create_instances(self, model, parent=None):
        """
        Recursively generates instance passing its model and parent.
        This function calls self._set_parameters, which provides
        model specific kwargs and the name of the child model

        Input:
            model (str): name of instance's model
            parent (Leukapp Instance): foreing key's object
        """
        for order in range(self.request[model]):
            kwargs, child = self._set_parameters(model, parent, order)
            instance = LEUKAPP_FACTORIES[model](**kwargs)
            self.instances[model].append(instance)
            self._write_row(instance, model)
            if child:
                self._create_instances(model=child, parent=instance)

    def _set_parameters(self, model, parent, order=None):
        """
        Provides the model specific Factory kwargs. Also determines whether
        or not this istance is in the last level of creation by quering
        the number of requested instances for the child model.

        Input:
            model (str): name of instance's model
            parent (Leukapp Instance): foreing key's object
            order (int): number of instances created so far for the given model
        Return:
            (kwargs (dict), child (str)): kawrgs is the model specific creation
                parameters, while child is the name of the child model
        """
        if model == 'Individual':
            self._last = (self.request['Specimen'] == 0)
            return {}, 'Specimen'
        if model == 'Specimen':
            self._last = (self.request['Aliquot'] == 0)
            return {'individual': parent, 'order': str(order)}, 'Aliquot'
        if model == 'Aliquot':
            self._last = (self.request['Run'] == 0)
            return {'specimen': parent}, 'Run'
        if model == 'Run':
            self._last = True
            pl = '|'.join(str(p.pk) for p in random.sample(self.projects, 3))
            return {'aliquot': parent, 'projects_list': pl}, None

    def _write_row(self, instance, model):
        """
        Writes each instance data to self._row and appends it to self.rows
        when self._last is True. Instances in the last level of creation will
        always be deleted. If self.delete and self._last are False only the
        instance slug will be recorded.

        Input:
            model (str): name of instance's model
            parent (Leukapp Instance): foreing key's object
        """
        if (not self.delete) and (not self._last):
            self._row = {}
            self._row[model + '.slug'] = instance.slug
        else:
            for field in LEUKFORM_FIELDS[model]:
                column = "{0}.{1}".format(model, field)
                value = eval('instance.{0}'.format(field))
                self._row[column] = value
        if self._last:
            instance.delete()
            self.rows.append(self._row.copy())

    def create_csv_from_rows(self):
        """
        Creates a csv from rows.
        Returns: Path of csv
        Raises: ImproperlyConfigured("create rows first")
        """
        if not self.rows:
            raise ImproperlyConfigured("create rows first")

        timestamp = datetime.datetime.now().isoformat().split('.')[0]
        file_name = 'test_leukform_' + timestamp + '.csv'
        path = os.path.join(settings.MEDIA_ROOT, 'csv', 'outrows', file_name)
        keys = set(self.rows[0])

        with open(path, 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(self.rows)

        return path

    def create_stringio_from_rows(self):
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
