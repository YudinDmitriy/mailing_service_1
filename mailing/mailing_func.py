import smtplib
from datetime import datetime, timedelta
import pytz
from django.core.mail import send_mail

from config import settings
from config.settings import EMAIL_HOST_USER
from mailing.models import Sending, Status, LOGS_STATUS_CHOICES


def mailing_func():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    mailings = Sending.objects.filter(time_first_mailing__lte=current_datetime).filter(
        sending_status__in=["created"]
    )

    for mailing in mailings:
        title = mailing.message.tem_message
        body = mailing.message.message_body
        mailing.sending_status = "started"
        mailing.save()

        try:
            service_response = send_mail(
                subject=title,
                message=body,
                from_email=EMAIL_HOST_USER,
                recipient_list=[client.email for client in mailing.clients.all()],
                fail_silently=False
            )
            if service_response == 1:
                Status.objects.create(status=LOGS_STATUS_CHOICES[0][1], service_response='Письмо отправлено успешно', sending=mailing)

            if mailing.periodicity == 'daily' and service_response == 1:
                mailing.time_first_mailing += timedelta(days=1)
                mailing.sending_status = "created"

            elif mailing.periodicity == 'weekly' and service_response == 1:
                mailing.time_first_mailing += timedelta(days=7)
                mailing.sending_status = "created"

            elif mailing.periodicity == 'monthly' and service_response == 1:
                mailing.time_first_mailing += timedelta(days=30)
                mailing.sending_status = "created"

            mailing.save()

        except smtplib.SMTPException as error:
            Status.objects.create(status=LOGS_STATUS_CHOICES[1][1], service_response=error,
                                  sending=mailing)
            mailing.sending_status = "created"

