from rest_framework import generics

from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerialiser

from rest_framework.permissions import IsAuthenticated


class OrderApiView(generics.CreateAPIView):
    queryset =  Order.objects.all()
    serializer_class = OrderSerialiser
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        try:
            queryset =  self.get_queryset()
            serializer =  OrderSerialiser(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({
                'status': False,
                "message":f"Xatolik {e} ",
            })
        
    

class MyOrders(generics.ListAPIView):
    queryset =  Order.objects.all()
    serializer_class = OrderSerialiser
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            user_id = request.user.id
            order =  self.queryset(user=user_id)
            serializer =  OrderSerialiser(order, many=True)

            return Response(serializer.data)
        except Exception:
            return Response(
               { "status": False,
                "message": "Ro'yxatdan o'tmagansiz 😔!!!"
                }
            )


    



  
        