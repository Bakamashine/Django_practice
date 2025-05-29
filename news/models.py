from typing import Any
from django.db import models

class News(models.Model):
    title = models.CharField(help_text="Заголовок", verbose_name="Внесите заголовок", max_length=20)
    text = models.TextField(help_text="Основной текст", verbose_name="Описание")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
         

class Images(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="news/" ,help_text="Картинки", verbose_name="Загрузить картинки", blank=True)
    
    def __str__(self):
        return f"Картинка {self.image}"
    
    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"

    def delete(self, using: Any = ..., keep_parents = ...) -> tuple[int, dict[str, int]]:
        self.image.delete()
        return super().delete(using, keep_parents)