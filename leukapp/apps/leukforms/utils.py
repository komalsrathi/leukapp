# -*- coding: utf-8 -*-

# python
import csv
import io

# local
from . import constants
from .validators import leukform_csv_validator, leukform_rows_validator

# useful dictionaries


class LeukformLoader(object):

    """
    """

    help = 'Gets create form fields for Individuals, Specimens and Aliquots'

    def __init__(self):
        super(LeukformLoader, self).__init__()

        # results data
        self.added = {}
        self.existed = {}
        self.rejected = {}

        # initialize
        for model in constants.LEUKAPP_MODELS:
            self.added[model] = []
            self.existed[model] = []
            self.rejected[model] = 0

    def submit(self, filepath=None, rows=None, validate=True):
        """ NOTTESTED
        Process `leukform` from csv file using `filepath` or from a list of
        dictionaries using rows. If validate, then the input is validated.

        Input:
            filepath (str): path to csv file
            rows (list): csv.DictReader list of dictionaries
            validate (boolean): If validate, then the input is validated
        Returns:
            json dictionary described in `self._write_output()`
        Raises:
            Exception: if neither filepath nor rows are provided; or if both.
        """
        if filepath and rows:
            raise Exception("Provide only csv path or a list of dictionaries")
        elif not filepath and not rows:
            raise Exception("Provide a csv path or a list of dictionaries")

        if rows:
            rows = list(rows)
            if validate:
                leukform_rows_validator(rows)
            columns = list(rows[0])

        elif filepath:
            if validate:
                leukform_csv_validator(filepath)
            with open(filepath, 'r') as leukform:
                reader = csv.reader(leukform)
                columns = list(next(reader))
                leukform.seek(0)
                rows = list(csv.DictReader(leukform, delimiter=","))

        else:
            raise Exception("Provide a csv filepath or a list of dictionaries")

        rows = self._process_leukform(rows)
        output = self._write_output(rows, columns)
        return output

    def _process_leukform(self, rows):
        """
        Process `leukform` from dictionary.
        Input: rows (list): csv.DictReader list of dictionaries
        Returns: json dictionary described in `self._write_output()`
        """

        processed_rows = []
        rows = self._sort_rows(rows)
        for row in rows:
            processed_row = self._process_row(row)
            processed_rows.append(processed_row)
        return processed_rows

    def _sort_rows(self, rows):
        """
        Sorts rows based on `Individual.ext_id` and `Specimen.order`
        Input: rows (list): csv.DictReader list of dictionaries
        Returns: json dictionary described in `self._write_output()`
        """
        keys = set(rows[0])

        if 'Specimen.order' in keys:
            for row in rows:
                if row['Specimen.order'] is not None:
                    row['Specimen.order'] = str(0)
        else:
            return rows

        c1 = set(['Individual.ext_id', 'Specimen.order']).issubset(keys)
        c2 = set(['Individual.slug', 'Specimen.order']).issubset(keys)
        c3 = c1 and c2

        if c3:
            rows = sorted(rows, key=lambda k: (
                k['Individual.ext_id'],
                k['Individual.slug'],
                int(k['Specimen.order'])))
        elif c1:
            rows = sorted(rows, key=lambda k: (
                k['Individual.ext_id'], int(k['Specimen.order'])))
        elif c2:
            rows = sorted(rows, key=lambda k: (
                k['Individual.slug'], int(k['Specimen.order'])))

        return rows

    def _process_row(self, row):
        """
        Process the current row.

        First, the leukform `fields` are obtained from `row` using
        `_get_fields`. Then, for each model in `MODELS_LIST`, an istance is
        `get_or_created` if the model is in `fields`. If the object is created
        or found, the fields are updated to add the parent foreing key.

        Input: row (dict): csv.DictReader type of dictionary
        Returns: row (dict): a processed row with its result and status
        """
        fields = self._get_fields(row)
        for model in constants.MODELS_LIST:
            if model in fields:
                instance, msg = self._get_or_create(model, fields)
                if instance:
                    fields = self._update_fields(model, fields, instance)
                else:
                    row['RESULT'] = msg
                    row['STATUS'] = 'REJECTED'
                    break

        if (msg == 'EXISTED') or (msg == 'ACCEPTED'):
            row['RESULT'] = instance.slug
            row['STATUS'] = msg

        return row

    def _get_fields(self, row):
        """
        Gets `fields` from `row`. If the field is empty, is not added
        Input:
            row (dict): csv.DictReader type of dictionary
        Returns:
            fields (dict): a dict of dicts, first level models, then fields
        """
        fields = {}

        if not row:
            return fields
        for column in list(row):
            if row[column]:
                model, field = column.split('.')
                if model not in fields:
                    fields[model] = {}
                fields[model][field] = row[column]

        return fields

    def _get_or_create(self, model, fields):
        """
        Gets or creates an instance while collecting results data.
        Input:
            model (string): name of instance's model
            fields (dict): a dict of dicts, first level models, then fields
        Returns:
            msj (str): json of errors and codes or string if existed or created
            instance (Leukapp Model): instance found or created
        """
        instance, msg = None, None
        MODEL = constants.LEUKAPP_MODELS[model]
        FORM = constants.LEUKAPP_FORMS[model]

        if 'slug' in fields[model]:  # if slug, use it to find the object
            try:
                msg = 'EXISTED'
                slug = fields[model]['slug']
                instance = MODEL.objects.get(slug=slug)
                if instance not in self.added[model]:
                    self.existed[model].append(instance)
            except MODEL.DoesNotExist:
                msg = 'SLUG NOT FOUND'
                self.rejected[model] += 1

        else:  # if not slug, find or create the object using all its data
            try:
                msg = 'EXISTED'
                unique = constants.LEUKAPP_UNIQUE_TOGETHER[model]
                search = {k: fields[model][k] for k in unique}
                instance = MODEL.objects.get(**search)
                if instance not in self.added[model]:
                    self.existed[model].append(instance)
            except MODEL.DoesNotExist:
                form = FORM(fields[model])
                if form.is_valid():
                    msg = 'ACCEPTED'
                    instance = form.save(commit=True)
                    self.added[model].append(instance)
                else:
                    msg = form.errors.as_json()
                    self.rejected[model] += 1

        return instance, msg

    def _update_fields(self, model, fields, instance):
        """
        Updates child fields after parent is found or created.
        Input Args:
            model (string): name of instance's model
            fields (dict): a dict of dicts, first level models, then fields
            instance (Leukapp Model): instance found or created
        Returns:
            fields (dict): a dict of dicts, first level models, then fields
        """
        if model == 'Individual' and instance and ('Specimen' in fields):
            fields['Specimen']['individual'] = instance.pk
        elif model == 'Specimen' and instance and ('Aliquot' in fields):
            fields['Aliquot']['specimen'] = instance.pk
        elif model == 'Aliquot' and instance and ('Run' in fields):
            fields['Run']['aliquot'] = instance.pk
        return fields

    def _write_output(self, rows, columns):
        """
        Process output dictionary including a csv results file
        """

        for model in constants.LEUKAPP_MODELS:
            self.existed[model] = set(self.existed[model])

        summary = self._write_summary()
        keys = columns
        keys.extend(['STATUS', 'RESULT'])
        result = io.StringIO()
        dict_writer = csv.DictWriter(result, keys)
        dict_writer.writeheader()
        dict_writer.writerows(rows)
        result.seek(0)

        output = {
            "added": self.added,
            "existed": self.existed,
            "result": result,
            "summary": summary,
            }

        return output

    def _write_summary(self):
        """
        writes out summary text
        """
        summary = ''
        for model in constants.MODELS_LIST:
            added = str(len(self.added[model]))
            existed = str(len(self.existed[model]))
            rejected = str(self.rejected[model])
            txt = '{0}s -> {1} added, {2} existed, {3} rejected.\n'
            summary += txt.format(model, added, existed, rejected)

        return summary
