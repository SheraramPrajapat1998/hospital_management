from datetime import datetime
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


def validate_future_date(date):
    if date > datetime.now().date():
        raise ValidationError("Date can't be in future!")


# def phone_number(number):
#     phone_regex = RegexValidator(
#         regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#     return phone_regex
