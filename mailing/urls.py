from django.urls import path

from mailing.views import SendingListView, SendingCreateView, SendingDetailView, SendingUpdateView, SendingDeleteView, \
    MessageListView, \
    MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView, StatusListView

app_name = 'mailing'


urlpatterns = [
    path('', SendingListView.as_view(), name='sending_list'),
    path('create_sending/', SendingCreateView.as_view(), name='sending_create'),
    path('sending/<int:pk>', SendingDetailView.as_view(), name='sending_detail'),
    path('update_sending/<int:pk>', SendingUpdateView.as_view(), name='sending_update'),
    path('delete_sending/<int:pk>', SendingDeleteView.as_view(), name='sending_delete'),

    path('message_list/', MessageListView.as_view(), name='message_list'),
    path('message/<int:pk>', MessageDetailView.as_view(), name='message_detail'),
    path('create_message/', MessageCreateView.as_view(), name='message_create'),
    path('update_message/<int:pk>', MessageUpdateView.as_view(), name='message_update'),
    path('delete_message/<int:pk>', MessageDeleteView.as_view(), name='message_delete'),

    path('status_list/', StatusListView.as_view(), name='status_list'),

]


