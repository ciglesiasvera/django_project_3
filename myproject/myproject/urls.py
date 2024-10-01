from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book.urls')),  # Incluir las URLs de la aplicación book
]

