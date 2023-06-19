from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializer import (
    UserSerializer,
    UserGetSerializer,
    UserGetAllSerializer,
    UserUpdateSerializer,
    UserDeleteSerializer,
)
from rest_framework.decorators import api_view


@api_view(["GET"])
def get_user(request):
    """Gets a user object based on userID."""
    serializer = UserGetSerializer(data=request.query_params)

    if serializer.is_valid(raise_exception=True):
        user_id = serializer.validated_data.get("id")
        user = User.objects.get(id=user_id)
        response = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
        }
        return Response(response, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_all_users(request):
    """Gets all user objects."""
    users = User.objects.all()
    return Response(
        UserGetAllSerializer(users, many=True).data, status=status.HTTP_200_OK
    )


@api_view(["POST"])
def create_user(request):
    """Creates a user object."""
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        user = User.objects.create_user(**serializer.validated_data)
        return Response({"id": user.id}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def update_user(request):
    serializer = UserUpdateSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        user_id = serializer.validated_data.get("id")
        user = User.objects.get(id=user_id)
        user.set_password(serializer.validated_data.get("password"))
        user.save()
        return Response({"id": user.id}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_user(request):
    serializer = UserDeleteSerializer(data=request.query_params)

    if serializer.is_valid(raise_exception=True):
        user_id = serializer.validated_data.get("id")
        user = User.objects.get(id=user_id)
        user.delete()
        return Response(status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
