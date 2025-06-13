from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, TagViewSet

router = DefaultRouter()
router.register("tasks", TaskViewSet)
router.register("tags", TagViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
