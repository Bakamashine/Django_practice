"""Стандартные формы для регистрации или авторизации пользователя"""

from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UsernameField,
)
from django import forms
from .models import CustomAbstractUser

# """Перевод ошибок валидации"""
from django.utils.translation import gettext_lazy as _


# INPUT_STYLES = "mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-red-500 focus:border-red-500"
# Стили для полей ввода
INPUT_STYLES = "input1"


class RegisterForm(UserCreationForm):
    """Форма для регистрации пользователей"""

    username = forms.CharField(
        label="Логин", widget=forms.TextInput(attrs={"class": INPUT_STYLES})
    )
    email = forms.EmailField(
        label="Email", widget=forms.EmailInput(attrs={"class": INPUT_STYLES})
    )
    password1 = forms.CharField(
        label="Пароль", widget=forms.PasswordInput(attrs={"class": INPUT_STYLES})
    )
    password2 = forms.CharField(
        label="Повтор пароля", widget=forms.PasswordInput(attrs={"class": INPUT_STYLES})
    )

    class Meta:
        model = CustomAbstractUser
        fields = ("username", "email", "password1", "password2")


class LoginForm(AuthenticationForm):
    """Форма для авторизации пользователей"""

    username = UsernameField(
        widget=forms.TextInput(attrs={"autofocus": True, "class": INPUT_STYLES})
    )

    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "class": INPUT_STYLES}
        ),
    )


class AcceptEmail(forms.Form):
    """Поле для ввода токена с почты"""

    # code = forms.TextInput(attrs={"autofocus": True, "class": "input1"})
    code = forms.CharField(
        label=_("Code"),
        widget=forms.TextInput(
            attrs={"autofocus": True, "class": INPUT_STYLES}
        )
    )


    def clean_code(self):
        """Валидация токена"""
        code = self.cleaned_data.get("code")
        if code is not self.code:
            raise forms.ValidationError("Токены не совпадают")
        return code
