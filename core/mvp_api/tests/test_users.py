from rest_framework.test import APITestCase
from django.urls import reverse
from uuid import uuid4
from django.contrib.auth import get_user_model

User = get_user_model()


class TestUsers(APITestCase):
    """
    Test cases for the User model.
    """

    def setUp(self):
        """
        Set up the test case data.
        """
        self.username = "testuser123"
        self.email = "testuser@test.com"
        self.password = "testpassword@123"

    def tearDown(self) -> None:
        """
        Clean up the test case data.
        """
        return super().tearDown()

    def test_create_user_with_valid_data(self):
        """
        Test that a user can be created with valid data.
        """
        data = {
            "username": self.username,
            "email": self.email,
            "password": self.password,
        }
        url = reverse("mvp_api:create-user")
        response = self.client.post(
            url,
            data,
            format="json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["message"], "User created successfully")

    def test_create_user_with_existing_username(self):
        """
        Test that a user cannot be created with an existing username.
        """
        data = {
            "username": self.username,
            "email": "mockuser@mock.com",
            "password": "mockpassword@123",
        }

        # Create the user
        User.objects.create_user(**data)

        # Attempt to create the user again
        url = reverse("mvp_api:create-user")
        response = self.client.post(
            url,
            data,
            format="json",
        )
        self.assertEqual(response.status_code, 400)

    def test_create_user_with_invalid_email(self):
        """
        Test that a user cannot be created with invalid data.
        """
        data = {
            "username": self.username,
            "email": "testuser@test",
            "password": self.password,
        }
        url = reverse("mvp_api:create-user")
        response = self.client.post(
            url,
            data,
            format="json",
        )
        self.assertEqual(response.status_code, 400)

    def test_create_user_with_invalid_password(self):
        """
        Test that a user cannot be created with invalid data.
        """
        data = {"username": self.username, "email": self.email, "password": "short"}

        url = reverse("mvp_api:create-user")
        response = self.client.post(
            url,
            data,
            format="json",
        )
        self.assertEqual(response.status_code, 400)

    def test_get_user_with_valid_id(self):
        """
        Test that a user can be retrieved with a valid id.
        """
        data = {
            "username": self.username,
            "email": self.email,
            "password": self.password,
        }

        # Create the user
        user = User.objects.create_user(**data)

        # Get the user
        url = reverse("mvp_api:get-user", kwargs={"id": user.id})
        response = self.client.get(
            url,
            format="json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], str(user.id))

    def test_get_user_with_invalid_id(self):
        """
        Test that a user cannot be retrieved with an invalid id.
        """
        data = {
            "username": self.username,
            "email": self.email,
            "password": self.password,
        }

        # Create the user
        User.objects.create_user(**data)

        # Get the user
        url = reverse("mvp_api:get-user", kwargs={"id": uuid4()})
        response = self.client.get(
            url,
            format="json",
        )
        self.assertEqual(response.status_code, 404)

    def test_update_user_password(self):
        """
        Test that a user's password can be updated.
        """
        data = {
            "username": self.username,
            "email": self.email,
            "password": self.password,
        }

        # Create the user
        user = User.objects.create_user(**data)

        # Update the user
        url = reverse("mvp_api:update-user", kwargs={"id": user.id})
        data = {"password": "newpassword@123"}
        response = self.client.put(
            url,
            data,
            format="json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["message"], "User updated successfully")

    def test_update_user_password_with_invalid_id(self):
        """
        Test that a user's password cannot be updated with an invalid id.
        """
        data = {
            "username": self.username,
            "email": self.email,
            "password": self.password,
        }

        # Create the user
        User.objects.create_user(**data)

        # Update the user
        url = reverse("mvp_api:update-user", kwargs={"id": uuid4()})
        data = {"password": "newpassword@123"}
        response = self.client.put(
            url,
            data,
            format="json",
        )
        self.assertEqual(response.status_code, 404)

    def test_update_user_password_with_invalid_data(self):
        """
        Test that a user's password cannot be updated with invalid data.
        """
        data = {
            "username": self.username,
            "email": self.email,
            "password": self.password,
        }

        # Create the user
        user = User.objects.create_user(**data)

        # Update the user
        url = reverse("mvp_api:update-user", kwargs={"id": user.id})
        data = {"password": "short"}
        response = self.client.put(
            url,
            data,
            format="json",
        )
        self.assertEqual(response.status_code, 400)

    def test_delete_user(self):
        """
        Test that a user can be deleted.
        """
        data = {
            "username": self.username,
            "email": self.email,
            "password": self.password,
        }

        # Create the user
        user = User.objects.create_user(**data)

        # Delete the user
        url = reverse("mvp_api:delete-user", kwargs={"id": user.id})
        response = self.client.delete(
            url,
            format="json",
        )
        self.assertEqual(response.status_code, 204)

    def test_delete_user_with_invalid_id(self):
        """
        Test that a user cannot be deleted with an invalid id.
        """
        data = {
            "username": self.username,
            "email": self.email,
            "password": self.password,
        }

        # Create the user
        User.objects.create_user(**data)

        # Delete the user
        url = reverse("mvp_api:delete-user", kwargs={"id": uuid4()})
        response = self.client.delete(
            url,
            format="json",
        )
        self.assertEqual(response.status_code, 404)
