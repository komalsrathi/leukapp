# -*- coding: utf-8 -*-

# python
import csv
import os
import datetime

# django
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

# leukapp
from leukapp.apps.individuals.models import Individual
from leukapp.apps.specimens.models import Specimen
from leukapp.apps.aliquots.models import Aliquot
from leukapp.apps.projects.models import Project

# local
from leukapp.apps.samples import forms
from leukapp.apps.samples.constants import LEUKFORM_OUT_FIELDS


class Command(BaseCommand):

    """
    Gets create form fields for Individuals, Specimens and Aliquots
    """

    help = 'Gets create form fields for Individuals, Specimens and Aliquots'

    models = {
        'Individual': Individual,
        'Specimen': Specimen,
        'Aliquot': Aliquot,
        'Project': Project,
        }

    models_forms = {
        'Individual': forms.IndividualForm,
        'Specimen': forms.SpecimenForm,
        'Aliquot': forms.AliquotForm,
        }

    # constant messages
    ACTION_EXISTING = 'EXISTED'
    ACTION_ADDED = 'ADDED'
    ACTION_ERROR = 'ERROR'
    ACTION_NO_ERRORS = 'NO ERRORS'
    ACTION_NOT_TESTED = 'NOT TESTED'

    def __init__(self):
        super(Command, self).__init__()
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

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)
    # raise CommandError('Poll "%s" does not exist' % poll_id)

    def handle(self, *args, **options):
        filename = settings.MEDIA_ROOT + options['filename']

        with open(filename, 'r') as leukform:
            rows = csv.DictReader(leukform, delimiter=",")
            self.save_samples_from_rows(rows)

        for model in self.models:
            if model != 'Project':
                a = len(self.added[model])
                e = len(self.existing[model])
                r = len(self.rejected[model])

                self.stdout.write(model + " added: %s" % a)
                self.stdout.write(model + " existing: %s" % e)
                self.stdout.write(model + " rejected: %s" % r)

        self.stdout.write("results file: %s" % self.save_out_rows_in_csv())

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
        self.get_or_create_instance(model='Aliquot')
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
