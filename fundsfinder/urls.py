from django.contrib import admin
from django.urls import path, include

urlpatterns = [
path('api/v1/', include('api.urls', namespace='api')),
path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
path('admin/', admin.site.urls),
]