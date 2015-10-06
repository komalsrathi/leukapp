# django
from django.core.management.base import BaseCommand, CommandError

# leukgen apps
from leukgen.apps.individuals.constants import CREATE_FIELDS as ind_fields
from leukgen.apps.specimens.constants import CREATE_FIELDS as spe_fields
from leukgen.apps.aliquots.constants import CREATE_FIELDS as ali_fields


class Command(BaseCommand):
    help = 'Gets create form fields for Individuals, Specimens and Aliquots'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)
    # raise CommandError('Poll "%s" does not exist' % poll_id)

    def handle(self, *args, **options):
        keys = ['Individual', 'Specimen', 'Aliquot']
        fields = {
            'Individuals': ind_fields,
            'Specimens': spe_fields,
            'Aliquots': ali_fields,
            }
        for k in keys:
            for f in fields[k]:
                self.stdout.write('.'.join([k, f]))
