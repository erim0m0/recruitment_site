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
        if any([
            obj.operator == request.user and \
            request.user.is_authenticated,
            request.user.is_staff
        ]):
            return True
        return False


class IsOperatorOrNot(BasePermission):
    message = "This user isn't an Operator"

    def has_permission(self, request, view):
        if any([
            request.user.is_operator and request.user.is_authenticated,
            request.user.is_superuser or request.user.is_staff
        ]):
            return True
        return False


class IsCompanyExistOrNot(BasePermission):
    message = "The company with this user's isn't exist."

    def has_permission(self, request, view):
        is_exist_company: bool = CompanyProfile.objects.filter(
            operator=request.user
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
            obj.company.operator == request.user or
            request.user.is_staff
        )


class IsUserOrStaff(BasePermission):
    message = "This user can't access the information"

    def has_object_permission(self, request, view, obj):
        if any([
            obj.user == request.user and request.user.is_authenticated,
            request.user.is_staff
        ]):
            return True
        return False
