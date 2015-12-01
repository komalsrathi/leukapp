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
from leukapp.apps.leukforms.utils import get_out_columns

# local
from .constants import CREATE_FIELDS, LEUKAPP_FACTORIES


class LeukformSamplesFactory(object):

    """
    A leukform samples factory. This factory is mainly used to test the
    LeukformLoader module.

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

    projects = [
        LEUKAPP_FACTORIES['Project'](title='test ' + str(i)) for i in range(3)]

    def __init__(self):
        super(LeukformSamplesFactory, self).__init__()
        self._set_variables()

    def _set_variables(self):
        # initialize rows
        self.rows = []
        self._row = {}

        # created instances
        self.instances = {
            'Individual': [],
            'Specimen': [],
            'Aliquot': [],
            'Extraction': [],
            }

        # requested instances
        self.request = {
            'Individual': 0,
            'Specimen': 0,
            'Aliquot': 0,
            'Extraction': 0,
            }

    def create_batch(self, individuals, specimens=0, aliquots=0, extractions=0,
            delete=True, slug=False):
        """
        Creates a batch of samples and returns them in a leukform format.

        Instances for the last model requested are always deleted.
        For instance, if you request individuals=10, specimens=2 and
        delete=False, the 10 individuals will not be deleted. However, the
        specimens will be.

        When using slug=True in LeukformSamplesFactory, only two sets of data
        are provided: the data of the object to be created and the slug of the
        parent object.

        Input:
            individuals (int): number of individuals
            specimens (int): number of specimens per individual
            aliquots (int): number of aliquots per specimen
            extractions (int): number of extractions per aliquot
            delete (boolean): if True, delete all created instances
            slug (boolean): if True, delete is depreciated, slugs are returned
        Returns:
            rows (list): a list of dictoaries ready to be submitted
        """
        if self.instances['Individual']:
            self._set_variables()

        if slug:  # if slug, instances won't be deleted, slugs will be returned
            self._delete = False
            self._slug = slug
        if not slug:  # if not slug, delete will not be depreciated
            self._delete = delete
            self._slug = slug

        self.request = {
            'Individual': int(individuals),
            'Specimen': int(specimens),
            'Aliquot': int(aliquots),
            'Extraction': int(extractions),
            }

        self._create_instances()

        if self._delete:
            try:  # this will recursively delete all child istances
                [i.delete() for i in self.instances['Individual']]
            except AssertionError:
                pass

        return self.rows

    def get_rows(self, shuffle=True):
        """ if shuffle, returns shuffled rows; else, returns rows """
        if not shuffle:
            random.shuffle(self.rows)
        return self.rows

    def _create_instances(self, model='Individual', parent=None):
        """
        Recursively generates instances by passing the child model name and
        the parent instance. This function calls self._update_parameters,
        which provides model specific kwargs and the name of the child model.

        Input:
            model (str): name of instance's model
            parent (Model Object): foreing key's object
        """
        for order in range(self.request[model]):
            kwargs, child = self._update_parameters(model, parent, order)
            instance = LEUKAPP_FACTORIES[model](**kwargs)
            self.instances[model].append(instance)
            self._write_row(instance, model)
            if child:
                self._create_instances(model=child, parent=instance)

    def _update_parameters(self, model, parent, order=None):
        """
        Provides the model specific' Factory kwargs. Also determines whether
        or not this instance is in the last level of creation by quering
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
            self._last = (self.request['Extraction'] == 0)
            return {'specimen': parent}, 'Extraction'
        if model == 'Extraction':
            self._last = True
            pl = '|'.join(str(p.pk) for p in random.sample(self.projects, 3))
            return {'aliquot': parent, 'projects_string': pl}, None

    def _write_row(self, instance, model):
        """
        Writes each instance's data to self._row and appends it to self.rows
        when self._last is True. Instances in the last level of creation will
        always be deleted. If self._slug=True and self._last=False, only the
        instance slug will be recorded.

        Input:
            model (str): name of instance's model
            parent (Leukapp Instance): foreing key's object
        """
        notused = [
            "individual", "specimen", "aliquot"]
        if self._slug and (not self._last):
            self._row = {}
            self._row[model + '.slug'] = instance.slug
        else:
            for field in CREATE_FIELDS[model]:
                if field in notused:
                    continue
                column = "{0}.{1}".format(model, field)
                value = eval('instance.{0}'.format(field))
                self._row[column] = str(value)
        if self._last:
            instance.delete()
            self.rows.append(self._row.copy())

    def create_csv_from_rows(self):
        """
        Creates a csv from rows.
        Returns: Path of csv
        Raises: ImproperlyConfigured("create batch first")
        """
        if not self.rows:
            raise ImproperlyConfigured("create rows first")

        timestamp = datetime.datetime.now().isoformat().split('.')[0]
        file_name = 'test_leukform_' + timestamp + '.csv'
        path = os.path.join(settings.MEDIA_ROOT, 'csv', 'outrows', file_name)
        keys = get_out_columns(columns=list(self.rows[0]))

        with open(path, 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(self.rows)

        return path

    def create_stringio_from_rows(self):
        """
        Creates a StringIO from rows.
        Returns: StringIO
        Raises:ImproperlyConfigured("create batch first")
        NOTTESTED
        """
        if not self.rows:
            raise ImproperlyConfigured("create rows first")

        keys = get_out_columns(columns=list(self.rows[0]))
        out = io.StringIO()
        dict_writer = csv.DictWriter(out, keys)
        dict_writer.writeheader()
        dict_writer.writerows(self.out)
        out.seek(0)

        return out


# ROUTINE PROTECTION
# =============================================================================

if __name__ == '__main__':
    pass
