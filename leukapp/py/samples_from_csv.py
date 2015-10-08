# python
import csv

# django
from django import forms
from django.db.models import Q

# leukgen apps
from leukgen.apps.individuals.models import Individual
from leukgen.apps.specimens.models import Specimen
from leukgen.apps.aliquots.models import Aliquot

from leukgen.apps.individuals.constants import CREATE_FIELDS as IndiFields
from leukgen.apps.specimens.constants import CREATE_FIELDS as SpeFields
from leukgen.apps.aliquots.constants import CREATE_FIELDS as AliFields


class IndividualForm(forms.ModelForm):

    class Meta:
        model = Individual
        fields = IndiFields


class SpecimenForm(forms.ModelForm):

    class Meta:
        model = Specimen
        fields = SpeFields


class AliquotForm(forms.ModelForm):

    class Meta:
        model = Aliquot
        fields = AliFields


def add_samples_from_csv(filename):
    """ adds samples from csv """

    rows = open(filename)
    individuals_added = 0
    specimens_added = 0
    aliquots_added = 0
    errors = []

    # Generate a dict per row, with the first CSV row being the keys.
    for row in csv.DictReader(rows, delimiter=","):

        individuals_row = {}
        specimens_row = {}
        aliquots_row = {}

        individual = None
        specimen = None

        keys = list(row)

        for k in keys:
            schema, field = k.split('.')
            if schema == 'Individual':
                individuals_row[field] = row[k]
            elif schema == 'Specimen':
                specimens_row[field] = row[k]
            elif schema == 'Aliquot':
                aliquots_row[field] = row[k]

        try:
            individual = Individual.objects.get(
                Q(ext_id__iexact=individuals_row['ext_id']),
                Q(institution__iexact=individuals_row['institution']),
                Q(species__iexact=individuals_row['species']),
                )
        except Individual.DoesNotExist:
            individual_form = IndividualForm(individuals_row)
            if individual_form.is_valid():
                individual = individual_form.save()
                individuals_added += 1
            else:
                errors.append(individual_form.errors)

        if not individual:
            break
        else:
            try:
                specimen = Specimen.objects.get(
                    Q(individual=individual.pk),
                    Q(ext_id__exact=specimens_row['ext_id']),
                    Q(source__exact=specimens_row['source']),
                    )
            except Specimen.DoesNotExist:
                specimens_row['individual'] = individual.pk
                specimen_form = SpecimenForm(specimens_row)
                if specimen_form.is_valid():
                    specimen = specimen_form.save()
                    specimens_added += 1
                else:
                    errors.append(specimen_form.errors)

        if not specimen:
            break
        else:
            try:
                bm = aliquots_row['biological_material']
                Aliquot.objects.get(
                    Q(specimen=specimen.pk),
                    Q(biological_material__exact=bm),
                    Q(ext_id__exact=aliquots_row['ext_id']),
                    )
            except Aliquot.DoesNotExist:
                aliquots_row['specimen'] = specimen.pk
                aliquot_form = AliquotForm(aliquots_row)
                if aliquot_form.is_valid():
                    aliquot_form.save()
                    aliquots_added += 1
                else:
                    errors.append(aliquot_form.errors)

    out = {
        'individuals_added': individuals_added,
        'specimens_added': specimens_added,
        'aliquots_added': aliquots_added,
        'errors': errors,
        }

    return out
