APP_NAME = 'specimens'

CREATE_URL = APP_NAME + ':create'
LIST_URL = APP_NAME + ':list'

TUMOR = 'T'
NORMAL = 'N'
SOURCE = (
    (TUMOR, 'Tumor'),
    (NORMAL, 'Normal'),
)

CHOICES = {
    "SOURCE": SOURCE,
}

CREATE_FIELDS = [
    'individual',
    'source',
    'ext_id',
    ]

UPDATE_FIELDS = [
    'individual',
    'source',
    ]
