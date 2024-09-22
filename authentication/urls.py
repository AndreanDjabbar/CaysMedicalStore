from django.urls import path
from . import views

app_name = "authentication"

urlpatterns = [
    path(
        "logout/",
        views.logout_process,
        name="logout_process"
    ),
    path(
        "logout-page/",
        views.logout_page,
        name="logout"
    ),
    path(
        "login-page/",
        views.login_page,
        name="login"
    ),
    path(
        "register/",
        views.register,
        name="register"
    ),
    path(
        "",
        views.login_redirection
    ),
]