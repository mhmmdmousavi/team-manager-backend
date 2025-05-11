from rest_framework import serializers
from .models import Group

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'team', 'name', 'subject', 'allow_message_edit', 'allow_message_delete', 'created_at']
