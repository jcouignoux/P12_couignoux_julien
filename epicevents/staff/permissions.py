from rest_framework.permissions import BasePermission


def authenticated(request):
    return bool(request.user and request.user.is_authenticated)


def management(request):
    return bool(request.user.groups.filter(name="Management").exists())


class MemberPermission(BasePermission):

    edit_methods = ("GET", "POST", "PUT", "DELETE")

    def has_permission(self, request, view):
        if request.method == "GET":
            return authenticated(request)
        else:
            return bool(authenticated(request) and management(request))

    def has_object_permission(self, request, view, obj):

        return bool(authenticated(request) and management(request))


class ClientPermission(BasePermission):

    edit_methods = ("GET", "POST", "PUT", "DELETE")

    def has_permission(self, request, view):
        if request.method == "GET":
            return authenticated(request)
        elif request.method == "PUT":
            return bool(authenticated(request) and (request.user.groups.filter(name="Sales").exists() or management(request)))
        else:
            return bool(authenticated(request) and request.user.groups.filter(name="Sales").exists())

    def has_object_permission(self, request, view, obj):
        is_reponsible = bool(obj.sales_contact == request.user)

        return bool(authenticated(request) and (management(request) or is_reponsible))


class ContractPermission(BasePermission):

    edit_methods = ("GET", "POST", "PUT", "DELETE")

    def has_permission(self, request, view):

        if request.method == "GET":
            return authenticated(request)
        elif request.method == "PUT":
            return bool(authenticated(request) and (request.user.groups.filter(name="Sales").exists() or management(request)))
        else:
            return bool(authenticated(request) and request.user.groups.filter(name="Sales").exists())

    def has_object_permission(self, request, view, obj):
        is_reponsible = bool(obj.sales_contact == request.user)

        return bool(authenticated(request) and (management(request) or is_reponsible))


class EventPermission(BasePermission):

    edit_methods = ("GET", "POST", "PUT", "DELETE")

    def has_permission(self, request, view):

        if request.method == "GET":
            return authenticated(request)
        elif request.method == "PUT":
            return bool(authenticated(request) and (management(request) or request.user.groups.filter(name="Support").exists()))
        else:
            return bool(authenticated(request) and request.user.groups.filter(name="Support").exists())

    def has_object_permission(self, request, view, obj):
        is_reponsible = bool(obj.support_contact == request.user)

        return bool(authenticated(request) and (management(request) or is_reponsible))
