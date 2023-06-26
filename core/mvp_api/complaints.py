from .models import Complaint
from .serializer import (
    ComplaintSerializer,
    ComplaintGetSerializer,
    ComplaintGetAllSerializer,
    ComplaintUpdateSerializer,
    ComplaintDeleteSerializer,
)
from rest_framework.parsers import MultiPartParser
from rest_framework import generics


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