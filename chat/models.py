from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
# chat/models.py

from django.db import models
from accounts.models import User
from groups.models import Group

def validate_file_size(file):
    max_size = 100 * 1024 * 1024  # 100MB
    if file.size > max_size:
        raise ValidationError("File size must be less than 100MB.")

class Message(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    is_edited = models.BooleanField(default=False)
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True, validators=[validate_file_size])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message by {self.sender.username} in {self.group.name}"

class PrivateMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_private_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_private_messages')
    content = models.TextField()
    is_edited = models.BooleanField(default=False)
    attachment = models.FileField(upload_to='private_attachments/', null=True, blank=True, validators=[validate_file_size])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Private message from {self.sender.username} to {self.receiver.username}"
