from rest_framework.test import APITestCase
from django.urls import reverse
from uuid import uuid4
from django.contrib.auth import get_user_model
from mvp_api.models import Complaint, Comment
from .api_client import authorized_client


User = get_user_model()


class TestComments(APITestCase):
    """
    Test cases for the Comment model.
    """

    def setUp(self):
        """
        Set up the test case data.
        """
        self.client = authorized_client()
        user = User.objects.create_user(
            "testuser123", "testuser@test.com", "testpassword@123"
        )
        complaint = Complaint.objects.create(
            title="Test Complaint",
            user=user,
            description="This is a test complaint.",
            status="pending",
            longitude=0.0,
            latitude=0.0,
        )
        self.user_id = user.id
        self.complaint_id = complaint.id
        self.comment = "This is a test comment."

    def tearDown(self) -> None:
        """
        Clean up the test case data.
        """
        return super().tearDown()

    def test_create_comment_with_valid_data(self):
        """
        Test that a comment can be created with valid data.
        """
        data = {
            "user": self.user_id,
            "complaint": self.complaint_id,
            "comment": self.comment,
        }
        url = reverse("mvp_api:create-comment")
        response = self.client.post(
            url,
            data,
            format="json",
        )
        self.assertEqual(response.status_code, 201)

    def test_create_comment_with_invalid_user(self):
        """
        Test that a comment cannot be created with an invalid user.
        """
        data = {
            "user": uuid4(),
            "complaint": self.complaint_id,
            "comment": self.comment,
        }
        url = reverse("mvp_api:create-comment")
        response = self.client.post(
            url,
            data,
            format="json",
        )
        self.assertEqual(response.status_code, 400)

    def test_create_comment_with_invalid_complaint(self):
        """
        Test that a comment cannot be created with an invalid complaint.
        """
        data = {
            "user": self.user_id,
            "complaint": uuid4(),
            "comment": self.comment,
        }
        url = reverse("mvp_api:create-comment")
        response = self.client.post(
            url,
            data,
            format="json",
        )
        self.assertEqual(response.status_code, 400)

    def test_create_comment_with_invalid_comment(self):
        """
        Test that a comment cannot be created with an invalid comment.
        """
        data = {
            "user": self.user_id,
            "complaint": self.complaint_id,
            "comment": "",
        }
        url = reverse("mvp_api:create-comment")
        response = self.client.post(
            url,
            data,
            format="json",
        )
        self.assertEqual(response.status_code, 400)

    def test_get_comment_with_valid_id(self):
        """
        Test that a comment can be retrieved with a valid id.
        """
        comment = Comment.objects.create(
            user_id=self.user_id,
            complaint_id=self.complaint_id,
            comment=self.comment,
        )
        url = reverse("mvp_api:get-comment", kwargs={"id": comment.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_comment_with_invalid_id(self):
        """
        Test that a comment cannot be retrieved with an invalid id.
        """
        url = reverse("mvp_api:get-comment", kwargs={"id": uuid4()})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_update_comment_with_valid_id(self):
        """
        Test that a comment can be updated with a valid id.
        """
        comment = Comment.objects.create(
            user_id=self.user_id,
            complaint_id=self.complaint_id,
            comment=self.comment,
        )
        url = reverse("mvp_api:update-comment", kwargs={"id": comment.id})
        data = {
            "user": self.user_id,
            "complaint": self.complaint_id,
            "comment": "This is an updated comment.",
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, 200)

    def test_update_comment_with_invalid_id(self):
        """
        Test that a comment cannot be updated with an invalid id.
        """
        url = reverse("mvp_api:update-comment", kwargs={"id": uuid4()})
        data = {
            "user": self.user_id,
            "complaint": self.complaint_id,
            "comment": "This is an updated comment.",
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, 404)

    def test_delete_comment_with_valid_id(self):
        """
        Test that a comment can be deleted with a valid id.
        """
        comment = Comment.objects.create(
            user_id=self.user_id,
            complaint_id=self.complaint_id,
            comment=self.comment,
        )
        url = reverse("mvp_api:delete-comment", kwargs={"id": comment.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def test_delete_comment_with_invalid_id(self):
        """
        Test that a comment cannot be deleted with an invalid id.
        """
        url = reverse("mvp_api:delete-comment", kwargs={"id": uuid4()})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 404)
