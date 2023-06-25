from django.urls import path
from .users import (
    ListUserView,
    create_user,
    update_user,
    get_user_token,
    get_user,
    DestroyUserView,
)
from .complaints import (
    GetComplaintView,
    ListComplaintView,
    CreateComplaintView,
    UpdateComplaintView,
    DestroyComplaintView,
)
from .comments import (
    GetCommentView,
    ListCommentView,
    CreateCommentView,
    UpdateCommentView,
    DestroyCommentView,
)

app_name = "mvp_api"

urlpatterns = [
    path("user/<uuid:id>", get_user, name="get-user"),
    path("user/all", ListUserView.as_view(), name="get-all-users"),
    path("user/<uuid:id>/token", get_user_token, name="get-user-token"),
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
    path("comment/<uuid:id>", GetCommentView.as_view(), name="get-comment"),
    path("comment/all", ListCommentView.as_view(), name="get-all-comments"),
    path("comment/create", CreateCommentView.as_view(), name="create-comment"),
    path(
        "comment/update/<uuid:id>", UpdateCommentView.as_view(), name="update-comment"
    ),
    path(
        "comment/delete/<uuid:id>", DestroyCommentView.as_view(), name="delete-comment"
    ),
]
