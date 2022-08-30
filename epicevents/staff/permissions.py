from rest_framework.permissions import BasePermission


class MemberPermission(BasePermission):

    edit_methods = ("GET", "POST", "PUT", "DELETE")

    def has_permission(self, request, view):
        if request.method == "GET":
            return bool(request.user and request.user.is_authenticated)
        else:
            return bool(request.user and request.user.is_authenticated and request.user.groups.filter(name="Management").exists())

    def has_object_permission(self, request, view, obj):

        return bool(request.user and request.user.is_authenticated and request.user.groups.filter(name="Management").exists())


class ClientPermission(BasePermission):

    edit_methods = ("GET", "POST", "PUT", "DELETE")

    def has_permission(self, request, view):
        if request.method == "GET":
            return bool(request.user and request.user.is_authenticated)
        elif request.method == "PUT":
            return bool(request.user and request.user.is_authenticated and request.user.groups.filter(name__in=["Sales", "Management"]).exists())
        else:
            return bool(request.user and request.user.is_authenticated and request.user.groups.filter(name="Sales").exists())

    def has_object_permission(self, request, view, obj):

        return bool(request.user and request.user.is_authenticated and request.user.groups.filter(name__in=["Sales", "Management"]).exists())


class ContractPermission(BasePermission):

    edit_methods = ("GET", "POST", "PUT", "DELETE")

    def has_permission(self, request, view):
        if request.method == "GET":
            return bool(request.user and request.user.is_authenticated)
        else:
            return bool(request.user and request.user.is_authenticated and request.user.groups.filter(name="Sales").exists())

    def has_object_permission(self, request, view, obj):
        if request.method == "POST":
            return True
        return bool(request.user and request.user.is_authenticated and request.user.groups.filter(name__in=["Sales", "Management"]).exists())


class EventPermission(BasePermission):

    edit_methods = ("GET", "POST", "PUT", "DELETE")

    def has_permission(self, request, view):

        if request.method == "GET":
            return bool(request.user and request.user.is_authenticated)
        elif request.method == "PUT":
            return bool(request.user and request.user.is_authenticated and request.user.groups.filter(name__in=["Support", "Management"]).exists())
        else:
            return bool(request.user and request.user.is_authenticated and request.user.groups.filter(name="Support").exists())

    def has_object_permission(self, request, view, obj):

        return bool(request.user and request.user.is_authenticated and request.user.groups.filter(name__in=["Support", "Management"]).exists())
