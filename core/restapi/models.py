from django.db import models
from uuid import uuid4


class Complaint(models.Model):
    """Model definition for Complaint."""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    user_id = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=255)
    longitude = models.FloatField()
    latitude = models.FloatField()
    image = models.ImageField(upload_to="complaints")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Complaint."""

        verbose_name = "Complaint"
        verbose_name_plural = "Complaints"

    def __str__(self):
        return self.name, self.status


class Comment(models.Model):
    """Model definition for Comment."""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    complaint_id = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    user_id = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Comment."""

        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.comment


class Reward(models.Model):
    """Model definition for Reward."""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user_id = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    complaint_id = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    token = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Reward."""

        verbose_name = "Reward"
        verbose_name_plural = "Rewards"

    def __str__(self):
        return self.token
