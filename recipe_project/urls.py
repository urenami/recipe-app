from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),  

    # All built-in auth routes (login, logout, password reset, etc.)
    path('accounts/', include('django.contrib.auth.urls')),

    # Force logout to use your logged_out.html template
    path(
        'accounts/logout/',
        auth_views.LogoutView.as_view(template_name='registration/logged_out.html'),
        name='logout'
    ),
]

# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
