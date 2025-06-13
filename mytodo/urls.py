from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("tasks.urls")),  # вот эта строка должна быть!
    path("api-auth/", include("rest_framework.urls")),
]
