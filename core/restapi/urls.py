from django.urls import path
from .users import get_user, get_all_users, create_user, update_user, delete_user

app_name = "restapi"

urlpatterns = [
    path("user", get_user, name="get_user"),
    path("user/all", get_all_users, name="get_all_users"),
    path("user/create", create_user, name="create_user"),
    path("user/update", update_user, name="update_user"),
    path("user/delete", delete_user, name="delete_user"),
]
