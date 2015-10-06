APP_NAME = 'individuals'

CREATE_URL = APP_NAME + ':create'
LIST_URL = APP_NAME + ':list'

CREATE_FIELDS = [
    'institution',
    'species',
    'ext_id',
    ]

UPDATE_FIELDS = [
    'institution',
    'species',
    ]

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
