from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from cart.models import Cart
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from cart.serializers import CartSerializer
from users.models import CustomUser
from order.models import Order, OrderItem
from .serializers import CustomUserSerializer

# class UserInfo(APIView):
#     def get(self, request, id, format=None):
#         user = CustomUser.objects.get(id=id)
#         carts = Cart.objects.filter(user=user)
#         carts = CartSerializer(carts)
#         cardcount = carts.count()
#         orders = Order.objects.filter(user=user)

#         data = {
#             "user": user,
#             "card_count": cardcount,
#             "cart": carts,
#             "orders": orders,
#         }

#         return Response(data=data)
    

class UserInfo(generics.ListAPIView):
        queryset = CustomUser.objects.all()
        serializer_class = CustomUserSerializer


    # def get(self, request, format=None):
    #     user = CustomUser.objects.all()
    #     user = CustomUserSerializer(user, many=True)
        # carts = Cart.objects.filter(user=user)
        # carts = CartSerializer(carts)
        # cardcount = carts.count()
        # orders = Order.objects.filter(user=user)



        # data = {
        #     "user": user,
        #     # "card_count": cardcount,
        #     # "cart": carts,
        #     # "orders": orders,
        # }

        # return Response(data=data)