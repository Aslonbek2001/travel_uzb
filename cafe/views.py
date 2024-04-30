from django.shortcuts import render
from .models import Cafe, CafeImages, Foods
from .serializers import CafeSerializer, CafeImagesSerializer, FoodsSerializer
from rest_framework.views import APIView
from rest_framework import generics
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status,permissions
# Create your views here.


class CafeListApiView(APIView):
    def get(self, request, format=None):
        cafes = Cafe.objects.all()
        serializer = CafeSerializer(cafes, many=True)
        return Response(serializer.data)


# class CafeDetailView(APIView):
#     def get(self, request, pk):
#         cafe = Cafe.objects.get(id=pk)
#         images = CafeImages.objects.filter(cafe=cafe)
#         menu = Foods.objects.filter(cafe=cafe)

#         cafe = CafeSerializer(cafe)
#         images = CafeImagesSerializer(images)
#         menu = FoodsSerializer(menu)

#         data = {
#             "cafe": cafe.data,
#             'images': images.data,
#             "menu": menu.data,
#         }

#         return Response(data=data)

class CafeDetailView(APIView):
    def get(self, request, pk):
        cafe = Cafe.objects.get(id=pk)
        images = CafeImages.objects.filter(chayxana_id=pk)  # Use the correct field name
        menu = Foods.objects.filter(cafe=cafe)

        cafe_serializer = CafeSerializer(cafe)
        images_serializer = CafeImagesSerializer(images, many=True)  # Assuming multiple images
        menu_serializer = FoodsSerializer(menu, many=True)

        data = {
            "cafe": cafe_serializer.data,
            "images": images_serializer.data,
            "menu": menu_serializer.data,
        }

        return Response(data=data)

    
    
    
    


