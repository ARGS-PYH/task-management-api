from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Task
        fields = [
            "id",
            "user",
            "title",
            "description",
            "due_date",
            "priority",
            "status",
            "completed_at",
        ]
