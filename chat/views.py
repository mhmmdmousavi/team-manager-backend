from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Message, PrivateMessage
from .serializers import MessageSerializer, PrivateMessageSerializer

class MessageListView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

class PrivateMessageListView(generics.ListCreateAPIView):
    queryset = PrivateMessage.objects.all()
    serializer_class = PrivateMessageSerializer
    permission_classes = [permissions.IsAuthenticated]

class PrivateMessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PrivateMessage.objects.all()
    serializer_class = PrivateMessageSerializer
    permission_classes = [permissions.IsAuthenticated]
