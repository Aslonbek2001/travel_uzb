from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static


from rest_framework_simplejwt.views import TokenObtainPairView


schema_view = get_schema_view(
   openapi.Info(
      title="Project Api",
      default_version='v1',
      description="Test description",
      terms_of_service="arslon.com",
      contact=openapi.Contact(email="aslonbekrahimov.1583@gmail.com"),
      license=openapi.License(name="Demo License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
   path('api/customer/', include('users.urls')),
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('admin/', admin.site.urls),
   path('api/main/', include('main.urls')),
   
   path('api/cafe/', include('cafe.urls')),
   path('api/order/', include('order.urls')),
   path('accounts/', include('django.contrib.auth.urls')),


   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)