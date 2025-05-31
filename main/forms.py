from django import forms
from main.validators import phone_validator
from RegAuth.forms import INPUT_STYLES


class FeedbackForm(forms.Form):
    phone = forms.CharField(
        max_length=24,
        validators=[phone_validator],
        required=True,
        widget=forms.TextInput(attrs={"class": INPUT_STYLES}),
        label="Номер телефона"
    )

    text = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={"class": INPUT_STYLES}),
        label="Описание"
    )
