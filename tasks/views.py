from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer

# 🔽 Импорт для регистрации
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]  # временно, для отладки

    def get_queryset(self):
        # Показываем задачи только текущего пользователя
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        # При создании задачи сохраняем владельца (текущего пользователя)
        serializer.save(owner=self.request.user)


# ✅ Регистрация нового пользователя через API
@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Требуются имя пользователя и пароль'}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Пользователь уже существует'}, status=400)

    user = User.objects.create_user(username=username, password=password)
    return Response({'message': 'Пользователь создан'}, status=201)