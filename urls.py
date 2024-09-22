from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path(
        "main/",
        include("main.urls", namespace="main")
    ),
    path(
        "authentication/",
        include("authentication.urls", namespace="authentication")
    ),
    path("", views.authenticate_redirection),
    path('admin/', admin.site.urls),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root = settings.MEDIA_ROOT
)