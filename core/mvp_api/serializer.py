import uuid
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import PermissionDenied
from .models import User, Complaint, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]

    username = serializers.CharField(max_length=255, required=True)
    email = serializers.EmailField(max_length=255, required=True)
    password = serializers.CharField(max_length=255, required=True)

    def validate(self, attrs):
        username = attrs.get("username", "")
        email = attrs.get("email", "")
        password = attrs.get("password", "")

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({"username": "Username already exists."})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "Email already exists."})

        try:
            validate_password(password)
        except serializers.ValidationError as e:
            raise serializers.ValidationError({"password": e.messages})

        return super().validate(attrs)

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        raise NotImplementedError


class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def validate(self, attrs):
        id = attrs.get("id", "")
        try:
            User.objects.get(id=id)
        except User.DoesNotExist:
            raise serializers.ValidationError({"id": "User does not exist."})

        return super().validate(attrs)

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        raise NotImplementedError


class UserGetAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]

    def validate(self, attrs):
        raise NotImplementedError

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        raise NotImplementedError


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "password"]

    def validate(self, attrs):
        password = attrs.get("password", "")
        try:
            validate_password(password)
        except serializers.ValidationError as e:
            raise serializers.ValidationError({"password": e.messages})
        return super().validate(attrs)

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        raise NotImplementedError


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id"]

    id = serializers.IntegerField(required=True)

    def validate(self, attrs):
        id = attrs.get("id", "")
        try:
            User.objects.get(id=id)
        except User.DoesNotExist:
            raise serializers.ValidationError({"id": "User does not exist."})

        return super().validate(attrs)

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        raise NotImplementedError


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = [
            "title",
            "user",
            "description",
            "status",
            "longitude",
            "latitude",
            "image",
        ]

    def validate(self, attrs):
        user = attrs.get("user", "")
        try:
            User(user)
        except User.DoesNotExist:
            raise serializers.ValidationError({"user": "User does not exist."})

        return super().validate(attrs)

    def create(self, validated_data):
        complaint = Complaint.objects.create(**validated_data)
        return complaint

    def update(self, instance, validated_data):
        raise NotImplementedError


class ComplaintGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = "__all__"

    def validate(self, attrs):
        complaint_id = attrs.get("id", "")
        try:
            Complaint.objects.get(id=complaint_id)
        except Complaint.DoesNotExist:
            raise serializers.ValidationError({"id": "Complaint does not exist"})
        return super().validate(attrs)

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        raise NotImplementedError


class ComplaintGetAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = "__all__"

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        raise NotImplementedError


class ComplaintUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ["id", "status"]

    def validate(self, attrs):
        complaint_id = self.context["request"].parser_context["kwargs"]["id"]
        try:
            uuid.UUID(str(complaint_id))
        except ValueError:
            raise serializers.ValidationError({"id": "Invalid UUID format"})
        try:
            Complaint.objects.get(id=complaint_id)
        except Complaint.DoesNotExist:
            raise serializers.ValidationError({"id": "Complaint does not exist"})
        return super().validate(attrs)

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        complaint_id = self.context["request"].parser_context["kwargs"]["id"]
        request_user = self.context["request"].user
        if not request_user.is_staff or not request_user.is_superuser:
            raise PermissionDenied(
                {"user": "Only staff and superuser can update complaint status"}
            )

        complaint = Complaint.objects.get(id=complaint_id)
        if validated_data.get("status") == "completed":
            user = complaint.user
            user.token += 100
            user.save()
        instance.status = validated_data.get("status", instance.status)
        instance.save()
        return instance


class ComplaintDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ["id"]

    def validate(self, attrs):
        complaint_id = attrs.get("id", "")
        try:
            Complaint.objects.get(id=complaint_id)
        except Complaint.DoesNotExist:
            raise serializers.ValidationError({"id": "Complaint does not exist"})
        return super().validate(attrs)

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        raise NotImplementedError


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "id",
            "complaint",
            "user",
            "comment",
        ]

    def validate(self, attrs):
        user = attrs.get("user", "")
        complaint = attrs.get("complaint", "")
        try:
            User(user)
            Complaint(complaint)
        except User.DoesNotExist:
            raise serializers.ValidationError({"user": "User does not exist."})
        except Complaint.DoesNotExist:
            raise serializers.ValidationError(
                {"complaint": "Complaint does not exist."}
            )

        return super().validate(attrs)

    def create(self, validated_data):
        comment = Comment.objects.create(**validated_data)
        return comment

    def update(self, instance, validated_data):
        raise NotImplementedError


class CommentGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

    def validate(self, attrs):
        comment_id = attrs.get("id", "")
        try:
            Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            raise serializers.ValidationError({"id": "Comment does not exist"})
        return super().validate(attrs)

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        raise NotImplementedError


class CommentGetAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        raise NotImplementedError


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "comment"]

    def validate(self, attrs):
        comment_id = self.context["request"].parser_context["kwargs"]["id"]
        try:
            uuid.UUID(str(comment_id))
        except ValueError:
            raise serializers.ValidationError({"id": "Invalid UUID format"})
        try:
            Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            raise serializers.ValidationError({"id": "Comment does not exist"})
        return super().validate(attrs)

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        instance.comment = validated_data.get("comment", instance.comment)
        instance.save()
        return instance


class CommentDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id"]

    def validate(self, attrs):
        comment_id = attrs.get("id", "")
        try:
            Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            raise serializers.ValidationError({"id": "Comment does not exist"})
        return super().validate(attrs)

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        raise NotImplementedError
