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
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


class GetComplaintView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = ComplaintGetSerializer
    lookup_field = "id"
    queryset = Complaint.objects.all()


class ListComplaintView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    queryset = Complaint.objects.all()
    serializer_class = ComplaintGetAllSerializer


class CreateComplaintView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = ComplaintSerializer
    parser_classes = [MultiPartParser]


class UpdateComplaintView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = ComplaintUpdateSerializer
    lookup_field = "id"
    queryset = Complaint.objects.all()


class DestroyComplaintView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = ComplaintDeleteSerializer
    lookup_field = "id"
    queryset = Complaint.objects.all()


@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@api_view(["GET"])
def get_complaint_comments(request, id):
    try:
        complaint = Complaint.objects.get(id=id)
        comments = Comment.objects.filter(complaint=complaint.id)
        serializer = CommentGetAllSerializer(comments, many=True)
        return Response(serializer.data)
    except Complaint.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
