from django.db import models

# Create your models here.
# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # اگر نیاز به فیلدهای اضافی داشتیم، اینجا اضافه می‌کنیم
    pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - Profile"
