APP_NAME = 'individuals'

MSK = 'MSK'
OTHER = 'O'
INSTITUTION = (
    (MSK, 'Memorial Sloan-Kettering Cancer Center'),
    (OTHER, 'Other'),
)

HUMAN = 'H'
MOUSE = 'M'
YEAST = 'Y'
ZEBRAFISH = 'Z'
SPECIES = (
    (HUMAN, 'Human'),
    (MOUSE, 'Mouse'),
    (YEAST, 'Yeast'),
    (ZEBRAFISH, 'Zebrafish'),
)

CHOICES = {
    "INSTITUTION": INSTITUTION,
    "SPECIES": SPECIES,
}
