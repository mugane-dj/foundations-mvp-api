from uuid import uuid4
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

__all__ = ["User", "UserManager", "Complaint", "Comment"]


class UserManager(BaseUserManager):
    """UserManager definition."""

    def create_user(
        self,
        username,
        email,
        password=None,
    ):
        """Create and return a `User` with an email, username and password."""
        if username is None:
            raise TypeError("Users must have a username.")

        if email is None:
            raise TypeError("Users must have an email address.")

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        """Create and return a `User` with superuser (admin) permissions."""
        if password is None:
            raise TypeError("Superusers must have a password.")

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User model definition."""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    username = models.CharField(max_length=255, unique=True, null=False, editable=False)
    email = models.EmailField(max_length=255, unique=True, null=False)
    token = models.IntegerField(null=True, editable=True, default=0)
    is_active = models.BooleanField(default=True, editable=True)
    is_staff = models.BooleanField(default=False, editable=True)
    is_superuser = models.BooleanField(default=False, editable=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    def __str__(self):
        return f"{self.username} - {self.email}"


class Complaint(models.Model):
    """Model definition for Complaint."""

    STATUS_CHOICES = (
        ("pending", "pending"),
        ("in_progress", "in_progress"),
        ("completed", "completed"),
    )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=20)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    image = models.ImageField(upload_to="complaints")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Complaint."""

        verbose_name = "Complaint"
        verbose_name_plural = "Complaints"

    def __str__(self):
        return f"{self.title} - {self.status}"


class Comment(models.Model):
    """Model definition for Comment."""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Comment."""

        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.comment
