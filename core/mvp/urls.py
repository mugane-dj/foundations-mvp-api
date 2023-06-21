from django.urls import path
from .users import (
    GetUserView,
    ListUserView,
    create_user,
    update_user,
    get_user_token,
    DestroyUserView,
)
from .complaints import (
    GetComplaintView,
    ListComplaintView,
    CreateComplaintView,
    UpdateComplaintView,
    DestroyComplaintView,
)

app_name = "mvp"

urlpatterns = [
    path("user/<int:id>", GetUserView.as_view(), name="get-user"),
    path("user/all", ListUserView.as_view(), name="get-all-users"),
    path("user/<int:id>/token", get_user_token, name="get-user-token"),
    path("user/create", create_user, name="create-user"),
    path("user/update/<int:id>", update_user, name="update-user"),
    path("user/delete/<int:id>", DestroyUserView.as_view(), name="delete-user"),
    path("complaint/<uuid:id>", GetComplaintView.as_view(), name="get-complaint"),
    path("complaint/all", ListComplaintView.as_view(), name="get-all-complaints"),
    path("complaint/create", CreateComplaintView.as_view(), name="create-complaint"),
    path(
        "complaint/update/<uuid:id>",
        UpdateComplaintView.as_view(),
        name="update-complaint",
    ),
    path(
        "complaint/delete/<uuid:id>",
        DestroyComplaintView.as_view(),
        name="delete-complaint",
    ),
]
