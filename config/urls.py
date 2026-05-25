from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('terms/', include('terms.urls')),
    path('courses/', include('courses.urls')),
    path('progress/', include('progress.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
]
