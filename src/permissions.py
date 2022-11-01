from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUserOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.is_superuser
        )


class IsOperatorOrStaff(BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(obj.organizational_interface == request.user or
                    request.user.is_staff)


class IsFounderOrStaff(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(obj.company.organizational_interface == request.user or
                    request.user.is_staff)


class IsUserOrStaff(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.user == request.user or request.user.is_staff:
            return True
        return False
