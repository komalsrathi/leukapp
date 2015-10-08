# django
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

# leukapp apps
from leukapp.apps.individuals.constants import CREATE_FIELDS as ind_fields
from leukapp.apps.specimens.constants import CREATE_FIELDS as spe_fields
from leukapp.apps.aliquots.constants import CREATE_FIELDS as ali_fields
from leukapp.py.samples_from_csv import add_samples_from_csv


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
