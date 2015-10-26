# django
from django.core.management.base import BaseCommand, CommandError

# leukapp apps
from leukapp.apps.individuals.constants import INDIVIDUAL_CREATE_FIELDS
from leukapp.apps.specimens.constants import SPECIMEN_CREATE_FIELDS
from leukapp.apps.aliquots.constants import ALIQUOT_CREATE_FIELDS


class Command(BaseCommand):
    help = 'Gets create form fields for Individuals, Specimens and Aliquots'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)
    # raise CommandError('Poll "%s" does not exist' % poll_id)

    def handle(self, *args, **options):
        keys = ['Individual', 'Specimen', 'Aliquot']
        fields = {
            'Individuals': INDIVIDUAL_CREATE_FIELDS,
            'Specimens': SPECIMEN_CREATE_FIELDS,
            'Aliquots': ALIQUOT_CREATE_FIELDS,
            }
        for k in keys:
            for f in fields[k]:
                self.stdout.write('.'.join([k, f]))
