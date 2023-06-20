from rest_framework import status
from rest_framework.response import Response
from .models import Complaint
from .serializer import (
    ComplaintSerializer,
    ComplaintGetSerializer,
    ComplaintGetAllSerializer,
    ComplaintUpdateSerializer,
    ComplaintDeleteSerializer,
)
from rest_framework.decorators import api_view


@api_view(["GET"])
def get_complaint(request):
    """Gets a complaint object based on complaintID."""
    serializer = ComplaintGetSerializer(data=request.query_params)

    if serializer.is_valid(raise_exception=True):
        complaint_id = serializer.validated_data.get("id")
        complaint = Complaint.objects.get(id=complaint_id)
        response = {
            "id": complaint.id,
            "title": complaint.title,
            "user_id": complaint.user_id,
            "description": complaint.description,
            "status": complaint.status,
            "longitude": complaint.longitude,
            "latitude": complaint.latitude,
            "created_at": complaint.created_at,
            "updated_at": complaint.updated_at,
        }
        return Response(response, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_all_complaints(request):
    """Gets all complaint objects."""
    complaints = Complaint.objects.all()
    return Response(
        ComplaintGetAllSerializer(complaints, many=True).data, status=status.HTTP_200_OK
    )


@api_view(["POST"])
def create_complaint(request):
    """Creates a complaint object."""
    serializer = ComplaintSerializer(data=request.data)
    user_id = request.user.id
    if serializer.is_valid(raise_exception=True):
        data = {
            "title": serializer.validated_data.get("title"),
            "user_id": user_id,
            "description": serializer.validated_data.get("description"),
            "status": serializer.validated_data.get("status"),
            "longitude": serializer.validated_data.get("longitude"),
            "latitude": serializer.validated_data.get("latitude"),
            "image": serializer.validated_data.get("image"),
        }
        complaint = Complaint.objects.create(**data)
        return Response({"id": complaint.id}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def update_complaint(request):
    serializer = ComplaintUpdateSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        complaint_id = serializer.validated_data.get("id")
        complaint = Complaint.objects.get(id=complaint_id)
        status = serializer.validated_data.get("status")
        complaint.status = status
        complaint.save()
        return Response({"id": complaint.id}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_complaint(request):
    serializer = ComplaintDeleteSerializer(data=request.query_params)

    if serializer.is_valid(raise_exception=True):
        complaint_id = serializer.validated_data.get("id")
        complaint = Complaint.objects.get(id=complaint_id)
        complaint.delete()
        return Response(status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
