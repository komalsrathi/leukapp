APP_NAME = 'aliquots'

CREATE_FORM_FIELDS = [
    'specimen',
    'biological_material',
    'ext_id',
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
