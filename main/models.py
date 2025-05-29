from django.db import models
from RegAuth.models import CustomAbstractUser

class Feedback(models.Model):
    user = models.ForeignKey(CustomAbstractUser, related_name="user", on_delete=models.CASCADE)
    text = models.TextField()
    phone = models.CharField(max_length=12)

    class Meta:
        verbose_name="Отклик"
        verbose_name_plural="Отклики"

