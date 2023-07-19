from .models import Comment
from .serializer import (
    CommentSerializer,
    CommentGetSerializer,
    CommentGetAllSerializer,
    CommentUpdateSerializer,
    CommentDeleteSerializer,
)
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication


class GetCommentView(generics.RetrieveAPIView):
    """
    Retrieves a comment object based on its ID.
    """

    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = CommentGetSerializer
    lookup_field = "id"
    queryset = Comment.objects.all()


class ListCommentView(generics.ListAPIView):
    """
    Retrieves a list of all comments.
    """

    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    queryset = Comment.objects.all()
    serializer_class = CommentGetAllSerializer


class CreateCommentView(generics.CreateAPIView):
    """
    Creates a new comment object.
    """

    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = CommentSerializer


class UpdateCommentView(generics.UpdateAPIView):
    """
    Updates a comment object based on its ID.
    """

    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = CommentUpdateSerializer
    lookup_field = "id"
    queryset = Comment.objects.all()


class DestroyCommentView(generics.DestroyAPIView):
    """
    Deletes a comment object based on its ID.
    """

    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = CommentDeleteSerializer
    lookup_field = "id"
    queryset = Comment.objects.all()
