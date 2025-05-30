from django import forms
from main.validators import phone_validator
from RegAuth.forms import INPUT_STYLES


class FeedbackForm(forms.Form):
    phone = forms.CharField(
        max_length=24,
        validators=[phone_validator],
        required=True,
        help_text="Введите свой номер телефона",
        widget=forms.TextInput(attrs={"class": INPUT_STYLES}),
    )

    text = forms.CharField(
        required=True,
        help_text="Введите ваше сообщение",
        widget=forms.Textarea(attrs={"class": INPUT_STYLES}),
    )
