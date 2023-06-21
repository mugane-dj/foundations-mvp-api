from django.contrib.auth.models import User
from .serializer import (
    UserSerializer,
    UserGetSerializer,
    UserGetAllSerializer,
    UserUpdateSerializer,
    UserDeleteSerializer,
)
from rest_framework import generics


class GetUserView(generics.RetrieveAPIView):
    serializer_class = UserGetSerializer
    lookup_field = "id"
    queryset = User.objects.all()


class ListUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserGetAllSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UpdateUserView(generics.UpdateAPIView):
    serializer_class = UserUpdateSerializer
    lookup_field = "id"
    queryset = User.objects.all()


class DestroyUserView(generics.DestroyAPIView):
    serializer_class = UserDeleteSerializer
    lookup_field = "id"
    queryset = User.objects.all()
