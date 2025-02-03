# recipe_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
    path('logout/', logout_view, name='logout'),
]

# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)