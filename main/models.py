from django.db import models
from RegAuth.models import CustomAbstractUser
from django.core.validators import FileExtensionValidator
from datetime import datetime


class Feedback(models.Model):
    user = models.ForeignKey(
        CustomAbstractUser,
        related_name="user",
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )
    text = models.TextField(verbose_name="Ответ")
    phone = models.CharField(max_length=12, verbose_name="Номер телефона")
    date = models.DateField(auto_created=True, auto_now=True, verbose_name="Дата")

    @staticmethod
    def DataString() -> str:
        # return datetime.strftime(date, "%d/%m/%Y, %H:%M:%S")
        return "%d/%m/%Y, %H:%M:%S"

    class Meta:
        verbose_name = "Отклик"
        verbose_name_plural = "Отклики"


class Forms(models.Model):
    formats = ["docx", "doc", "xml", "xslx", "pdf"]
    title = models.CharField(verbose_name="Название файла")
    text = models.TextField(verbose_name="Описание", max_length=200)
    file = models.FileField(
        verbose_name="Документ",
        upload_to="forms/",
        help_text=f"Файлы должны быть в форматах {formats}",
        validators=[
            FileExtensionValidator(formats, f"Файл должен быть с расширением {formats}")
        ],
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Бланк заказа"
        verbose_name_plural = "Бланки заказов"
