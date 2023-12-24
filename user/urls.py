from django.urls import path

from .apps import UserConfig
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

app_name = UserConfig.name

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
    ]
