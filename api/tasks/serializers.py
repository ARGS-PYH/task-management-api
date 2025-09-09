from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task
from django.utils import timezone


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"],
        )
        return user


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Task
        fields = [
            "id",
            "user",
            "title",
            "description",
            "start_date",
            "due_date",
            "priority",
            "status",
            "completed_at",
        ]


def validate(self, data):
    start_date = data.get("start_date")   
    due_date = data.get("due_date")       

    if start_date and start_date < timezone.now().date():
        raise serializers.ValidationError("Start date cannot be in the past.")

    if start_date and due_date:
        if due_date.date() < start_date:
            raise serializers.ValidationError("Due date cannot be earlier than start date.")

    return data
