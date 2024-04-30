from django.urls import path
from .views import OrderApiView, MyOrders


urlpatterns = [
    path('', OrderApiView.as_view()),
    path('my_orders/', MyOrders.as_view()),
]



