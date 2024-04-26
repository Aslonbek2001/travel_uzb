from django.urls import path
from .views import QadamjoDetail, QadamjoList, AboutUsView

app_name = "main"

urlpatterns = [
    path("about/", AboutUsView.as_view(), name='about'),
    path("qadamjo/<int:pk>/", QadamjoDetail.as_view(), name='qadamjo'),
    path("qadamjolar/", QadamjoList.as_view(), name="qadamjolar"),
]