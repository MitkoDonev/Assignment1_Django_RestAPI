from django.urls import path

from .views import get_entries, create_entry

urlpatterns = [
    path("all/", get_entries, name="get_entries"),
    path("create/", create_entry, name="create_entry"),
]
