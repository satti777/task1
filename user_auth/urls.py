from django.urls import path, include
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("login/", LoginView.as_view(template_name='admin/login.html', )),
    path('signup/', Signup.as_view()),
    path('logout/', LogoutView.as_view()),
    path('UserCreate/', UserCreate.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
