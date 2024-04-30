from django.db import models
from cafe.models import Foods
from users.models import CustomUser

class Order(models.Model):
    user = models.ForeignKey(CustomUser, null=True, blank=True,on_delete=models.CASCADE, related_name='orders')
    foods = models.ManyToManyField(Foods, null=True, blank=True, related_name='orders')
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=20, verbose_name="Tel numer")
    status = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.name} -> Order"


# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.CASCADE, related_name='items')
#     food = models.ForeignKey(Foods, null=True, on_delete=models.CASCADE, blank=True)
#     quantity = models.PositiveIntegerField(default=1)

    # def __str__(self):
    #     return f"{self.order.user.name} -> {self.food.name}"
    
    


