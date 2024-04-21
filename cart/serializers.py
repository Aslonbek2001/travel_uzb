from rest_framework import serializers
from .models import Cart
from users.models import CustomUser
from cafe.models import Foods
from order.models import Order, OrderItem


class CartSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(read_only=True)
    foods_id = serializers.IntegerField()
    quantity = serializers.IntegerField(default=1)


    def create(self, validated_data):
        user_id = validated_data.get('user_id')
        foods_id = validated_data.get('foods_id')
        quantity = validated_data.get('quantity')
        user = CustomUser.objects.get(id=user_id)
        foods = Foods.objects.get(id=foods_id)
        cart = Cart(user=user, foods=foods, quantity=quantity)
        cart.save()
        return cart
    
    def update(self, instance, validated_data):
        user_id = validated_data.get('user_id')
        foods_id = validated_data.get('foods_id')
        quantity = validated_data.get('quantity')
        user = CustomUser.objects.get(id=user_id)
        foods = Foods.objects.get(id=foods_id)
        instance.user = user
        instance.foods = foods
        instance.quantity = quantity
        instance.save()
        return instance




