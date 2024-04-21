from rest_framework.serializers import ModelSerializer
from .models import Order, OrderItem


class OrderSerialiser(ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "user", "total_price", "order_time", "order_status")

        read_only_fields = ["id"]


class OrderItemSerialiser(ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ("id", "order", "food", "quantity", "price")
