from django.urls import path
from .views import CafeListApiView, CafeDetailView

urlpatterns = [
    path('cafelar/', CafeListApiView.as_view(), name='cafes'),
    path('cafe/<int:pk>/', CafeDetailView.as_view(), name='cafes_detail'),  
]

