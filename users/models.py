from django.db import models
import os
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    manager = models.BooleanField(default=False, help_text="Choyxona egasi", blank=True, null=True)
    
    def __str__(self):
        return self.username

class ProFile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="profil", primary_key=True)
    image = models.ImageField(default=None, help_text="Profile image", upload_to="profile", blank=True, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
 
