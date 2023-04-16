from rest_framework import permissions
from rest_framework.views import Request, View
from users.models import User


class UsersPermission(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User) -> bool:
        return (
            obj.id == request.user.id
            and request.user.is_authenticated
            or request.user.is_superuser
        )
