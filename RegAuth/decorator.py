from django.shortcuts import redirect
from functools import wraps
from django.conf import settings



# Перенаправление на главную страницу если пользователь авторизирован
# Только для функций-контроллеров
def anon_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if (request.user.is_authenticated):
            return redirect(settings.LOGIN_REDIRECT_URL)
        return view_func(request, *args, **kwargs)
    return wrapper
