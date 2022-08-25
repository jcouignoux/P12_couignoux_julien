from rest_framework.permissions import BasePermission


class ManagePermission(BasePermission):

    edit_methods = ("GET", "PUT", "DELETE")

    def has_permission(self, request, view):

        return bool(request.user and request.user.is_authenticated and request.user.groups.filter(name="Management").exists())

    def has_object_permission(self, request, view, obj):

        return bool(request.user and request.user.is_authenticated and request.user.groups.filter(name="Management").exists())


class SalePermission(BasePermission):

    edit_methods = ("GET", "PUT", "DELETE")

    def has_permission(self, request, view):

        return bool(request.user and request.user.is_authenticated and request.user.groups.filter(name="Sales").exists())

    def has_object_permission(self, request, view, obj):

        return bool(request.user and request.user.is_authenticated and request.user.groups.filter(name="Sales").exists())


class SupportPermission(BasePermission):

    edit_methods = ("GET", "PUT", "DELETE")

    def has_permission(self, request, view):

        return bool(request.user and request.user.is_authenticated and request.user.groups.filter(name="Support").exists())

    def has_object_permission(self, request, view, obj):

        return bool(request.user and request.user.is_authenticated and request.user.groups.filter(name="Support").exists())
