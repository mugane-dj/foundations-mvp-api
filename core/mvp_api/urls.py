from django.urls import path
from .users import (
    ListUserView,
    create_user,
    update_user,
    get_user_token,
    get_user,
    get_user_complaints,
    DestroyUserView,
)
from .complaints import (
    GetComplaintView,
    ListComplaintView,
    CreateComplaintView,
    UpdateComplaintView,
    DestroyComplaintView,
    get_complaint_comments,
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
    path("users/<uuid:id>", get_user, name="get-user"),
    path("users/", ListUserView.as_view(), name="get-all-users"),
    path("users/<uuid:id>/tokens", get_user_token, name="get-user-token"),
    path("users/<uuid:id>/complaints", get_user_complaints, name="get-user-complaints"),
    path("users/create", create_user, name="create-user"),
    path("users/update/<uuid:id>", update_user, name="update-user"),
    path("users/delete/<uuid:id>", DestroyUserView.as_view(), name="delete-user"),
    path("complaints/<uuid:id>", GetComplaintView.as_view(), name="get-complaint"),
    path(
        "complaints/<uuid:id>/comments",
        get_complaint_comments,
        name="get-complaint-comments",
    ),
    path("complaints/", ListComplaintView.as_view(), name="get-all-complaints"),
    path("complaints/create", CreateComplaintView.as_view(), name="create-complaint"),
    path(
        "complaints/update/<uuid:id>",
        UpdateComplaintView.as_view(),
        name="update-complaint",
    ),
    path(
        "complaints/delete/<uuid:id>",
        DestroyComplaintView.as_view(),
        name="delete-complaint",
    ),
    path("comments/<uuid:id>", GetCommentView.as_view(), name="get-comment"),
    path("comments/", ListCommentView.as_view(), name="get-all-comments"),
    path("comments/create", CreateCommentView.as_view(), name="create-comment"),
    path(
        "comments/update/<uuid:id>", UpdateCommentView.as_view(), name="update-comment"
    ),
    path(
        "comments/delete/<uuid:id>", DestroyCommentView.as_view(), name="delete-comment"
    ),
]
