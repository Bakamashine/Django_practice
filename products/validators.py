import os
from django.core.exceptions import ValidationError

VALID_EXTENS = ['.stl', '.glb']

def file_validator(value):
    ext = os.path.splitext(value.name)[1]
    if not ext.lower() in VALID_EXTENS:
        raise ValidationError(f"Поддерживается только разрешения {VALID_EXTENS}")