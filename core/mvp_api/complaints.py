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
    """
    Retrieves a complaint object based on its ID.
    """

    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = ComplaintGetSerializer
    lookup_field = "id"
    queryset = Complaint.objects.all()


class ListComplaintView(generics.ListAPIView):
    """
    Retrieves a list of all complaints.
    """

    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    queryset = Complaint.objects.all()
    serializer_class = ComplaintGetAllSerializer


class CreateComplaintView(generics.CreateAPIView):
    """
    Creates a new complaint object.
    """

    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = ComplaintSerializer
    parser_classes = [MultiPartParser]


class UpdateComplaintView(generics.UpdateAPIView):
    """
    Updates a complaint object based on its ID.
    """

    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = ComplaintUpdateSerializer
    lookup_field = "id"
    queryset = Complaint.objects.all()


class DestroyComplaintView(generics.DestroyAPIView):
    """
    Deletes a complaint object based on its ID.
    """

    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = ComplaintDeleteSerializer
    lookup_field = "id"
    queryset = Complaint.objects.all()


@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@api_view(["GET"])
def get_complaint_comments(request, id):
    """
    The function retrieves all comments associated with a specific complaint.

    :param request: The `request` parameter is an object that represents the HTTP request made by the
    client. It contains information such as the request method, headers, and body
    :param id: The "id" parameter is the unique identifier of the complaint for which you want to
    retrieve the comments
    :return: a Response object. If the complaint with the given id exists, it will return a Response
    object with the serialized data of all the comments related to that complaint. If the complaint does
    not exist, it will return a Response object with a status code of 404 (Not Found).
    """
    try:
        complaint = Complaint.objects.get(id=id)
        comments = Comment.objects.filter(complaint=complaint.id)
        serializer = CommentGetAllSerializer(comments, many=True)
        return Response(serializer.data)
    except Complaint.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
