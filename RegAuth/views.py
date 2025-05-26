"""Контроллеры свзяанные с регистрацией или авторизацией"""

from django.views.generic.edit import CreateView
from django.shortcuts import redirect, render
from .forms import RegisterForm, LoginForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import resolve_url
from django.views import View
from django.core.mail import send_mail
from django.template.loader import render_to_string
from RegAuth.models import CustomAbstractUser
from .decorators import anon_required
from smtplib import SMTPRecipientsRefused, SMTPDataError
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.conf import settings
from django.http import Http404


class SendEmail:
    """Отправка письма на почту"""

    def __init__(self, user: CustomAbstractUser):
        self.user = user
        self.token = default_token_generator.make_token(user)
        self.uid = urlsafe_base64_encode(str(self.user.pk).encode())

    def send_active_email(self):
        send_mail(
            f"Уважаемый {self.user.username}!",
            "",
            settings.EMAIL_HOST_USER,
            [self.user.email],
            html_message=render_to_string(
                "RegAuth/message.html",
                {
                    "user": self.user.username,
                    "token": self.token,
                    "uid": self.uid,
                },
            ),
        )


class AnonRequired(View):
    """
    Перенаправление на главную страницу если пользователь авторизирован
    В данный момент это будет осуществляться при переходе на страницу регистрации или авторизации
    Только для классов-контроллеров
    """

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            return super().dispatch(request, *args, **kwargs)


class CustomRegisterView(AnonRequired, CreateView):
    """Переопределённый класс регистрации"""

    form_class = RegisterForm
    template_name = "RegAuth/register.html"

    def form_valid(self, form):
        try:
            user: CustomAbstractUser = form.save()
            user.token = default_token_generator.make_token(user)
            user.save()
            mail = SendEmail(user=user)
            mail.send_active_email()

            return redirect("acceptEmail")
        # except SMTPRecipientsRefused:
        #     user.delete()
        #     form.add_error("email", "Такой почты не существует")
        #     return self.form_invalid(form)
        except SMTPDataError:
            user.delete()
            form.add_error("email", "Такой почты не существует")
            return self.form_invalid(form)

class CustomLogin(AnonRequired, LoginView):
    """Переопределённый метод авторизации"""

    form_class = LoginForm
    template_name = "RegAuth/login.html"


class CustomLogout(LogoutView):
    """Переопределённый класс Деавторизации"""

    template_name = None

    def get_default_redirect_url(self):
        return resolve_url(settings.LOGIN_REDIRECT_URL)


# @anon_required
# def accept_email(request, username, email, password):
#     """
#     Страница для подтверждения электронной почты
#     (ввод данных с письма)
#     """

#     form = AcceptEmail()
#     mycode = CODE
#     hash_code = hash_string(CODE)

#     return render(
#         request,
#         "RegAuth/acceptEmail.html",
#         {
#             "form": form,
#             "code": mycode,
#             "code_hashed": hash_code,
#             "username": username,
#             "email": email,
#             "password": password,
#         },
#     )


# @anon_required
# def accept_email2(request, code: str, username, email, password):
#     if request.method == "GET":
#         mycode = hash_string(request.GET.get("code"))
#         if mycode == code:
#             user = CustomAbstractUser(username=username, email=email, password=password)
#             user.is_active = True
#             user.save()

#             login(request, user)
#             return redirect("main")
#     return HttpResponse(404)


@anon_required
def accept_email(request):
    return render(request, "RegAuth/acceptEmail.html")


@anon_required
def accept_email2(request, token, uid):
    if request.method == "GET":
        id = urlsafe_base64_decode(uid)
        user = CustomAbstractUser.objects.get(pk=id)
        if token == user.token:
            user.is_active = True
            user.save()
            return redirect("main")
        else:
            return Http404("Такого пользователя не существует")
