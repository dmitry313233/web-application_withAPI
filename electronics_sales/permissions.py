from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsActivePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        return False
