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
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = CommentGetSerializer
    lookup_field = "id"
    queryset = Comment.objects.all()


class ListCommentView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    queryset = Comment.objects.all()
    serializer_class = CommentGetAllSerializer


class CreateCommentView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = CommentSerializer


class UpdateCommentView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = CommentUpdateSerializer
    lookup_field = "id"
    queryset = Comment.objects.all()


class DestroyCommentView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = CommentDeleteSerializer
    lookup_field = "id"
    queryset = Comment.objects.all()
