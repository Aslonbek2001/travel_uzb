from django.contrib.auth.models import AbstractUser
from django.db import models







########################   CUSTOMERS ##############################
class CustomUser(AbstractUser):
    USER_ROLE = (
        ('mijoz', 'Mijoz'),
        ('xodim', 'Xodim'),
    )
    

    phone = models.CharField(max_length=15)
    user_role = models.CharField(max_length=20, choices=USER_ROLE)
    create_at = models.DateTimeField(auto_now_add=True)

 

    def __str__(self):
        return self.username

