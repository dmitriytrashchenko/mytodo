from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(
        source="owner.username"
    )  # 🔑 Это исправляет ошибку

    class Meta:
        model = Task
        fields = "__all__"
