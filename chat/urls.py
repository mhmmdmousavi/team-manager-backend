from django.urls import path
from .views import MessageListView, MessageDetailView, PrivateMessageListView, PrivateMessageDetailView

urlpatterns = [
    path('messages/', MessageListView.as_view(), name='message-list'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),
    path('private-messages/', PrivateMessageListView.as_view(), name='private-message-list'),
    path('private-messages/<int:pk>/', PrivateMessageDetailView.as_view(), name='private-message-detail'),
]
