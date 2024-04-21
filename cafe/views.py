from django.shortcuts import render
from .models import Cafe, CafeImages, Foods
from .serializers import CafeSerializer, CafeImagesSerializer, FoodsSerializer
from rest_framework.views import APIView
from rest_framework import generics
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status,permissions
# Create your views here.

class CafeListView(generics.ListAPIView):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer


class CafeDetailView(APIView):
    def get(self, request, *args, **kwargs):
        cafe = Cafe.objects.get(pk=kwargs['pk'])
        menu = Foods.objects.filter(cafe=cafe)
        cafe = CafeSerializer(cafe)
        menu = FoodsSerializer(menu)

        data = {
            "cafe": cafe.data,
            "menu": menu.data
        }

        return Response(data=data)


    # def get_object(self, pk):
    #     try:
    #         return Cafe.objects.get(pk=pk)
    #     except Cafe.DoesNotExist:
    #         raise Http404
        
    # def get(self, request, pk, format=None):
    #     cafe = self.get_object(pk)
    #     serializer = CafeSerializer(cafe)
    #     return Response(serializer.data)
    
    # def post(self, request, pk, format=None):
    
    
    
    


