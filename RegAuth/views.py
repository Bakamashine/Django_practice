"""Контроллеры свзяанные с регистрацией или авторизацией"""

from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.http import Http404
from django.shortcuts import redirect, render
from django.shortcuts import resolve_url
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.views.generic.edit import CreateView
from rest_framework import generics, response, status, permissions

from RegAuth.decorator import anon_required
from RegAuth.serializers import CustomAbstractUserSerializer
from .forms import RegisterForm, LoginForm
from .models import CustomAbstractUser


# from django.contrib.sites.models import Site

# class SendEmail:
#     """Отправка письма на почту"""
#
#     def __init__(self, user: CustomAbstractUser):
#         self.user = user
#         self.token = default_token_generator.make_token(user)
#         self.uid = urlsafe_base64_encode(str(self.user.pk).encode())
#
#     def send_active_email(self):
#         #        domain = Site.objects.get_current().domain
#         domain = settings.BASE_URL
#         # url = "https://%s%s" % (Site.objects.get_current().domain, f"/accept/{self.token}/{self.uid}")
#         token_url = f"accept/{self.token}/{self.uid}"
#         url = f"http://{domain}/{token_url} "
#         send_mail(
#             f"Уважаемый {self.user.username}!",
#             "",
#             settings.EMAIL_HOST_USER,
#             [self.user.email],
#             html_message=render_to_string(
#                 "RegAuth/message.html",
#                 {
#                     # "user": self.user.username,
#                     # "token": self.token,
#                     # "uid": self.uid,
#                     "url": url
#                 },
#             ),
#         )


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
        login(self.request, user)
        return redirect("main")

        # try:
        #     user.token = default_token_generator.make_token(user)
        #     user.save()
        #     mail = SendEmail(user=user)
        #     mail.send_active_email()
        #     return redirect("acceptEmail")
        # except SMTPDataError:
        #     user.delete()
        #     form.add_error("email", "Такой почты не существует")
        #     return self.form_invalid(form)
        # except:
        #     user.delete()
        #     form.add_error("email", "Ошибка с отправкой письма")
        # return self.form_invalid(form)


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


class RegisterUserApi(generics.CreateAPIView):
    serializer_class = CustomAbstractUserSerializer

    def post(self, request, *args, **kwargs):
        user = self.serializer_class(data=request.data)
        if user.is_valid():
            user.save()

            userRetrieved = CustomAbstractUser.objects.get(username=user.data["username"])
            rawUserPassword = user.data["password"]
            userRetrieved.set_password(rawUserPassword)
            userRetrieved.save();
            return response.Response(status=status.HTTP_201_CREATED)
        else:
            return super().post(request, *args, **kwargs)


class GetUserApi(generics.ListAPIView):
    # queryset  = 
    # serializer_class = CustomAbstractUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user;
        return response.Response({
            "username": user.username,
            "email": user.email
        }, status=status.HTTP_200_OK)
