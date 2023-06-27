from rest_framework.test import APIClient
from faker import Faker
import base64
from django.contrib.auth import get_user_model

User = get_user_model()


def authorized_client():
    """
    Create an authorized client.
    """
    fake = Faker()
    username = fake.user_name()
    email = fake.email()
    password = fake.password()
    User.objects.create_superuser(username, email, password)
    encoded_credentials = base64.b64encode(
        f"{email}:{password}".encode("utf-8")
    ).decode("utf-8")
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Basic {encoded_credentials}")
    return client
