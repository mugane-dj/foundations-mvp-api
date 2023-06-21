from rest_framework import generics
from .serializer import (
    UserSerializer,
    UserGetSerializer,
    UserGetAllSerializer,
    UserUpdateSerializer,
    UserDeleteSerializer,
)
from .models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(["POST"])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        User.objects.create_user(**serializer.validated_data)
        return Response(
            {"message": "User create successfully"}, status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def update_user(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(
            {"message": "User does not exist."}, status=status.HTTP_404_NOT_FOUND
        )
    serializer = UserUpdateSerializer(user, data=request.data)
    if serializer.is_valid():
        user.set_password(serializer.validated_data["password"])
        user.save()
        return Response(
            {"message": "User updated successfully"}, status=status.HTTP_200_OK
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
