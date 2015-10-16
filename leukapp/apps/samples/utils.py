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
from leukapp.apps.individuals.models import Individual
from leukapp.apps.specimens.models import Specimen
from leukapp.apps.aliquots.models import Aliquot
from leukapp.apps.projects.models import Project
from leukapp.apps.individuals.factories import IndividualFactory
from leukapp.apps.specimens.factories import SpecimenFactory
from leukapp.apps.aliquots.factories import AliquotFactory
from leukapp.apps.samples.factories import SampleFactory
from leukapp.apps.projects.factories import ProjectFactory

# local
from .models import Sample
from .forms import IndividualForm, SpecimenForm, AliquotForm, SampleForm
from .constants import LEUKFORM_FIELDS, LEUKFORM_OUT_FIELDS


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
        projects = [ProjectFactory() for i in range(10)]

        self.individuals += IndividualFactory.create_batch(i)

        for individual in self.individuals:
            kwargs = {'individual': individual}
            self.specimens += SpecimenFactory.create_batch(s, **kwargs)

        for specimen in self.specimens:
            kwargs = {'specimen': specimen}
            self.aliquots += AliquotFactory.create_batch(a, **kwargs)

        for aliquot in self.aliquots:
            kwargs = {
                'aliquot': aliquot,
                'projects': random.sample(projects, 3)
                }
            self.samples += SampleFactory.create_batch(sa, **kwargs)

        self.instances = {
            'Individual': self.individuals,
            'Specimen': self.specimens,
            'Aliquot': self.aliquots,
            'Sample': self.samples,
            }

    def create_rows(self):
        """
        rows simulates the leukform

        Raises:
            ImproperlyConfigured("create rows first")
        tests: test_samples_factory_create_rows
        """

        if not self.individuals:
            raise ImproperlyConfigured("create batch first")

        for sample in self.samples:

            # format projects in csv friendly style
            projects = '|'.join([str(e.pk) for e in sample.projects.all()])

            # extract parent objects
            aliquot = sample.aliquot
            specimen = aliquot.specimen
            individual = specimen.individual

            # initialize row
            row = {}

            # loop through leukform fields
            for col in LEUKFORM_FIELDS:
                model, field = col.split('.')
                if model == 'Sample' and field == 'projects':
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
        keys = LEUKFORM_FIELDS

        with open(path, 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(self.rows)

        return path


class SamplesCSV(object):

    """
    """

    help = 'Gets create form fields for Individuals, Specimens and Aliquots'

    models = {
        'Individual': Individual,
        'Specimen': Specimen,
        'Aliquot': Aliquot,
        'Sample': Sample,
        'Project': Project,
        }

    models_forms = {
        'Individual': IndividualForm,
        'Specimen': SpecimenForm,
        'Aliquot': AliquotForm,
        'Sample': SampleForm
        }

    # constant messages
    ACTION_EXISTING = 'EXISTED'
    ACTION_ADDED = 'ADDED'
    ACTION_ERROR = 'ERROR'
    ACTION_NO_ERRORS = 'NO ERRORS'
    ACTION_NOT_TESTED = 'NOT TESTED'

    def __init__(self):
        super(SamplesFromCsv, self).__init__()

        # models
        self.model = ''
        self.models_fields = {}

        # results data
        self.existing = {}
        self.added = {}
        self.rejected = {}
        self.out_rows = []
        self.out_row = {}

        # initialize
        for model in self.models:
            self.models_fields[model] = {}

            if model != 'Project':
                self.added[model] = []
                self.existing[model] = []
                self.rejected[model] = []

    def save_samples_from_rows(self, rows):
        """
        Adds samples from csv

        tests:
            test_save_samples_from_rows
            test_added_existing_individuals
            test_added_existing_specimens
            test_added_existing_aliquots
        """

        # Generate a dict per row, with the first CSV row being the keys.
        for row in rows:
            if not self.process_row(row):
                continue

        for model in self.models:
            if model != 'Project':
                self.added[model] = set(self.added[model])
                self.existing[model] = set(self.existing[model])
                self.rejected[model] = set(self.rejected[model])

    def initialize_out_row(self):
        """
        initializes the results row for the current leukform row

        test: test_initialize_out_row
        """
        for model in self.models:
            if model == 'Project':
                self.out_row[model + '.pk'] = self.ACTION_NOT_TESTED
            else:
                self.out_row[model + '.ext_id'] = self.ACTION_NOT_TESTED
            self.out_row[model + '.action'] = self.ACTION_NOT_TESTED
            self.out_row[model + '.errors'] = self.ACTION_NOT_TESTED

    def get_fields_from_row(self, row):
        """
        Gets fields from rows.

        Input Args:
            row (dict): dict with keys as column names
        Returns:
            models_fields: nested dictionary, first lever are models
                second level are leuk_form fields
        tests:
            test_get_fields_from_row
        """
        if not row:
            return self.models_fields

        keys = list(row)
        for k in keys:
            model, field = k.split('.')
            self.models_fields[model][field] = row[k]

        return self.models_fields

    def process_row(self, row):
        """
        Process row's fields.

        Input Args:
            row (dict): dict with keys as column names
        tests:
            test_process_row_empty_row_dict
            test_process_row_invalid_individual
            test_process_row_invalid_specimen
        """
        # initialize outrow
        self.initialize_out_row()

        # get fields from row
        self.get_fields_from_row(row)

        # find or create individual
        if not self.get_or_create_instance(model='Individual'):
            self.out_rows.append(self.out_row)
            return False

        # find or create specimen
        if not self.get_or_create_instance(model='Specimen'):
            self.out_rows.append(self.out_row)
            return False

        # find or create aliquot
        if not self.get_or_create_instance(model='Aliquot'):
            self.out_rows.append(self.out_row)
            return False

        # find or create Sample
        self.get_or_create_instance(model='Sample')
        self.out_rows.append(self.out_row)
        return True

    def get_or_create_instance(self, model):
        """
        Gets or creates instance while collecting results data.

        Input Args:
            model (string): name of instance's model
        Returns:
            models_fields: created instance. If form isn't valid, returns None
        tests:
            test_get_or_create_instance_existent_instance
            test_get_or_create_instance_nonexistent_instance
        """
        fields = self.models_fields[model]
        form = self.models_forms[model](fields)
        try:
            instance = self.get_instance(model, fields)
        except self.models[model].DoesNotExist:
            instance, errors = self.create_instance(model, fields, form)

        return instance

    def get_instance(self, model, fields=None):
        """
        Gets instance.

        Input Args:
            model (string): name of instance's model
            fields (dict): dictionary with get fields
        tests:
            test_get_instance_using_existent_instance
            test_get_instance_using_nonexistent_instance
        """
        if not fields:
            fields = self.models_fields[model]

        instance = self.models[model].objects.get(**fields)

        # collect results data
        self.out_row[model + '.ext_id'] = fields['ext_id']
        self.out_row[model + '.action'] = self.ACTION_EXISTING
        self.out_row[model + '.errors'] = self.ACTION_NO_ERRORS

        if instance not in self.added[model]:
            self.existing[model].append(instance)

        # update Specimen and Aliquot fields foreing keys
        self.update_models_fields(model, instance)
        return instance

    def create_instance(self, model, fields=None, form=None):
        """
        Creates instance.

        Input Args:
            model (string): name of instance's model
            fields (dict): dictionary with create fields
            form (form): instance create form
        tests:
            test_create_instance_form_valid
            test_create_instance_form_invalid
        """
        if not fields and not self.models_fields[model]:
            return None, None
        elif not fields and self.models_fields[model]:
            fields = self.models_fields[model]

        if not form:
            form = self.models_forms[model](fields)

        if form.is_valid():
            instance = form.save()
            errors = None

            # write out_row instance columns
            self.out_row[model + '.ext_id'] = fields['ext_id']
            self.out_row[model + '.action'] = self.ACTION_ADDED
            self.out_row[model + '.errors'] = self.ACTION_NO_ERRORS

            # keep count of created instances
            self.added[model].append(instance)

            # update Specimen and Aliquot fields foreing keys
            self.update_models_fields(model, instance)
            return instance, errors
        else:
            instance = None
            errors = form.errors.as_json()

            # write out_row instance columns
            self.out_row[model + '.ext_id'] = fields['ext_id']
            self.out_row[model + '.action'] = self.ACTION_ERROR
            self.out_row[model + '.errors'] = str(errors)

            # keep count of rejected instances
            self.rejected[model].append(instance)
            return instance, errors

    def update_models_fields(self, model, instance):
        """
        Updates Specimen and Aliqots fields after Individual and Specimen
        instances are gotten or created.

        Input Args:
            model (string): name of instance's model
        tests:
            test_update_models_fields_for_specimen
            test_update_models_fields_for_aliquot
        """
        if model == 'Individual' and instance:
            self.models_fields['Specimen']['individual'] = instance.pk

        if model == 'Specimen' and instance:
            self.models_fields['Aliquot']['specimen'] = instance.pk

        if model == 'Aliquot' and instance:
            self.models_fields['Sample']['Aliquot'] = instance.pk

    def save_out_rows_in_csv(self):
        """
        Creates a csv from out_rows.

        Returns:
            Path of csv
        Raises:
            ImproperlyConfigured("create out_rows first")
        tests: test_csv_from_rows
        """
        if not self.out_rows:
            raise ImproperlyConfigured("create rows first")

        timestamp = datetime.datetime.now().isoformat()
        file_name = 'out_leukform_' + timestamp + '.csv'
        path = os.path.join(settings.MEDIA_ROOT, 'csv', 'outrows', file_name)
        keys = LEUKFORM_OUT_FIELDS

        with open(path, 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(self.out_rows)

        return path
