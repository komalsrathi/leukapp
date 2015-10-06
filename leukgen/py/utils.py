# python
import sys

# django
from django.core.management.base import BaseCommand, CommandError

# leukgen apps
from leukgen.apps.individuals.constants import CREATE_FIELDS as ind_fields
from leukgen.apps.specimens.constants import CREATE_FIELDS as spe_fields
from leukgen.apps.aliquots.constants import CREATE_FIELDS as ali_fields


class Command(BaseCommand):
    help = 'Gets create form fields for Individuals, Specimens and Aliquots'

    def add_arguments(self, parser):
        parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        for poll_id in options['poll_id']:
            try:
                poll = Poll.objects.get(pk=poll_id)
            except Poll.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            poll.opened = False
            poll.save()

            self.stdout.write('Successfully closed poll "%s"' % poll_id)


def get_individuals_specimens_aliquots_create_form_fields():
    fields = ind_fields + spe_fields + ali_fields
    return fields

if __name__ == '__main__':

    if sys.argv[1] == 'get_individuals_specimens_aliquots_create_form_fields':
        print(get_individuals_specimens_aliquots_create_form_fields())
