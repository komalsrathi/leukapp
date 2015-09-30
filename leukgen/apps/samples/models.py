# django imports
from django.db import models

# apps imports
from core.models import TimeStampedModel


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
        index_together = (("ext_id", "source", "species"))
        unique_together = (("ext_id", "source", "species"))


# class Specimen(TimeStampedModel):

#     """docstring for Specimen"""

#     # choices
#     TUMOR = 'T'
#     NORMAL = 'N'
#     SOURCE_TYPE_CHOICES = (
#         (TUMOR, 'Tumor'),
#         (NORMAL, 'Normal'),
#     )

#     # fields
#     individual = models.ForeignKey(Individual)
#     source_type = models.CharField(max_length=1, choices=SOURCE_TYPE_CHOICES)
#     ext_id = models.CharField(max_length=100)


# class Aliquot(TimeStampedModel):

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
    # pass
