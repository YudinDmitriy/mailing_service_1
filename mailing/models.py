from django.db import models

from client.models import Client

NULLABLE = {"blank": True, "null": True}
PERIODICITY_CHOICES = [
    ("daily", "Раз в день"),
    ("weekly", "Раз в неделю"),
    ("monthly", "Раз в месяц"),
]
SENDING_STATUS_CHOICES = [
    ("created", "Создана"),
    ("started", "Запущена"),
    ("completed", "Завершена"),
]
LOGS_STATUS_CHOICES = [("success", "успешно"), ("fail", "неуспешно")]


class Message(models.Model):

    tem_message = models.CharField(max_length=100, verbose_name="Тема письма")
    message_body = models.TextField(verbose_name="Тело письма")

    def __str__(self):
        return f"{self.tem_message}"

    class Meta:
        verbose_name = "Письмо"
        verbose_name_plural = "Письма"


class Sending(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название рассылки")
    time_first_mailing = models.DateTimeField(verbose_name="Начало рассылки")
    periodicity = models.CharField(max_length=50, choices=PERIODICITY_CHOICES, verbose_name="Периодичность рассылки")
    sending_status = models.CharField(
        max_length=50,
        choices=SENDING_STATUS_CHOICES,
        verbose_name="Статус рассылки",
        default="created"
    )
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE, verbose_name="Сообщение"
    )
    clients = models.ManyToManyField(Client, verbose_name="Клиенты")

    def __str__(self):
        return f"{self.title}({self.message})"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"


class Status(models.Model):
    time = models.DateTimeField(auto_now_add=True, verbose_name="Дата рассылки")
    status = models.CharField(max_length=50, verbose_name="Статус рассылки")
    service_response = models.TextField(verbose_name="Ответ почты")
    sending = models.ForeignKey(
        Sending, on_delete=models.CASCADE, verbose_name="Рассылка"
    )

    def __str__(self):
        return f"{self.time}, {self.sending} отправлялась {self.status}, ответ сервиса: {self.service_response}"

    class Meta:
        verbose_name = "Статус отправки"
        verbose_name_plural = "Статусы отправки"
