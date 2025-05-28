from django.db import models
from products.validators import file_validator

class Product(models.Model):
    title = models.CharField(help_text="Название модели", max_length=20, verbose_name="Внесите заголовок")
    description = models.TextField(help_text="Описание", verbose_name="Напишите описание")
    file = models.FileField(help_text="Модель в 3Д", validators=[file_validator], upload_to="product/models")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "продукты"
    