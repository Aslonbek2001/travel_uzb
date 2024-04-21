from django.urls import path
from .views import CafeListView, CafeDetailView

urlpatterns = [
    path('cafelar/', CafeListView.as_view(), name='cafes'),
    path('cafe/<int:pk>/', CafeDetailView.as_view(), name='cafes_detail'),  
]

