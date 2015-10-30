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
from .constants import LEUKFORM_CSV_FIELDS, MODELS
from .forms import IndividualForm, SpecimenForm, AliquotForm, RunForm
from .validators import leukform_csv_validator, leukform_rows_validator


class LeukformLoader(object):

    """
    """

    help = 'Gets create form fields for Individuals, Specimens and Aliquots'

    def __init__(self):
        super(LeukformLoader, self).__init__()

        # variables
        self.rows = {}
        self.MODELS = MODELS

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

    def submit(self, csvpath):
        """ Process `leukform` from csv file using `csvpath` (str) """
        if leukform_csv_validator(csvpath):
            with open(csvpath, 'r') as leukform:
                leukform_csv_validator(leukform)
                rows = csv.DictReader(leukform, delimiter=",")
                return self.process_leukform(rows)

    def process_leukform(self, rows):
        """
        Process `leukform` from dictionary.
        Input: rows (dict): csv.DictReader type of dictionary
        Returns: json dictionary described in `self._write_out()`
        """
        self.rows = list(rows)
        self._process_rows()
        return self._write_out()

    def _process_rows(self):
        """ process csv rows """

        self._sort_rows()
        for row in self.rows:
            row = self._process_row(row)
            self.result.append(row)

        # removes duplicates from existing instances
        for model in self.models:
            self.existed[model] = set(self.existed[model])

    def _sort_rows(self):
        """ Sorts rows based on `Individual.ext_id` and `Specimen.order` """
        self.rows = sorted(
            self.rows,
            key=lambda k: (
                k['Individual.ext_id'],
                k['Individual.leukid'],
                int(k['Specimen.order']),
                )
            )

    def _process_row(self, row):
        """ process csv rows """
        fields = self._get_fields_from_row(row)
        for model in self.MODELS:
            instance, errors = self._get_or_create(model=model)
            if errors:
                result, status = errors, 'REJECTED'
                self.rejected[model] += 1
                break

        if (not row['RESULT']) and (instance in self.added['Run']):
            row['RESULT'] = instance.slug
            row['STATUS'] = 'ACCEPTED'
        elif (not row['RESULT']):
            row['RESULT'] = instance.slug
            row['STATUS'] = 'EXISTED'

        row['RESULT'], row['STATUS'] = result, status
        return row

    def _get_fields_from_row(self, row):
        """
        Gets fields from rows.

        Input Args:
            row (dict): dict with keys as column names
        Returns:
            input: nested dictionary, first lever are models
                second level are leuk_form fields
        """
        fields = {}
        if not row:
            return fields

        for column in list(row):
            model, field = column.split('.')
            fields[model][field] = self._clean_field(row, column)

        return fields

    def _clean_field(self, row, column):
        """
        clean field based on preprocessing rules.

        Input Args:
            row (dict): dict with keys as column names
            column (str): column name for the field to be cleaned
        Returns:
            value (not fixed): cleaned value
        """
        model, field = column.split('.')
        value = row[column]

        if field == 'projects' and model == 'Run':
            try:
                value = [int(e) for e in row[column].split("|")]
            except Exception:
                pass

        return value

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

        try:
            if not self.input[model]:
                raise self.models[model].DoesNotExist
            unique = self.unique_together[model]
            search = {k: self.input[model][k] for k in unique}
            instance = self.models[model].objects.get(**search)
            if instance not in self.added[model]:
                self.existed[model].append(instance)
        except self.models[model].DoesNotExist:
            form = self.forms[model](self.input[model])
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

    def _write_out(self):
        """ Process output dictionary including a csv results file """
        summary = self._write_summary()
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

    def _write_summary(self):
        """ writes out summary text"""
        summary = ''
        for model in self.MODELS:
            added = str(len(self.added[model]))
            existed = str(len(self.existed[model]))
            rejected = str(self.rejected[model])
            txt = '{0}s -> {1} added, {2} existed, {3} rejected.\n'
            summary += txt.format(model, added, existed, rejected)
        return summary
