from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from client.models import Client
from mailing.forms import MessageForm, SendingForm
from mailing.models import Sending, Message, Status


# ListView


class SendingListView(ListView):
    model = Sending


class MessageListView(ListView):
    model = Message


class StatusListView(ListView):
    model = Status


# DetailView


class SendingDetailView(DetailView):
    model = Sending

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        clients_detail = Client.objects.all()
        context_data['clients_all'] = clients_detail
        return context_data


class MessageDetailView(DetailView):
    model = Message


# CreateView


class SendingCreateView(CreateView):
    model = Sending
    form_class = SendingForm
    success_url = reverse_lazy("mailing:sending_list")


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailing:message_list")


# UpdateView


class SendingUpdateView(UpdateView):
    model = Sending
    form_class = SendingForm
    success_url = reverse_lazy("mailing:sending_list")


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailing:message_list")


# DeleteView


class SendingDeleteView(DeleteView):
    model = Sending
    success_url = reverse_lazy("mailing:sending_list")


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy("mailing:message_list")




