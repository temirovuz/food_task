from rest_framework import permissions


class IsAdminOrWaiter(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['admin', 'waiter']
