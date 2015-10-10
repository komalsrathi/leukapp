# python
import csv
import json

# django
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django import forms
from django.db.models import Q

# leukapp apps
from leukapp.apps.individuals.constants import INDIVIDUAL_CREATE_FIELDS
from leukapp.apps.specimens.constants import SPECIMEN_CREATE_FIELDS
from leukapp.apps.aliquots.constants import ALIQUOT_CREATE_FIELDS

from leukapp.apps.individuals.models import Individual
from leukapp.apps.specimens.models import Specimen
from leukapp.apps.aliquots.models import Aliquot

from leukapp.apps.samples.models import PseudoIndividual
from leukapp.apps.samples.models import PseudoSpecimen
from leukapp.apps.samples.models import PseudoAliquot


class PseudoIndividualForm(forms.ModelForm):

    class Meta:
        model = PseudoIndividual
        fields = INDIVIDUAL_CREATE_FIELDS


class PseudoSpecimenForm(forms.ModelForm):

    class Meta:
        model = PseudoSpecimen
        fields = SPECIMEN_CREATE_FIELDS


class PseudoAliquotForm(forms.ModelForm):

    class Meta:
        model = PseudoAliquot
        fields = ALIQUOT_CREATE_FIELDS


def initialize_out_row(fields):
    out_row = {}

    for model_name in ['Individual', 'Specimen', 'Aliquot']:
        out_row[model_name + '.ext_id'] = fields[model_name]['ext_id']
        out_row[model_name + '.action'] = 'NOT TESTED'
        out_row[model_name + '.errors'] = 'NOT TESTED'

    return out_row


def get_models_fields(row):

    fields = {}
    keys = list(row)

    fields['Individual'] = {}
    fields['Specimen'] = {}
    fields['Aliquot'] = {}
    fields['Project'] = {}

    for k in keys:
        schema, field = k.split('.')
        if schema == 'Individual':
            fields['Individual'][field] = row[k]
        elif schema == 'Specimen':
            fields['Specimen'][field] = row[k]
        elif schema == 'Aliquot':
            fields['Aliquot'][field] = row[k]
        elif schema == 'Project':
            fields['Project'][field] = row[k]

    return fields


def find_individual(fields):
    try:
        individual = Individual.objects.get(
            Q(ext_id__exact=fields['ext_id']),
            Q(institution__exact=fields['institution']),
            Q(species__exact=fields['species']),
            )
    except Individual.DoesNotExist:
        individual = ''
    return individual


def find_specimen(fields, individual):
    try:
        specimen = Specimen.objects.get(
            Q(individual=individual.pk),
            Q(ext_id__exact=fields['ext_id']),
            Q(source__exact=fields['source']),
            )
    except Specimen.DoesNotExist:
        specimen = ''
    return specimen


def find_aliquot(fields, specimen):
    try:
        bm = fields['biological_material']
        aliquot = Aliquot.objects.get(
            Q(specimen=specimen.pk),
            Q(biological_material__exact=bm),
            Q(ext_id__exact=fields['ext_id']),
            )
    except Aliquot.DoesNotExist:
        aliquot = ''
    return aliquot


def find_or_create_pseudo_model(model_name, mock, **kwargs):

    fields = mock['fields']['model_name']

    if model_name == 'Individual':
        instance = find_individual(fields)
        form = PseudoIndividualForm(fields)
    elif model_name == 'Specimen':
        instance = find_specimen(fields, kwargs['individual'])
        form = PseudoSpecimenForm(fields)
    elif model_name == 'Aliquot':
        instance = find_aliquot(fields, kwargs['specimen'])
        form = PseudoAliquotForm(fields)

    plural = model_name.lower() + 's'

    if instance:
        # write out_row individual columns
        mock['out_row'][model_name + '.ext_id'] = fields['ext_id']
        mock['out_row'][model_name + '.action'] = mock['ACTION_EXISTING']
        mock['out_row'][model_name + '.errors'] = ''

        # keep count
        mock['existing_' + plural] += 1

    else:
        if form.is_valid():
            instance = form.save()
            mock['added_' + plural] += 1

            # write out_row instance columns
            mock['out_row'][model_name + '.ext_id'] = fields['ext_id']
            mock['out_row'][model_name + '.action'] = mock['ACTION_ADDED']
            mock['out_row'][model_name + '.errors'] = ''

        else:
            errors_as_json = form.errors.as_json()
            errors = json.dump(errors_as_json)

            # write out_row instance columns
            mock['out_row'][model_name + '.ext_id'] = fields['ext_id']
            mock['out_row'][model_name + '.action'] = mock['ACTION_ERROR']
            mock['out_row'][model_name + '.errors'] = errors

    return instance, mock


def mock_samples_from_csv(filename):
    """ adds samples from csv """

    rows = open(filename)

    mock = {

        # mock output file
        'out_rows': [],

        # report data
        'existing_individuals': 0,
        'added_individuals': 0,
        'existing_specimens': 0,
        'added_specimens': 0,
        'existing_aliquots': 0,
        'added_aliquots': 0,
        'errors': [],

        # action messages for mock file
        'ACTION_EXISTING': 'EXISTED',
        'ACTION_ADDED': 'ADDED',
        'ACTION_ERROR': 'ERROR',
        'ACTION_NOT_TESTED': 'NOT TESTED',
    }

    # Generate a dict per row, with the first CSV row being the keys.
    for row in csv.DictReader(rows, delimiter=","):

        mock['fields'] = get_models_fields(row)
        mock['out_row'] = initialize_out_row(mock['fields'])

        # find or create individual
        individual, mock = find_or_create_pseudo_model(
            model_name='Individual', mock=mock)

        if not individual:
            mock["out_rows"].append(mock["out_row"])
            break
        else:
            kwargs = dict(individual=individual)
            specimen, mock = find_or_create_pseudo_model(
                model_name='Specimen', mock=mock, **kwargs)
        if not specimen:
            mock["out_rows"].append(mock["out_row"])
            break
        else:
            kwargs = dict(specimen=specimen)
            aliquot, mock = find_or_create_pseudo_model(
                model_name='Specimen', mock=mock, **kwargs)

    out = {
        'individuals_added': individuals_added,
        'specimens_added': specimens_added,
        'aliquots_added': aliquots_added,
        'errors': errors,
        }

    return out


class Command(BaseCommand):
    help = 'Gets create form fields for Individuals, Specimens and Aliquots'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)
    # raise CommandError('Poll "%s" does not exist' % poll_id)

    def handle(self, *args, **options):
        filename = settings.MEDIA_ROOT + options['filename']
        out = add_samples_from_csv(filename)

        self.stdout.write("individuals_added: %s" % out['individuals_added'])
        self.stdout.write("specimens_added: %s" % out['specimens_added'])
        self.stdout.write("aliquots_added: %s" % out['aliquots_added'])

        for e in out['errors']:
            self.stdout.write("errors: %s" % e)
