# django imports
from django.test import TestCase
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

# local
from ..validators import ext_id_validator


class CoreValidatorsTest(TestCase):

    def test_ext_id_validator_doesnt_allow_white_spaces(self):
        with self.assertRaises(ValidationError):
            ext_id_validator("Juan San")

    def test_ext_id_validator_does_allow_periods(self):
        self.assertEqual(None, ext_id_validator("asdf.asfs.sdaf"))

    def test_ext_id_validator_displays_correct_msg(self):
        msg = "Enter a valid 'External id' consisting of" \
            " letters, numbers, underscores or hyphens."
        try:
            ext_id_validator("Juan San")
        except ValidationError as e:
            self.assertEqual(e.message, _(msg))
