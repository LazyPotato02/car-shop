from rest_framework import permissions


class IsGetOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method == 'GET'


class IsAuthenticatedAndPostOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.method == 'POST':
            return True
        return False
