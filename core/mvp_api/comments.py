from .models import Comment
from .serializer import (
    CommentSerializer,
    CommentGetSerializer,
    CommentGetAllSerializer,
    CommentUpdateSerializer,
    CommentDeleteSerializer,
)
from rest_framework import generics


class GetCommentView(generics.RetrieveAPIView):
    serializer_class = CommentGetSerializer
    lookup_field = "id"
    queryset = Comment.objects.all()


class ListCommentView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentGetAllSerializer


class CreateCommentView(generics.CreateAPIView):
    serializer_class = CommentSerializer


class UpdateCommentView(generics.UpdateAPIView):
    serializer_class = CommentUpdateSerializer
    lookup_field = "id"
    queryset = Comment.objects.all()


class DestroyCommentView(generics.DestroyAPIView):
    serializer_class = CommentDeleteSerializer
    lookup_field = "id"
    queryset = Comment.objects.all()
