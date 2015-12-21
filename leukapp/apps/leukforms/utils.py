# -*- coding: utf-8 -*-

# python
# import time
import csv
import io
import json

# leukapp
from leukapp.apps.core.constants import UNKNOWN

# local
from . import constants
from .validators import leukform_csv_validator


def get_out_columns(columns):
    """NOTTESTED NOTDOCUMENTED"""
    out_columns = []
    for model in constants.MODELS_LIST:
        fields = constants.CREATE_FIELDS[model]
        fields = ['.'.join([model, field]) for field in fields]
        fields.append(model + ".slug")
        for field in fields:
            if (field in columns):
                out_columns.append(field)
    return out_columns


class LeukformLoader(object):

    """
    """

    help = 'Gets create form fields for Individuals, Specimens and Aliquots'

    def __init__(self):
        super(LeukformLoader, self).__init__()

        # constants
        self.VALID_MESSAGE = 'ACCEPTED'
        self.REJECTED_MESSAGE = 'REJECTED'
        self.EXISTED_MESSAGE = 'EXISTED'

        # results data
        self.added = {}
        self.existed = {}
        self.rejected = {}

        # initialize
        for model in constants.LEUKAPP_MODELS:
            self.added[model] = []
            self.existed[model] = []
            self.rejected[model] = 0

    def submit(self, filepath=None, rows=None, validate=True, mock=False):
        """
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
                # leukform_rows_validator(rows)
                pass
            columns = list(rows[0])

        elif filepath:
            if validate:
                leukform_csv_validator(filepath)
            with open(filepath, 'r') as leukform:
                reader = csv.reader(leukform, dialect=csv.excel)
                columns = list(next(reader))
                leukform.seek(0)
                rows = list(csv.DictReader(
                        leukform, delimiter=",", dialect=csv.excel))

        else:
            raise Exception("Provide a csv filepath or a list of dictionaries")

        if mock:
            self.VALID_MESSAGE = 'VALID_MESSAGE'

        # print("Validation completed.")
        columns = get_out_columns(columns)
        rows = self._process_leukform(rows)
        output = self._write_output(rows, columns, mock)
        return output

    def _process_leukform(self, rows):
        """
        Process `leukform` from dictionary.
        Input: rows (list): csv.DictReader list of dictionaries
        Returns: json dictionary described in `self._write_output()`
        """

        processed_rows = []
        rows = self._sort_rows(rows)

        count = 0
        # start = time.time()
        for row in rows:
            processed_row = self._process_row(row)
            processed_rows.append(processed_row)
            count += 1
            # print("%s rows processed in %s." % (count, time.time() - start))
        # print(time.time() - start)
        return processed_rows

    def _sort_rows(self, rows):
        """
        Sorts rows based on `Individual.ext_id` and `Specimen.order`
        Input: rows (list): csv.DictReader list of dictionaries
        Returns: json dictionary described in `self._write_output()`
        """
        columns = set(rows[0])

        if 'Specimen.order' in columns:
            rows = self._clean_specimen_order_column(rows)
        else:
            return rows

        c1 = {'Individual.ext_id', 'Specimen.order'}.issubset(columns)
        c2 = {'Individual.slug', 'Specimen.order'}.issubset(columns)
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

    def _clean_specimen_order_column(self, rows):
        """ simply adds zeros when Specimen.order is blank """
        for row in rows:
            if row['Specimen.order'] == '':
                row['Specimen.order'] = str(0)
        return rows

    def _process_row(self, row):
        """
        Process the current row.

        First, the leukform fields are obtained from row using
        _get_fields. Then, for each model in MODELS_LIST, an istance is
        get_or_created if the model is in fields. If the object is created
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
                    row['STATUS'] = self.REJECTED_MESSAGE
                    break

        if (msg == self.EXISTED_MESSAGE) or (msg == self.VALID_MESSAGE):
            row['RESULT'] = instance.slug
            row['STATUS'] = msg

        return row

    def _get_fields(self, row):
        """
        Get `fields` from `row`. If the field is empty, is not added.

        Input:
            row (dict): csv.DictReader type of dictionary

        Returns:
            fields (dict): a dict of dicts, first level models, then fields
        """
        if not row:
            return {}

        fields = {}
        columns = set(row)
        row = self._alter_row_special_case(row)

        for column in columns:
            model, field = column.split('.')
            if row[column]:
                if model not in fields:
                    fields[model] = {}
                fields[model][field] = row[column].strip()

        return fields

    def _alter_row_special_case(self, row):
        """
        Replace
        Test the case when only the Individual and/or Specimen ext_id are
        available. In this situation the leukform will be submitted with empty
        Specimen.ext_id and empty Aliquot.ext_id if only Individual.ext_id is
        available. Or, with empty Aliquot.ext_id if only the Individual and
        Specimen ext_id are available. Then, the empty fields will be set to 1.

        Input:
            row (dict): csv.DictReader type of dictionary
        """
        for column in constants.UNKWOWN_ENABLED_COLUMNS:
            try:
                if not row[column]:
                    row[column] = UNKNOWN
            except KeyError:
                continue
        return row

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
        exceptions = (
            MODEL.DoesNotExist,
            MODEL.MultipleObjectsReturned,
            KeyError,
            )

        if 'slug' in fields[model]:  # if slug, use it to find the object
            try:
                msg = self.EXISTED_MESSAGE
                slug = fields[model]['slug']
                instance = MODEL.objects.get(slug=slug)
                if instance not in self.added[model]:
                    self.existed[model].append(instance)
            except MODEL.DoesNotExist:
                msg = 'SLUG NOT FOUND'
                self.rejected[model] += 1

        else:  # if not slug, find or create the object using all its data
            try:
                unique = constants.LEUKAPP_UNIQUE_TOGETHER[model]
                if not unique:  # if there isn't unique condition, create it!
                    raise MODEL.DoesNotExist
                msg = self.EXISTED_MESSAGE
                search = {k: fields[model][k] for k in unique}
                instance = MODEL.objects.get(**search)
                if instance not in self.added[model]:
                    self.existed[model].append(instance)
            except exceptions:
                form = FORM(fields[model])
                if form.is_valid():
                    msg = self.VALID_MESSAGE
                    instance = form.save(commit=True)
                    self.added[model].append(instance)
                else:
                    # print(search)
                    msg = form.errors.as_json()
                    self.rejected[model] += 1

        return instance, msg

    def _update_fields(self, model, fields, instance):
        """
        Update child fields after parent is found or created.

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
        elif model == 'Aliquot' and instance and ('Extraction' in fields):
            fields['Extraction']['aliquot'] = instance.pk
        elif model == 'Extraction' and instance and ('Workflow' in fields):
            fields['Workflow']['extraction'] = instance.pk
        return fields

    def _write_output(self, rows, columns, mock=False):
        """ NOTTESTED
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

        if mock:
            self._delete_added_models()

        return output

    def _delete_added_models(self):
        """ deletes current added models """
        for model in constants.MODELS_LIST[::-1]:
            for instance in self.added[model]:
                try:
                    instance.delete()
                except AssertionError:
                    continue

    def _write_summary(self):
        """ NOTTESTED
        writes out summary text
        """
        summary = {}
        for model in constants.MODELS_LIST:
            summary[model] = {
                "valid": len(self.added[model]),
                "existed": len(self.existed[model]),
                "rejected": self.rejected[model],
                }
        return json.dumps(summary)
