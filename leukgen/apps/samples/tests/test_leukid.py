from django.test import TestCase
from ..leukid import *


class LeukidTest(TestCase):

    """docstring for ItemModelTest"""

    INTERNAL = 'I'
    EXTERNAL = 'E'

    INDIVIDUAL_SOURCE_CHOICES = (
        (INTERNAL, 'Internal'),
        (EXTERNAL, 'External'),
    )

    HUMAN = 'H'
    MOUSE = 'M'
    YEAST = 'Y'
    ZEBRAFISH = 'Z'

    INVIVIDUAL_SPECIES_CHOICES = (
        (HUMAN, 'Human'),
        (MOUSE, 'Mouse'),
        (YEAST, 'Yeast'),
        (ZEBRAFISH, 'Zebrafish'),
    )

    TUMOR = 'T'
    NORMAL = 'N'

    SPECIMEN_TYPE_CHOICES = (
        (TUMOR, 'Tumor'),
        (NORMAL, 'Normal'),
    )

    DNA = 'D'
    RNA = 'R'
    MIXED = 'M'

    ALIQUOT_MATERIAL_CHOICES = (
        (DNA, 'DNA'),
        (RNA, 'RNA'),
        (MIXED, 'MIXED'),
    )

    sample_fields = [
        'individual_source',
        'individual_species',
        'individual_ext_id',
        'specimen_type',
        'specimen_ext_id',
        'aliquot_material',
        'aliquot_ext_id',
    ]

    def test_(self):
        pass
