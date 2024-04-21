from django.db import models
from users.models import CustomUser
from cafe.models import Foods

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="carts")
    foods = models.ForeignKey(Foods, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    session_key = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.foods.name
    




