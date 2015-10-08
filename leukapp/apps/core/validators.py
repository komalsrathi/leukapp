from django.core.validators import RegexValidator

phone = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'." +
        "Up to 15 digits allowed."
    )

name = RegexValidator(
    regex=r'^[a-zA-Z\s]$',
    message="Use under scores."
    )

object_name = RegexValidator(
    regex=r'^[-a-zA-Z0-9_\s]+\Z',
    message="Enter a valid name consisting of letters, numbers, white spaces"
        ", underscores or hyphens.",
    code='invalid'
    )
