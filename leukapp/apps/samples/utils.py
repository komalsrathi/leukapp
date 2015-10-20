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
from leukapp.apps.individuals.factories import IndividualFactory
from leukapp.apps.specimens.factories import SpecimenFactory
from leukapp.apps.aliquots.factories import AliquotFactory
from leukapp.apps.samples.factories import SampleFactory
from leukapp.apps.projects.factories import ProjectFactory

# local
from .models import Sample
from .forms import IndividualForm, SpecimenForm, AliquotForm, SampleForm
from .constants import LEUKFORM_FIELDS, LEUKFORM_OUT_FIELDS


def rows_to_csv(rows, keys, path):
    with open(path, 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(rows)


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

    def create_batch(self, individuals, specimens, aliquots, samples):
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

        self.individuals += IndividualFactory.create_batch(individuals)

        for individual in self.individuals:
            kwargs = {'individual': individual}
            self.specimens += SpecimenFactory.create_batch(specimens, **kwargs)

        for specimen in self.specimens:
            kwargs = {'specimen': specimen}
            self.aliquots += AliquotFactory.create_batch(aliquots, **kwargs)

        for aliquot in self.aliquots:
            kwargs = {
                'aliquot': aliquot,
                'projects': random.sample(projects, 3)
                }
            self.samples += SampleFactory.create_batch(samples, **kwargs)

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
            individual

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

    def __init__(self):
        super(SamplesCSV, self).__init__()

        # models
        self.models = {
            'Individual': Individual,
            'Specimen': Specimen,
            'Aliquot': Aliquot,
            'Sample': Sample,
            }

        # forms
        self.forms = {
            'Individual': IndividualForm,
            'Specimen': SpecimenForm,
            'Aliquot': AliquotForm,
            'Sample': SampleForm
            }

        # row input
        self.input = {}

        # results data
        self.existing = {}
        self.added = {}
        self.rejected = []
        self.accepted = []

        # initialize
        for model in self.models:
            self.input[model] = {}
            self.added[model] = []
            self.existing[model] = []

    def save_samples_from_rows(self, rows):
        """
        Adds samples from csv

        tests:
            test_save_samples_from_rows
            test_added_existing_individuals
            test_added_existing_specimens
            test_added_existing_aliquots
        """
        models = ['Individual', 'Specimen', 'Aliquot', 'Sample']

        for row in rows:
            self.fields_from_row(row)

            for model in models:
                instance, errors = self.get_or_create(model=model)
                if errors:
                    row['ERRORS'] = errors
                    self.rejected.append(row)
                    break

            if 'ERRORS' not in row:
                self.accepted.append(row)

        for model in self.models:
            self.added[model] = set(self.added[model])
            self.existing[model] = set(self.existing[model])

    def fields_from_row(self, row):
        """
        Gets fields from rows.

        Input Args:
            row (dict): dict with keys as column names
        Returns:
            input: nested dictionary, first lever are models
                second level are leuk_form fields
        tests:
            test_fields_from_row
        """
        if not row:
            return self.input

        keys = list(row)
        for k in keys:
            model, field = k.split('.')

            if field == 'projects' and model == 'Sample':
                try:
                    projects = [int(e) for e in row[k].split("|")]
                    self.input[model][field] = projects
                except Exception:
                    self.input[model][field] = row[k]
            else:
                self.input[model][field] = row[k]

        return self.input

    def get_or_create(self, model):
        """
        Gets or creates instance while collecting results data.

        Input Args:
            model (string): name of instance's model
        Returns:
            input: created instance. If form isn't valid, returns None
        tests:
            test_get_or_create_using_existent_instance
            test_get_or_create_nonexistent_instance
        """
        errors, instance = None, None
        form = self.forms[model](self.input[model])
        search = self.input[model].copy()

        try:
            if not self.input[model]:
                raise self.models[model].DoesNotExist

            search.pop('projects', None)
            instance = self.models[model].objects.get(**search)

            if instance not in self.added[model]:
                self.existing[model].append(instance)

        except self.models[model].DoesNotExist:
            if form.is_valid():
                instance = form.save()
                self.added[model].append(instance)
            else:
                errors = form.errors.as_json()

        # update foreing key for next model
        self.update_input(model, instance)
        return instance, errors

    def update_input(self, model, instance):
        """
        Updates child instances after parent are found or created.

        Input Args:
            model (string): model name of parent instance
            instance (django Model): parent instance
        tests:
            test_update_input_for_specimen
            test_update_input_for_aliquot
        """
        if model == 'Individual' and instance:
            self.input['Specimen']['individual'] = instance.pk

        if model == 'Specimen' and instance:
            self.input['Aliquot']['specimen'] = instance.pk

        if model == 'Aliquot' and instance:
            self.input['Sample']['aliquot'] = instance.pk

"""
        timestamp = datetime.datetime.now().isoformat().split('.')[0]
        file_name = 'out_leukform_' + timestamp + '.csv'
        path = os.path.join(settings.MEDIA_ROOT, 'csv', 'outrows', file_name)
        keys = LEUKFORM_OUT_FIELDS
"""
