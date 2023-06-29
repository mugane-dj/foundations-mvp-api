from django.urls import reverse
from uuid import uuid4
from django.contrib.auth import get_user_model
from django.test.client import MULTIPART_CONTENT, encode_multipart, BOUNDARY
from rest_framework.test import APITestCase
from mvp_api.models import Complaint
from .api_client import authorized_client

User = get_user_model()


class TestComplaints(APITestCase):
    """
    Test cases for the Complaint model.
    """

    def setUp(self):
        """
        Set up the test case data.
        """
        self.client = authorized_client()
        user = User.objects.create_user(
            "testuser123", "testuser@test.com", "testpassword@123"
        )
        self.user_id = user.id
        self.title = "Test Complaint"
        self.description = "This is a test complaint."
        self.status = "pending"
        self.longitude = 0.0
        self.latitude = 0.0

    def tearDown(self) -> None:
        """
        Clean up the test case data.
        """
        return super().tearDown()

    def test_create_complaint_with_valid_data(self):
        """
        Test that a complaint can be created with valid data.
        """
        with open("media/complaints/test_complaint.jpg", "rb") as image:
            url = reverse("mvp_api:create-complaint")
            data = {
                "title": self.title,
                "user": self.user_id,
                "description": self.description,
                "status": self.status,
                "longitude": self.longitude,
                "latitude": self.latitude,
                "image": image,
            }
            response = self.client.post(
                path=url,
                data=encode_multipart(data=data, boundary=BOUNDARY),
                content_type=MULTIPART_CONTENT,
            )
            self.assertEqual(response.status_code, 201)

    def test_create_complaint_with_invalid_user(self):
        """
        Test that a complaint cannot be created with an invalid user.
        """
        with open("media/complaints/test_complaint.jpg", "rb") as image:
            url = reverse("mvp_api:create-complaint")
            data = {
                "title": self.title,
                "user": uuid4(),
                "description": self.description,
                "status": self.status,
                "longitude": self.longitude,
                "latitude": self.latitude,
                "image": image,
            }
            response = self.client.post(
                path=url,
                data=encode_multipart(data=data, boundary=BOUNDARY),
                content_type=MULTIPART_CONTENT,
            )
            self.assertEqual(response.status_code, 400)

    def test_create_complaint_with_invalid_image(self):
        """
        Test that a complaint cannot be created with an invalid image.
        """
        url = reverse("mvp_api:create-complaint")
        data = {
            "title": self.title,
            "user": self.user_id,
            "description": self.description,
            "status": self.status,
            "longitude": self.longitude,
            "latitude": self.latitude,
            "image": "invalid image",
        }
        response = self.client.post(
            path=url,
            data=encode_multipart(data=data, boundary=BOUNDARY),
            content_type=MULTIPART_CONTENT,
        )
        self.assertEqual(response.status_code, 400)

    def test_create_complaint_with_invalid_status(self):
        """
        Test that a complaint cannot be created with an invalid status.
        """
        with open("media/complaints/test_complaint.jpg", "rb") as image:
            url = reverse("mvp_api:create-complaint")
            data = {
                "title": self.title,
                "user": self.user_id,
                "description": self.description,
                "status": "invalid status",
                "longitude": self.longitude,
                "latitude": self.latitude,
                "image": image,
            }
            response = self.client.post(
                path=url,
                data=encode_multipart(data=data, boundary=BOUNDARY),
                content_type=MULTIPART_CONTENT,
            )
            self.assertEqual(response.status_code, 400)

    def test_get_complaint_with_valid_id(self):
        """
        Test that a complaint can be retrieved with a valid id.
        """
        complaint = Complaint.objects.create(
            title=self.title,
            user_id=self.user_id,
            description=self.description,
            status=self.status,
            longitude=self.longitude,
            latitude=self.latitude,
        )
        url = reverse("mvp_api:get-complaint", kwargs={"id": complaint.id})
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 200)

    def test_get_complaint_with_invalid_id(self):
        """
        Test that a complaint cannot be retrieved with an invalid id.
        """
        url = reverse("mvp_api:get-complaint", kwargs={"id": uuid4()})
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 404)

    def test_get_complaint_comments_with_valid_id(self):
        """
        Test that a complaint's comments can be retrieved with a valid id.
        """
        complaint = Complaint.objects.create(
            title=self.title,
            user_id=self.user_id,
            description=self.description,
            status=self.status,
            longitude=self.longitude,
            latitude=self.latitude,
        )
        url = reverse("mvp_api:get-complaint-comments", kwargs={"id": complaint.id})
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 200)

    def test_get_complaint_comments_with_invalid_id(self):
        """
        Test that a complaint's comments cannot be retrieved with an invalid id.
        """
        url = reverse("mvp_api:get-complaint-comments", kwargs={"id": uuid4()})
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 404)

    def test_update_complaint_with_valid_id(self):
        """
        Test that a complaint can be updated with a valid id.
        """
        complaint = Complaint.objects.create(
            title=self.title,
            user_id=self.user_id,
            description=self.description,
            status=self.status,
            longitude=self.longitude,
            latitude=self.latitude,
        )
        url = reverse("mvp_api:update-complaint", kwargs={"id": complaint.id})
        data = {
            "title": self.title,
            "user": self.user_id,
            "description": self.description,
            "status": "completed",
            "longitude": self.longitude,
            "latitude": self.latitude,
        }
        response = self.client.put(path=url, data=data, format="json")
        self.assertEqual(response.status_code, 200)

    def test_update_complaint_with_invalid_id(self):
        """
        Test that a complaint cannot be updated with an invalid id.
        """
        url = reverse("mvp_api:update-complaint", kwargs={"id": uuid4()})
        data = {
            "title": self.title,
            "user": self.user_id,
            "description": self.description,
            "status": "completed",
            "longitude": self.longitude,
            "latitude": self.latitude,
        }
        response = self.client.put(path=url, data=data)
        self.assertEqual(response.status_code, 404)

    def test_delete_complaint_with_valid_id(self):
        """
        Test that a complaint can be deleted with a valid id.
        """
        complaint = Complaint.objects.create(
            title=self.title,
            user_id=self.user_id,
            description=self.description,
            status=self.status,
            longitude=self.longitude,
            latitude=self.latitude,
        )
        url = reverse("mvp_api:delete-complaint", kwargs={"id": complaint.id})
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, 204)

    def test_delete_complaint_with_invalid_id(self):
        """
        Test that a complaint cannot be deleted with an invalid id.
        """
        url = reverse("mvp_api:delete-complaint", kwargs={"id": uuid4()})
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, 404)
