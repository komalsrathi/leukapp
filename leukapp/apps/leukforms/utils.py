# -*- coding: utf-8 -*-

# python
import csv
import io

# leukapp
from leukapp.apps.individuals.models import Individual
from leukapp.apps.specimens.models import Specimen
from leukapp.apps.aliquots.models import Aliquot
from leukapp.apps.runs.models import Run

from leukapp.apps.individuals.constants import INDIVIDUAL_UNIQUE_TOGETHER
from leukapp.apps.specimens.constants import SPECIMEN_UNIQUE_TOGETHER
from leukapp.apps.aliquots.constants import ALIQUOT_UNIQUE_TOGETHER
from leukapp.apps.runs.constants import RUN_UNIQUE_TOGETHER

# local
from .constants import LEUKFORM_CSV_FIELDS
from .forms import IndividualForm, SpecimenForm, AliquotForm, RunForm


class RunsFromCsv(object):

    """
    """

    help = 'Gets create form fields for Individuals, Specimens and Aliquots'

    def __init__(self):
        super(RunsFromCsv, self).__init__()

        # models list
        self.models_keys = ['Individual', 'Specimen', 'Aliquot', 'Run']

        self.unique_together = {
            'Individual': INDIVIDUAL_UNIQUE_TOGETHER,
            'Specimen': SPECIMEN_UNIQUE_TOGETHER,
            'Aliquot': ALIQUOT_UNIQUE_TOGETHER,
            'Run': RUN_UNIQUE_TOGETHER,
        }

        # models
        self.models = {
            'Individual': Individual,
            'Specimen': Specimen,
            'Aliquot': Aliquot,
            'Run': Run,
            }

        # forms
        self.forms = {
            'Individual': IndividualForm,
            'Specimen': SpecimenForm,
            'Aliquot': AliquotForm,
            'Run': RunForm
            }

        # row input
        self.input = {}

        # results data
        self.result = []
        self.added = {}
        self.existed = {}
        self.rejected = {}

        # initialize
        for model in self.models:
            self.input[model] = {}
            self.added[model] = []
            self.existed[model] = []
            self.rejected[model] = 0

    def submit(self, filename):
        """ Adds rows from csv file """
        with open(filename, 'r') as leukform:
            rows = csv.DictReader(leukform, delimiter=",")
            return self.save_runs_from_rows(rows)

    def save_runs_from_rows(self, rows):
        """ Adds runs from list of dictionaries  """
        self._process_rows(rows)
        summary = self._write_summary()
        return self._write_out(summary)

    def _write_summary(self):
        """ writes out summary text"""
        summary = ''
        for model in self.models_keys:
            added = str(len(self.added[model]))
            existed = str(len(self.existed[model]))
            rejected = str(self.rejected[model])
            txt = '{0}s -> {1} added, {2} existed, {3} rejected.\n'
            summary += txt.format(model, added, existed, rejected)
        return summary

    def _write_out(self, summary):
        """ Process output dictionary including a csv results file """
        keys = LEUKFORM_CSV_FIELDS.copy()
        keys.extend(['STATUS', 'RESULT'])
        result = io.StringIO()
        dict_writer = csv.DictWriter(result, keys)
        dict_writer.writeheader()
        dict_writer.writerows(self.result)
        result.seek(0)

        out = {
            "added": self.added,
            "existed": self.existed,
            "result": result,
            "summary": summary,
            }

        return out

    def _process_rows(self, rows):
        """ process csv rows """

        rows = self._sort_rows(rows)
        for row in rows:
            self._fields_from_row(row)
            row['RESULT'] = None
            row['STATUS'] = None

            for model in self.models_keys:
                instance, errors = self._get_or_create(model=model)
                if errors:
                    row['RESULT'] = errors
                    row['STATUS'] = 'REJECTED'
                    self.rejected[model] += 1
                    break

            if not row['RESULT']:
                row['RESULT'] = instance.slug
                row['STATUS'] = 'ACCEPTED'

            self.result.append(row)

        # removes duplicates from existing instances
        for model in self.models:
            self.existed[model] = set(self.existed[model])

    def _sort_rows(self, rows):
        """ Sorts rows based on Run.order column """
        return sorted(
            rows,
            key=lambda k: (
                k['Individual.ext_id'],
                k['Specimen.ext_id'],
                k['Aliquot.ext_id'],
                int(k['Run.order']),
                )
            )

    def _fields_from_row(self, row):
        """
        Gets fields from rows.

        Input Args:
            row (dict): dict with keys as column names
        Returns:
            input: nested dictionary, first lever are models
                second level are leuk_form fields
        """
        if not row:
            return self.input

        keys = list(row)
        for k in keys:
            model, field = k.split('.')
            if field == 'projects' and model == 'Run':
                try:
                    # parse projects
                    projects = [int(e) for e in row[k].split("|")]
                    self.input[model][field] = projects
                except Exception:
                    self.input[model][field] = row[k]
            else:
                self.input[model][field] = row[k]

        return self.input

    def _get_or_create(self, model):
        """
        Gets or creates instance while collecting results data.

        Input Args:
            model (string): name of instance's model
        Returns:
            errors (json): json of errors and codes
            instance (model): instance found or created
        """
        errors, instance = None, None
        form = self.forms[model](self.input[model])
        search = {k: self.input[model][k] for k in self.unique_together[model]}

        try:
            if not self.input[model]:
                raise self.models[model].DoesNotExist
            instance = self.models[model].objects.get(**search)
            if instance not in self.added[model]:
                self.existed[model].append(instance)
        except self.models[model].DoesNotExist as e:
            print(e, search)
            if form.is_valid():
                instance = form.save()
                self.added[model].append(instance)
            else:
                errors = form.errors.as_json()

        # update foreing key for next model
        self._update_input(model, instance)
        return instance, errors

    def _update_input(self, model, instance):
        """ Updates child instances after parent are found or created. """
        if model == 'Individual' and instance:
            self.input['Specimen']['individual'] = instance.pk
        elif model == 'Specimen' and instance:
            self.input['Aliquot']['specimen'] = instance.pk
        elif model == 'Aliquot' and instance:
            self.input['Run']['aliquot'] = instance.pk
