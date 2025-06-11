from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('records/', include('records.urls')),
    path('', include('records.urls')),  # Home page shows records
]