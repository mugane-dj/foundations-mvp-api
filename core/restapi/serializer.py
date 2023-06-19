from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Complaint, Comment, Reward


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]

    username = serializers.CharField(required=True, allow_blank=False, max_length=100)
    email = serializers.EmailField(required=True, allow_blank=False, max_length=100)
    password = serializers.CharField(required=True, allow_blank=False, max_length=100)

    def validate(self, attrs):
        username = attrs.get("username", "")
        email = attrs.get("email", "")

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({"username": "Username already exists."})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "Email already exists."})

        return super().validate(attrs)

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        raise NotImplementedError


class UserGetSerializer(serializers.ModelSerializer):
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


class UserGetAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]

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

    id = serializers.IntegerField(required=True)
    password = serializers.CharField(required=True, allow_blank=False, max_length=100)

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
        fields = "__all__"

    name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    description = serializers.CharField(
        required=True, allow_blank=False, max_length=100
    )
    status = serializers.CharField(required=True, allow_blank=False, max_length=100)
    image = serializers.ImageField(required=True)

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        raise NotImplementedError


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

    complaint_id = serializers.CharField(
        required=True, allow_blank=False, max_length=100
    )
    comment = serializers.CharField(required=True, allow_blank=False, max_length=100)

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        raise NotImplementedError


class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = "__all__"

    complaint_id = serializers.CharField(
        required=True, allow_blank=False, max_length=100
    )
    token = serializers.IntegerField(required=True)

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        raise NotImplementedError
