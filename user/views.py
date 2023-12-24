from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from user.models import User
from user.serializers import UserSerializer


# Create your views here.


class UserRegisterView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()