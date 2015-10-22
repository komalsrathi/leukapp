# -*- coding: utf-8 -*-

# python
import csv
import os
import datetime

# django
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):

    """
    Gets create form fields for Individuals, Specimens and Aliquots
    """

    help = 'Gets create form fields for Individuals, Specimens and Aliquots'

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
