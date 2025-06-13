from django.db import models
from django.contrib.auth.models import User  # импортируем модель пользователя

class Task(models.Model):
    PRIORITY_CHOICES = [
        ("L", "Low"),
        ("M", "Medium"),
        ("H", "High"),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # добавляем поле владельца задачи

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    tags = models.CharField(max_length=100, blank=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default="M")
    deadline = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
