from rest_framework.permissions import BasePermission, SAFE_METHODS

from accounts.models.company import CompanyProfile


class IsSuperUserOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.is_superuser
        )


class IsOperatorOrStaff(BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(
            obj.organizational_interface == request.user or
            request.user.is_staff
        )


class IsOperatorOrNot(BasePermission):
    message = "This user not a Operator"

    def has_permission(self, request, view):
        if request.user.is_operator or request.user.is_staff:
            return True


class IsCompanyExistOrNot(BasePermission):
    message = "The company with this user's isn't exist."

    def has_permission(self, request, view):
        is_exist_company: bool = CompanyProfile.objects.filter(
            organizational_interface=request.user
        ).exists()

        if not is_exist_company:
            return False
        return True


class IsFounderOrStaff(BasePermission):
    message = "This user isn't a founder of this Advertisement."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(
            obj.company.organizational_interface == request.user or
            request.user.is_staff
        )


class IsUserOrStaff(BasePermission):
    message = "This User isn't Access That Information"

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user or request.user.is_staff:
            return True
        return False
