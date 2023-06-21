import uuid
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Complaint


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def validate(self, attrs):
        username = attrs.get("username", "")
        email = attrs.get("email", "")

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({"username": "Username already exists."})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "Email already exists."})

        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        raise NotImplementedError


class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id"]

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

    def validate(self, attrs):
        id = self.context["request"].parser_context["kwargs"]["id"]
        try:
            User.objects.get(id=id)
        except User.DoesNotExist:
            raise serializers.ValidationError({"id": "User does not exist."})

        return super().validate(attrs)

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        instance.set_password(validated_data["password"])
        instance.save()
        return instance


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
            uuid.UUID(str(complaint_id))  # Validate if it's a valid UUID
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
