from django.shortcuts import render
from .models import Cart
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status,permissions
from .serializers import CartSerializer
from users.models import CustomUser

class CartApiView(APIView):
    def get(self, request, user_id, format=None):
        user = CustomUser.objects.get(id=user_id)
        carts = Cart.objects.filter(user=user)
        serializer = CartSerializer(carts, many=True)
        data = {
            "count": carts.count(),
            "carts": serializer.data
        }
        return Response(data=data)
    
    def post(self, request, user_id,  format=None):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, format=None):
        cart = self.get_object()
        serializer = CartSerializer(cart, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

