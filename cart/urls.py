from django.urls import path
from .views import CartApiView

urlpatterns = [
    path('cart/<int:user_id>/', CartApiView.as_view(), name='cart'),
]
