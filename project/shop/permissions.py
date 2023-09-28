from rest_framework.permissions import BasePermission, SAFE_METHODS

from rest_framework.exceptions import PermissionDenied
from .exceptions import NotAuthorized


class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if not bool(request.user.is_staff):
            raise PermissionDenied({'message': 'Forbidden for you'})

        return bool(request.user.is_staff)


class CustomIsAuthenticated(BasePermission):

    def has_permission(self, request, view):
        if not bool(request.user and request.user.is_authenticated):
            raise NotAuthorized()
        return True
