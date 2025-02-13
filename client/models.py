from django.db import models


class Client(models.Model):

    email = models.EmailField(unique=True, verbose_name='Почта')
    client_name = models.CharField(max_length=150, verbose_name='ФИО клиента')
    comment = models.TextField(verbose_name='Комментарий')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

