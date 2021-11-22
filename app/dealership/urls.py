from django.urls import path

from .views import get_entries, create_entry, delete_entry, edit_entry

urlpatterns = [
    path("all/", get_entries, name="get_entries"),
    path("create/", create_entry, name="create_entry"),
    path(
        "delete/<str:vehicle_type>/<str:vehicle_id>", delete_entry, name="delete_entry"
    ),
    path("edit/<str:vehicle_type>/<str:vehicle_id>", edit_entry, name="edit_entry"),
]
