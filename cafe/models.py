from django.db import models
from users.models import CustomUser
import os

"""Choyxona  ma'lumotlari Funksiyalar
    Registration
    Login Logout
    orders
    Open Close
    Edit menu   
"""

DRINK, FOOD, DESSERT = ('drink', 'food', 'dessert')
START, PROCESS, DONE = ('start', 'process', 'done')


"""Qisqa text qo'shaman choyxona va qadamjoga"""
class Cafe(models.Model):
    user = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.CASCADE, related_name="chayxana")
    name = models.CharField(max_length=100, db_index=True, default="Nomi", blank=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    info = models.TextField(blank=True, null=True, help_text="Umumiy ma'lumotlar kiritish kerak")
    image = models.ImageField(default=None, help_text="Choyxona rasimi", upload_to="restaurant", blank=True, null=True)
    status = models.BooleanField(default=False)
    phone = models.CharField(max_length=9, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Cafelar"
        verbose_name = "Cafe"

    def __str__(self):
        return self.name
    



# """ Chayxana Images """
    
class CafeImages(models.Model):
    chayxana = models.ForeignKey(Cafe, blank=True, null=True, on_delete=models.CASCADE, related_name="fotos")
    image = models.ImageField(default=None, help_text="Choyxona rasimi", upload_to="chayxana_images", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Chayxana rasmlari"
        verbose_name = "Chayxana rasmi"

    def __str__(self):
        return self.chayxana.name
    

""" Menu Details """
class Foods(models.Model):

    TYPE_CHOICES = (
        (DRINK, DRINK),
        (FOOD, FOOD),
        (DESSERT, DESSERT),
    )

    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, null=True, help_text="choyxona", related_name="foods")
    name = models.CharField(max_length=100, db_index=True, default="Nomi", blank=True)
    price = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, default=FOOD)
    image = models.ImageField(default=None, help_text="menu", upload_to="menu_item", blank=True, null=True)
    description = models.TextField(blank=True, null=True, help_text="Umumiy ma'lumotlar")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Chayxona minulari"
        verbose_name = "Chayxana minusi"
        ordering = ["id"]

    def __str__(self):
        return f"{self.name} -> {self.cafe.name}"