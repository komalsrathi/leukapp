from django.db import models


class Individual(models.Model):

    """docstring for Individual"""

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

    individual_source = models.CharField(
                            max_length=1,
                            choices=INDIVIDUAL_SOURCE_CHOICES,
                            default=INTERNAL
                        )
    individual_species = models.
    individual_ext_id = models.


class Specimen(models.Model):

    """docstring for Specimen"""

    TUMOR = 'T'
    NORMAL = 'N'

    SPECIMEN_TYPE_CHOICES = (
        (TUMOR, 'Tumor'),
        (NORMAL, 'Normal'),
    )

    specimen_type = models.CharField(max_length=1, choices=)
    specimen_ext_id = models.


class Aliquot(models.Model):

    """docstring for Aliquot"""

    DNA = 'D'
    RNA = 'R'
    MIXED = 'M'

    ALIQUOT_MATERIAL_CHOICES = (
        (DNA, 'DNA'),
        (RNA, 'RNA'),
        (MIXED, 'MIXED'),
    )

    aliquot_material = models.
    aliquot_ext_id = models.
