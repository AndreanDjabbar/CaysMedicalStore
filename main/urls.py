from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path(
        "delete-product/<slug:slug_product>/",
        views.delete_product,
        name="delete_product"
    ),
    path(
        "update-product/<slug:slug_product>/",
        views.update_product,
        name="update_product"
    ),
    path(
        "detail-product/<slug:slug_product>/",
        views.detail_product,
        name="detail_product"
    ),
    path(
        "edit-profile/",
        views.edit_profile,
        name="edit_profile"
    ),
    path(
        "profile/",
        views.view_profile,
        name="profile"
    ),
    path(
        "create/",
        views.create,
        name="create"
    ),
    path(
        "home/",
        views.home,
        name="home"
    ),
    path(
        "",
        views.main_redirection
    ),
]