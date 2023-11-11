import re

from django.core.exceptions import ValidationError


def name_validator(value):
    if not  all(x.isalpha() or x.isspace() for x in value):
        raise ValidationError("Name can only contain letters and spaces")


def phone_validator(value):
    valid = re.match("^\+359\d{9}$", value)
    if not valid:
        raise ValidationError("Phone number must start with a '+359' followed by 9 digits")

