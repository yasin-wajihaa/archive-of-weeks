from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings 


urlpatterns = [
    path('terms/', include('terms.urls')),
    path('courses/', include('courses.urls')),
    path('progress/', include('progress.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)