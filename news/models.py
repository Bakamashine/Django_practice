from typing import Any
from django.db import models


class News(models.Model):
    title = models.CharField(verbose_name="Внесите заголовок", max_length=20)
    text = models.TextField(verbose_name="Описание")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
