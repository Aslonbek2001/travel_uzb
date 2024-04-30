from rest_framework.serializers import ModelSerializer
from .models import Order


class OrderSerialiser(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

   

