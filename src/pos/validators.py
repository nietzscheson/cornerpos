from django.utils.timezone import localdate
from django.core.exceptions import ValidationError


def validate_date(date):
    if date < localdate():
        raise ValidationError(
            code="invalid_datetime",
            message="The menu date must be equal to or greater than today",
        )
