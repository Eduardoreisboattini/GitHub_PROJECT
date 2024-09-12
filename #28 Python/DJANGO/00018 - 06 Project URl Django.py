#include your app’s urls.py in the main project’s urls.py ymyproject/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Include app's URLs
]
