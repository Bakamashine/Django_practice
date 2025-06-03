from django.db import models
from products.validators import file_validator, VALID_EXTENS
from django.core.validators import FileExtensionValidator

class Category(models.Model):
    name = models.CharField(verbose_name="Название категории", max_length=30)
    description = models.CharField(verbose_name="Описание")
    img = models.ImageField(
        verbose_name="Изображение", upload_to="category/img"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    formats = ['stl', 'glb']
    title = models.CharField(
        help_text="Название модели", max_length=20, verbose_name="Заголовок"
    )
    description = models.TextField(
        help_text="Описание", verbose_name="Описание"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория"
    )
    img = models.ImageField(
        verbose_name="Фото товара", null=True, blank=True, upload_to="product/img"
    )
    file = models.FileField(
        help_text=f"Модель в 3Д в форматах {VALID_EXTENS} ",
        validators=[
            FileExtensionValidator(formats, f"Файл должен быть с расширением {formats}")
            ],
        upload_to="product/models",
        verbose_name="Выберите 3Д модель"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
