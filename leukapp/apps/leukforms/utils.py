# -*- coding: utf-8 -*-

# python
import csv
import io

from leukapp.apps.individuals.models import Individual

# local
from . import constants
from .forms import LEUKAPP_FORMS
from .validators import leukform_csv_validator

# useful dictionaries


class LeukformLoader(object):

    """
    """

    help = 'Gets create form fields for Individuals, Specimens and Aliquots'

    def __init__(self):
        super(LeukformLoader, self).__init__()

        # variables
        self.FORMS = LEUKAPP_FORMS
        self.MODELS = constants.LEUKAPP_MODELS
        self.MODELS_LIST = constants.MODELS_LIST
        self.UNIQUE_TOGETHER = constants.LEUKAPP_UNIQUE_TOGETHER

        # input
        self.rows = {}
        self.fields = {}

        # results data
        self.result = []
        self.added = {}
        self.existed = {}
        self.rejected = {}

        # initialize
        for model in self.MODELS:
            self.added[model] = []
            self.existed[model] = []
            self.rejected[model] = 0

    def submit(self, filename, validate=False):
        """ Process `leukform` from csv file using `filename` (str) """
        # NOTTESTED
        with open(filename, 'r') as leukform:
            if validate:
                leukform_csv_validator(leukform)
            reader = csv.reader(leukform)
            columns_submitted = next(reader)
            leukform.seek(0)
            rows = csv.DictReader(leukform, delimiter=",")
            return self.process_leukform(rows, columns_submitted)

    def process_leukform(self, rows, columns_submitted):
        """
        Process `leukform` from dictionary.
        Input: rows (dict): csv.DictReader type of dictionary
        Returns: json dictionary described in `self._write_output()`
        """
        self.rows = list(rows)
        self.columns_submitted = columns_submitted
        self._sort_rows()
        for row in self.rows:
            self.row = row
            self._process_row()
            self.result.append(row)

        # removes duplicates from existing instances
        for model in self.MODELS:
            self.existed[model] = set(self.existed[model])

        return self._write_output()

    def _sort_rows(self):
        """ Sorts rows based on `Individual.ext_id` and `Specimen.order` """
        # NOTTESTED
        try:
            for row in self.rows:
                if not row['Specimen.order']:
                    row['Specimen.order'] = str(0)
        except KeyError:
            pass

        keys = set(self.rows[0])
        c1 = set(['Individual.ext_id', 'Specimen.order']).issubset(keys)
        c2 = set(['Individual.slug', 'Specimen.order']).issubset(keys)
        c3 = c1 and c2
        if c1:
            self.rows = sorted(self.rows, key=lambda k: (
                k['Individual.ext_id'], int(k['Specimen.order'])))
        elif c2:
            self.rows = sorted(self.rows, key=lambda k: (
                k['Individual.slug'], int(k['Specimen.order'])))
        elif c3:
            self.rows = sorted(self.rows, key=lambda k: (
                k['Individual.ext_id'], int(k['Specimen.order'])))

    def _process_row(self):
        """ process csv rows """
        self._clean_row()
        for model in self.MODELS_LIST:
            if model in self.fields:
                # previous_model = model
                instance, msg = self._get_or_create(model=model)
                if (msg != 'ACCEPTED') and (msg != 'EXISTED'):
                    self.row['RESULT'] = msg
                    self.row['STATUS'] = 'REJECTED'
                    self.rejected[model] += 1
                    break

        if instance and (msg == 'EXISTED'):
            self.row['RESULT'] = instance.slug
            self.row['STATUS'] = ' EXISTED'
        elif instance and (msg == 'ACCEPTED'):
            self.row['RESULT'] = instance.slug
            self.row['STATUS'] = ' ACCEPTED'

        return self.row

    def _clean_row(self):
        """
        NOTTESTED
        Gets fields from rows.
        Input Args: row (dict): dict with keys as column names
        Returns: input: nested dictionary of models and its fields
        """
        if not self.row:
            raise Exception("The row is empty")

        for column in list(self.row):
            model, field = column.split('.')
            if self.row[column]:
                if model not in self.fields:
                    self.fields[model] = {}
                self.fields[model][field] = self.row[column]

    def _get_or_create(self, model):
        """
        NOTTESTED
        Gets or creates instance while collecting results data.
        Input Args: model (string): name of instance's model
        Returns:
            msj (json/str): json of errors and codes, str if existed
            instance (model): instance found or created
        """
        instance, msg = None, None

        try:
            if 'slug' in self.fields[model]:
                slug = self.fields[model]['slug']
                instance = self.MODELS[model].objects.get(slug=slug)
            else:
                unique = self.UNIQUE_TOGETHER[model]
                search = {k: self.fields[model][k] for k in unique}
                instance = self.MODELS[model].objects.get(**search)
            if instance not in self.added[model]:
                self.existed[model].append(instance)
            msg = 'EXISTED'
        except self.MODELS[model].DoesNotExist:
            form = self.FORMS[model](self.fields[model])
            if form.is_valid():
                instance = form.save(commit=True)
                self.added[model].append(instance)
                msg = 'ACCEPTED'
            else:
                msg = form.errors.as_json()

        # update foreing key for next model
        self._update_input(model, instance)
        return instance, msg

    def _update_input(self, model, instance):
        """ Updates child instances after parent are found or created. """
        if model == 'Individual' and instance and ('Specimen' in self.fields):
            self.fields['Specimen']['individual'] = instance.pk
        elif model == 'Specimen' and instance and ('Aliquot' in self.fields):
            self.fields['Aliquot']['specimen'] = instance.pk
        elif model == 'Aliquot' and instance and ('Run' in self.fields):
            self.fields['Run']['aliquot'] = instance.pk

    def _write_output(self):
        """ Process output dictionary including a csv results file """
        # NOTTESTED
        summary = self._write_summary()
        keys = self.columns_submitted
        keys.extend(['STATUS', 'RESULT'])
        result = io.StringIO()
        dict_writer = csv.DictWriter(result, keys)
        dict_writer.writeheader()
        dict_writer.writerows(self.result)
        result.seek(0)

        output = {
            "added": self.added,
            "existed": self.existed,
            "result": result,
            "summary": summary,
            }

        return output

    def _write_summary(self):
        """ writes out summary text"""
        summary = ''
        for model in self.MODELS_LIST:
            try:
                added = str(len(self.added[model]))
                existed = str(len(self.existed[model]))
                rejected = str(self.rejected[model])
                txt = '{0}s -> {1} added, {2} existed, {3} rejected.\n'
                summary += txt.format(model, added, existed, rejected)
            except KeyError:
                continue

        return summary
