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
from RegAuth.decorator import anon_required
from smtplib import SMTPRecipientsRefused, SMTPDataError
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.conf import settings
from django.http import Http404, HttpResponse, HttpRequest
from django.contrib.auth import login
from django.contrib.sites.models import Site


class SendEmail:
    """Отправка письма на почту"""

    def __init__(self, user: CustomAbstractUser):
        self.user = user
        self.token = default_token_generator.make_token(user)
        self.uid = urlsafe_base64_encode(str(self.user.pk).encode())


    def send_active_email(self):
        domain = Site.objects.get_current().domain

        # url = "https://%s%s" % (Site.objects.get_current().domain, f"/accept/{self.token}/{self.uid}")
        token_url = f"accept/{self.token}/{self.uid}"
        url = f"http://{domain}/{token_url} "
        send_mail(
            f"Уважаемый {self.user.username}!",
            "",
            settings.EMAIL_HOST_USER,
            [self.user.email],
            html_message=render_to_string(
                "RegAuth/message.html",
                {
                    # "user": self.user.username,
                    # "token": self.token,
                    # "uid": self.uid,
                
                    "url": url
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
        return super().dispatch(request, *args, **kwargs)


class CustomRegisterView(AnonRequired, CreateView):
    """Переопределённый класс регистрации"""

    form_class = RegisterForm
    template_name = "RegAuth/register.html"

    def form_valid(self, form):
        user: CustomAbstractUser = form.save()
        try:
            user.token = default_token_generator.make_token(user)
            user.save()
            mail = SendEmail(user=user)
            mail.send_active_email()
            return redirect("acceptEmail")
        except SMTPDataError:
            user.delete()
            form.add_error("email", "Такой почты не существует")
            return self.form_invalid(form)
        except:
            user.delete()
            form.add_error("email", "Ошибка с отправкой письма")
            return self.form_invalid(form)


class CustomLoginView(AnonRequired, LoginView):
    """Переопределённый метод авторизации"""

    form_class = LoginForm
    template_name = "RegAuth/login.html"


class CustomLogout(LogoutView):
    """Переопределённый класс Деавторизации"""

    template_name = ""

    def get_default_redirect_url(self):
        return resolve_url(settings.LOGIN_REDIRECT_URL)


@anon_required
def accept_email(request):
    """Простой вывод о том, что сообщение было отправлено"""
    return render(request, "RegAuth/acceptEmail.html")


@anon_required
def accept_email2(request, token, uid):
    """Активация пользователя"""
    id = urlsafe_base64_decode(uid)
    try:
        user = CustomAbstractUser.objects.get(pk=id)
        if token == user.token:
            user.is_active = True
            user.save()
            login(request, user)
            return redirect("main")
    except CustomAbstractUser.DoesNotExist:
        return Http404("Такого пользователя не существует")
