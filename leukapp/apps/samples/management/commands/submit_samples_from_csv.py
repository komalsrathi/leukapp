# python
import csv
import json

# django
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

# leukapp
from leukapp.apps.individuals.models import Individual
from leukapp.apps.specimens.models import Specimen
from leukapp.apps.aliquots.models import Aliquot
from leukapp.apps.projects.models import Project

# local
from leukapp.apps.samples import forms


class Command(BaseCommand):
    help = 'Gets create form fields for Individuals, Specimens and Aliquots'

    # models
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
    models_fields = {}

    models_names = [m.__name__ for m in models]
    sample_models = ['Individual', 'Specimen', 'Aliquot']

    # results data
    existing = {}
    added = {}
    rejected = {}
    out_rows = []
    out_row = {}

    # initialize
    for m in sample_models:
        added[m] = []
        existing[m] = []
        models_fields[m] = {}

    # constant messages
    ACTION_EXISTING = 'EXISTED'
    ACTION_ADDED = 'ADDED'
    ACTION_ERROR = 'ERROR'
    ACTION_NO_ERRORS = 'NO ERRORS'
    ACTION_NOT_TESTED = 'NOT TESTED'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)
    # raise CommandError('Poll "%s" does not exist' % poll_id)

    def handle(self, *args, **options):
        filename = settings.MEDIA_ROOT + options['filename']

        with open(filename, 'r') as rows:
            out = self.save_samples_from_csv(rows)

        self.stdout.write("individuals_added: %s" % out['individuals_added'])
        self.stdout.write("specimens_added: %s" % out['specimens_added'])
        self.stdout.write("aliquots_added: %s" % out['aliquots_added'])

        for e in out['errors']:
            self.stdout.write("errors: %s" % e)

    def initialize_out_row(self):
        """
        initializes the results row for the current leukgen_form row

        test: test_initialize_out_row
        """
        for model in self.models_names:
            self.out_row[model + '.id'] = self.ACTION_NOT_TESTED
            self.out_row[model + '.action'] = self.ACTION_NOT_TESTED
            self.out_row[model + '.errors'] = self.ACTION_NOT_TESTED

    def get_fields_from_row(self, row):
        keys = list(row)
        for k in keys:
            model, field = k.split('.')
            self.models_fields[model][field] = row[k]

    def get_or_create_instance(self, model):

        fields = self.models_fields[model]
        form = self.models_forms[model](fields)

        try:
            instance = self.models[model].object.get(**fields)

            # write out_row individual columns
            self.out_row[model + '.ext_id'] = fields['ext_id']
            self.out_row[model + '.action'] = self.ACTION_EXISTING
            self.out_row[model + '.errors'] = self.ACTION_NO_ERRORS

            # keep count
            self.existing[model].append[instance]

        except self.models[model].DoesNotExist:

            if form.is_valid():
                instance = form.save()
                self.added[model].append[instance]

                # write out_row instance columns
                self.out_row[model + '.ext_id'] = fields['ext_id']
                self.out_row[model + '.action'] = self.ACTION_EXISTING
                self.out_row[model + '.errors'] = self.ACTION_NO_ERRORS

            else:
                instance = None
                errors_as_json = form.errors.as_json()
                errors = json.dump(errors_as_json)
                self.rejected[model].append[instance]

                # write out_row instance columns
                self.out_row[model + '.ext_id'] = fields['ext_id']
                self.out_row[model + '.action'] = self.ACTION_ERROR
                self.out_row[model + '.errors'] = errors

        return instance

    def save_samples_from_csv(self, rows):
        """ adds samples from csv """

        # Generate a dict per row, with the first CSV row being the keys.
        for row in csv.DictReader(rows, delimiter=","):

            self.get_fields_from_row(row)  # get fields from row
            self.initialize_out_row()  # initialize outrow

            # find or create individual
            individual = self.get_or_create_instance(model='Individual')

            if not individual:
                self.out_rows.append(self.out_row)
                break

            # find or create specimen
            self.models_fields['Specimen']['individual'] = individual.pk
            specimen = self.get_or_create_instance(model='Specimen')

            if not specimen:
                self.out_rows.append(self.out_row)
                break

            # find or create Aliquot
            self.models_fields['Specimen']['specimen'] = specimen.pk
            aliquot, mock = self.get_or_create_instance(model='Aliquot')
