from rest_framework import generics
from .serializer import (
    UserSerializer,
    UserGetSerializer,
    UserGetAllSerializer,
    UserUpdateSerializer,
    UserDeleteSerializer,
    ComplaintGetAllSerializer,
)
from .models import User, Complaint
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(["POST"])
def create_user(request):
    """
    Create a new user.

    Parameters:
    - request: The HTTP request object containing user data.

    Returns:
    - Response: The HTTP response object indicating the success or
                failure of the user creation.

    """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        User.objects.create_user(**serializer.validated_data)
        return Response(
            {"message": "User created successfully"}, status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def update_user(request, id):
    """
    Update a user's password.

    Parameters:
    - request: The HTTP request object containing user data.
    - id: The ID of the user to update.

    Returns:
    - Response: The HTTP response object indicating the success or
                failure of the user update.
    """
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


@api_view(["GET"])
def get_user_token(request, id):
    """
    Retrieve a user's token.

    Parameters:
    - request: The HTTP request object containing user data.
    - id: The ID of the user to retrieve.

    Returns:
    - Response: The HTTP response object containing the user's token.

    """
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(
            {"message": "User does not exist."}, status=status.HTTP_404_NOT_FOUND
        )
    return Response({"tokens": user.token}, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_user_complaints(request, id):
    """
    Retrieve a user's complaints.
    """
    try:
        user = User.objects.get(id=id)
        complaints = Complaint.objects.filter(user=user.id)
        serializer = ComplaintGetAllSerializer(complaints, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response(
            {"message": "User does not exist."}, status=status.HTTP_404_NOT_FOUND
        )


@api_view(["GET"])
def get_user(request, id):
    """
    Retrieve a user's information.

    Parameters:
    - request: The HTTP request object containing user data.
    - id: The ID of the user to retrieve.

    Returns:
    - Response: The HTTP response object containing the user's information.

    """
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(
            {"message": "User does not exist."}, status=status.HTTP_404_NOT_FOUND
        )
    serializer = UserGetSerializer(user, many=False)
    response = {
        "id": serializer.data.get("id"),
        "username": serializer.data.get("username"),
    }
    return Response(response, status=status.HTTP_200_OK)


class ListUserView(generics.ListAPIView):
    """
    List all users.

    Parameters:
    - request: The HTTP request object containing user data.

    Returns:
    - Response: The HTTP response object containing the list of users.

    """

    queryset = User.objects.all()
    serializer_class = UserGetAllSerializer


class DestroyUserView(generics.DestroyAPIView):
    """
    Delete a User instance.

    Parameters:
    - request: The HTTP request object containing user data.
    - id: The ID of the user to delete.

    Returns:
    - Response: The HTTP response object indicating the success or
                failure of the user deletion.

    """

    serializer_class = UserDeleteSerializer
    lookup_field = "id"
    queryset = User.objects.all()
