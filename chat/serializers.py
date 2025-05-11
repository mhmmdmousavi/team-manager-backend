from rest_framework import serializers
from .models import Message, PrivateMessage

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'group', 'sender', 'content', 'is_edited', 'attachment', 'created_at']

class PrivateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateMessage
        fields = ['id', 'sender', 'receiver', 'content', 'is_edited', 'attachment', 'created_at']
