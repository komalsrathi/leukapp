from base64 import b64encode
import pandas as pd

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
    (HUMAN, 'H'),
    (MOUSE, 'M'),
    (YEAST, 'Y'),
    (ZEBRAFISH, 'Z'),
)


TUMOR = 'T'
NORMAL = 'N'

SPECIMEN_TYPE_CHOICES = (
    (TUMOR, 'T'),
    (NORMAL, 'N'),
)


DNA = 'D'
RNA = 'R'
MIXED = 'M'

ALIQUOT_MATERIAL_CHOICES = (
    (DNA, 'D'),
    (RNA, 'R'),
    (MIXED, 'M'),
)


individual_source
individual_species
individual_ext_id
specimen_type
specimen_ext_id
aliquot_material
aliquot_ext_id



b64encode(os.urandom(10)).decode('utf-8')
