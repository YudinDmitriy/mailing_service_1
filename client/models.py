from django.db import models

from config import settings

NULLABLE = {"blank": True, "null": True}


class Client(models.Model):

    email = models.EmailField(verbose_name='Почта')
    client_name = models.CharField(max_length=150, verbose_name='ФИО клиента')
    comment = models.TextField(verbose_name='Комментарий')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f"{self.client_name} ({self.email})"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

