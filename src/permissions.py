from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUserOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.is_superuser
        )


class IsStaffOrOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        print(obj)
        print("*" * 10)
        return bool(
            request.user.is_authenticated and request.user.is_superuser or
            request.user.is_authenticated and obj == request.user
        )
