from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

phone_validator = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message=_("Phone number must be entered in the format: '+999999999'."
        "Up to 15 digits allowed.")
    )

name_validator = RegexValidator(
    regex=r'^[a-zA-Z\s]$',
    message=_("Use under scores.")
    )

object_name_validator = RegexValidator(
    regex=r'^[-a-zA-Z0-9_\s]+\Z',
    code='invalid',
    message=_("Enter a valid name consisting of letters, numbers, white spaces"
        ", underscores or hyphens."),
    )

# the ext_id_validator uses the same regex as
# django.core.validators.validate_slug
ext_id_validator = RegexValidator(
    regex=r'^[-a-zA-Z0-9_]+\Z',
    code='invalid',
    message=_("Enter a valid 'External id' consisting of"
        " letters, numbers, underscores or hyphens."),
    )
