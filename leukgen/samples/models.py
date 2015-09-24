# django imports
from django.db import models

# local imports
from ..core.models import TimeStampedModel


class Individual(TimeStampedModel):

    """docstring for Individual"""

    # choices
    MSK = 'MSK'
    OTHER = 'O'
    SOURCE_CHOICES = (
        (MSK, 'Memorial Sloan-Kettering Cancer Center'),
        (OTHER, 'Other'),
    )

    HUMAN = 'H'
    MOUSE = 'M'
    YEAST = 'Y'
    ZEBRAFISH = 'Z'
    SPECIES_CHOICES = (
        (HUMAN, 'Human'),
        (MOUSE, 'Mouse'),
        (YEAST, 'Yeast'),
        (ZEBRAFISH, 'Zebrafish'),
    )

    # fields
    source = models.CharField(max_length=3, choices=SOURCE_CHOICES)
    species = models.CharField(max_length=1, choices=SPECIES_CHOICES)
    ext_id = models.CharField(max_length=100)

    # methods
    def check_source(self):
        if self.source == 'MSK':
            return 'I'
        else:
            return 'E'

    # meta options
    class Meta:
        index_together = (("ext_id", "source"))
        unique_together = (("ext_id", "source"))


class Specimen(TimeStampedModel):

    """docstring for Specimen"""

    # TUMOR = 'T'
    # NORMAL = 'N'

    # SPECIMEN_TYPE_CHOICES = (
    #     (TUMOR, 'Tumor'),
    #     (NORMAL, 'Normal'),
    # )

    # specimen_type = models.CharField(max_length=1, choices=)
    # specimen_ext_id = models.
    pass


class Aliquot(TimeStampedModel):

    """docstring for Aliquot"""

    # DNA = 'D'
    # RNA = 'R'
    # MIXED = 'M'

    # ALIQUOT_MATERIAL_CHOICES = (
    #     (DNA, 'DNA'),
    #     (RNA, 'RNA'),
    #     (MIXED, 'MIXED'),
    # )

    # aliquot_material = models.
    # aliquot_ext_id = models.
    pass
