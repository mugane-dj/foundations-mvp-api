from .models import User, Complaint, Comment
from django.contrib import admin


class UserAdmin(admin.ModelAdmin):
    """
    Admin class for the User model.
    """

    fields = [
        "id",
        "username",
        "email",
        "password",
        "token",
        "is_staff",
        "is_active",
        "is_superuser",
        "created_at",
        "updated_at",
    ]

    readonly_fields = [
        "id",
        "username",
        "email",
        "password",
        "token",
        "created_at",
        "updated_at",
    ]

    list_display = [
        "id",
        "username",
        "email",
        "token",
        "is_staff",
        "is_active",
        "is_superuser",
        "created_at",
        "updated_at",
    ]

    list_filter = [
        "is_staff",
        "is_active",
        "is_superuser",
        "created_at",
        "updated_at",
    ]

    search_fields = [
        "username",
    ]


class ComplaintAdmin(admin.ModelAdmin):
    """
    Admin class for the Complaint model.
    """

    fields = [
        "id",
        "title",
        "user",
        "description",
        "status",
        "longitude",
        "latitude",
        "created_at",
        "updated_at",
        "image",
    ]

    readonly_fields = [
        "id",
        "title",
        "user",
        "description",
        "longitude",
        "latitude",
        "created_at",
        "updated_at",
        "image",
    ]

    list_display = [
        "id",
        "title",
        "user",
        "description",
        "status",
        "longitude",
        "latitude",
        "created_at",
        "updated_at",
        "image",
    ]

    list_filter = [
        "status",
        "created_at",
        "updated_at",
    ]

    search_fields = [
        "title",
        "description",
    ]

    ordering = [
        "created_at",
    ]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        if obj.status == "completed":
            obj.user.token += 100
            obj.user.save()


class CommentAdmin(admin.ModelAdmin):
    """
    Admin class for the Comment model.
    """

    fields = [
        "id",
        "user",
        "complaint",
        "comment",
        "created_at",
        "updated_at",
    ]

    readonly_fields = [
        "id",
        "user",
        "complaint",
        "comment",
        "created_at",
        "updated_at",
    ]

    list_display = [
        "id",
        "user",
        "complaint",
        "comment",
        "created_at",
        "updated_at",
    ]

    list_filter = [
        "user",
        "complaint",
        "created_at",
    ]

    search_fields = [
        "comment",
    ]

    ordering = [
        "created_at",
    ]


admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(User, UserAdmin)
