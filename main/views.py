from .models import *
from .serializers import *
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


class QadamjoList(APIView):
    def get(self, request, format=None):
        qadajolar = Qadamjo.objects.all()
        serializer = QadamjoSeralizer(qadajolar, many=True)
        data = {
            "count": qadajolar.count(),
            "qadajolar": serializer.data
        }
        return Response(data=data)


class QadamjoDetail(APIView):
    def get_object(self, pk):
        try:
            return Qadamjo.objects.get(pk=pk)
        except Qadamjo.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        qadamjo = self.get_object(pk)
        serializer = QadamjoSeralizer(qadamjo).data
        images = FotoPlus.objects.filter(pleace=qadamjo).all()
        imageSerialiser = QadamjoFotoSerial(images).data
        data = {
            "qadamjo": serializer,
            "images": imageSerialiser,
        }

        return Response(data=data)

    # def put(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = QadamjoSeralizer(snippet, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     snippet.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)



class AboutUsView(APIView):
    # queryset = AboutUs.objects.all()
    # serializer_class = AboutUsSeralizer

    def get(self, request, format=None):
        about_us = AboutUs.objects.all()
        about_serializer = AboutUsSeralizer(about_us, many=True)
        about_img = AboutImages.objects.all()
        about_img_serializer = AboutImagesSeralizer(about_img, many=True)
        data = {
            "about": about_serializer.data,
            "image": about_img_serializer.data,
        }
        return Response(data=data)
    
