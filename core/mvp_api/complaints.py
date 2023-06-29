from .models import Complaint, Comment
from .serializer import (
    ComplaintSerializer,
    ComplaintGetSerializer,
    ComplaintGetAllSerializer,
    ComplaintUpdateSerializer,
    ComplaintDeleteSerializer,
    CommentGetAllSerializer,
)
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


class GetComplaintView(generics.RetrieveAPIView):
    serializer_class = ComplaintGetSerializer
    lookup_field = "id"
    queryset = Complaint.objects.all()


class ListComplaintView(generics.ListAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintGetAllSerializer


class CreateComplaintView(generics.CreateAPIView):
    serializer_class = ComplaintSerializer
    parser_classes = [MultiPartParser]


class UpdateComplaintView(generics.UpdateAPIView):
    serializer_class = ComplaintUpdateSerializer
    lookup_field = "id"
    queryset = Complaint.objects.all()


class DestroyComplaintView(generics.DestroyAPIView):
    serializer_class = ComplaintDeleteSerializer
    lookup_field = "id"
    queryset = Complaint.objects.all()


@api_view(["GET"])
def get_complaint_comments(request, id):
    try:
        complaint = Complaint.objects.get(id=id)
        comments = Comment.objects.filter(complaint=complaint.id)
        serializer = CommentGetAllSerializer(comments, many=True)
        return Response(serializer.data)
    except Complaint.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
