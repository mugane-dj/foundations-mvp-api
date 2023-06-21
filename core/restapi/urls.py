from django.urls import path
from .users import (
    GetUserView,
    ListUserView,
    CreateUserView,
    UpdateUserView,
    DestroyUserView,
)
from .complaints import (
    GetComplaintView,
    ListComplaintView,
    CreateComplaintView,
    UpdateComplaintView,
    DestroyComplaintView,
)

app_name = "restapi"

urlpatterns = [
    path("user/<int:id>", GetUserView.as_view(), name="get-user"),
    path("user/all", ListUserView.as_view(), name="get-all-users"),
    path("user/create", CreateUserView.as_view(), name="create-user"),
    path("user/update/<int:id>", UpdateUserView.as_view(), name="update-user"),
    path("user/delete/<int:id>", DestroyUserView(), name="delete-user"),
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
