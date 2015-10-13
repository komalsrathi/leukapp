# python
import random

# leukapp
from leukapp.apps.individuals.utils import IndividualFactory
from leukapp.apps.specimens.utils import SpecimenFactory
from leukapp.apps.aliquots.utils import AliquotFactory


def create_samples_batch(i, s, a):
    """
    Creates a batch of samples.

    Input Args:
        i (int): number of individuals
        s (int): number of specimens per individual
        a (int): number of aliquots per specimen

    Returns:
        dictionary {
            'individuals': list of all individuals created
            'specimens': list of all specimens created
            'aliquots': list of all aliquots created
        }

    Raises:
        not defined yet

    tests: test_utils | test_create_samples_batch
    """

    individuals = IndividualFactory.create_batch(i)

    specimens = []
    for i in individuals:
        kwargs = {'individual': i}
        specimens += SpecimenFactory.create_batch(s, **kwargs)

    aliquots = []
    for s in specimens:
        kwargs = {'specimen': s}
        aliquots += AliquotFactory.create_batch(a, **kwargs)

    return {
        'individuals': individuals,
        'specimens': specimens,
        'aliquots': aliquots,
        }


def create_rows(individuals):

    create_batch()

    rows = []
    for i in individuals:
        row = {
            'Project.pk': random.randint(1, 1000),
            'Individual.institution': i.institution,
            'Individual.species': i.species,
            'Individual.ext_id': i.ext_id,
            'Specimen.source': i.specimen.source,
            'Specimen.ext_id': i.specimen.ext_id,
            'Aliquot.bio_source': i.specimen.aliquot.bio_source,
            'Aliquot.ext_id': i.specimen.aliquot.ext_id,
            }
        rows.append(row)

    return rows
