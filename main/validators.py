from django.core.validators import RegexValidator

def phone_validator(value):
    validator = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    validator(value)