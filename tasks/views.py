from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Показываем задачи только текущего пользователя
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        # При создании задачи сохраняем владельца (текущего пользователя)
        serializer.save(owner=self.request.user)
