from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomAbstractUser(AbstractUser):
    """
    Дочерний класс от AbstractUser
    Модель для регистрации или авторизации пользователей
    """

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[AbstractUser.username_validator],
        null=True,
        blank=True,
    )

    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A email with that username already exists."),
        },
    )

    is_active = models.BooleanField(
        _("non-active"),
        default=False,
        # help_text=_(
        #     "Designates whether this user should be treated as active. "
        #     "Unselect this instead of deleting accounts."
        # ),
    )

    token = models.CharField(max_length=255, unique=True, null=True)

    avatar = models.ImageField(
        upload_to="avatars",
        verbose_name="Загружаемый аватар",
        blank=True,
        null=True,
        default="avatars/default_avatar.png",
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

