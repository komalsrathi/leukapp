APP_NAME = 'individuals'

CREATE_URL = APP_NAME + ':create'
LIST_URL = APP_NAME + ':list'

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

CREATE_FORM_FIELDS = [
    'institution',
    'species',
    'ext_id',
    ]
