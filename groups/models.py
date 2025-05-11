from django.db import models

# Create your models here.
# groups/models.py

from django.db import models
from teams.models import Team

class Group(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='groups')
    name = models.CharField(max_length=255)
    subject = models.TextField()
    allow_message_edit = models.BooleanField(default=True)
    allow_message_delete = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.team.name})"
