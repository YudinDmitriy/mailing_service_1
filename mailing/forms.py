from django import forms

from client.models import Client
from config.forms import StyleFormMixin
from mailing.models import Sending, Message


class SendingForm(StyleFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        self.fields['message'].queryset = Message.objects.filter(
            creator=self.request.user)
        self.fields['clients'].queryset = Client.objects.filter(
            creator=self.request.user)

    class Meta:
        model = Sending
        fields = ('title', 'time_first_mailing', 'periodicity', 'message', 'clients')


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('tem_message', 'message_body')
