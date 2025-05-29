import os
from django.core.exceptions import ValidationError

def file_validator(value):
    ext = os.path.splitext(value.name)[1]
    valid_extens = ['.stl', '.glb']
    if not ext.lower() in valid_extens:
        raise ValidationError(f"Поддерживается только разрешения {valid_extens}")