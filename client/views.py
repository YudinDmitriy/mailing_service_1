from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from client.forms import ClientForm
from client.models import Client


# Create your views here.
class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("client:client_list")

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.creator = self.request.user
            self.object.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("client:client_list")


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy("client:client_list")