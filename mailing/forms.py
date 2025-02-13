from django import forms

from config.forms import StyleFormMixin
from mailing.models import Sending, Message


class SendingForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Sending
        fields = ('title', 'time_first_mailing', 'periodicity', 'message', 'clients')


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('tem_message', 'message_body')
