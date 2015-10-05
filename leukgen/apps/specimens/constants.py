APP_NAME = 'specimens'

TUMOR = 'T'
NORMAL = 'N'
SOURCE = (
    (TUMOR, 'Tumor'),
    (NORMAL, 'Normal'),
)

CHOICES = {
    "SOURCE": SOURCE,
}

CREATE_FORM_FIELDS = [
    'individual',
    'source',
    'ext_id',
    ]
