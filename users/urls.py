from django.urls import path
from .views import UserInfo
# from .views import login, registration, profile, logout

app_name = "users"

urlpatterns = [
    path("users/",UserInfo.as_view(), name="users")
    # path('', registration, name='registration'),
    # path('login/', login, name='login'),
    # path('logout/', logout, name='logout'),
    # path('profile/', profile, name='profile'),

]