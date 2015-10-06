APP_NAME = 'aliquots'

CREATE_URL = APP_NAME + ':create'
LIST_URL = APP_NAME + ':list'

CREATE_FIELDS = [
    'specimen',
    'biological_material',
    'ext_id',
]

UPDATE_FIELDS = [
    'specimen',
    'biological_material',
]

DNA = 'D'
RNA = 'R'
MIXED = 'M'
BIOLOGICAL_MATERIAL = (
    (DNA, 'DNA'),
    (RNA, 'RNA'),
    (MIXED, 'MIXED'),
)

CHOICES = {
    "BIOLOGICAL_MATERIAL": BIOLOGICAL_MATERIAL,
}
