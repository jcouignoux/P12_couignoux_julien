from rest_framework.permissions import BasePermission


def authenticated(user):
    return bool(user and user.is_authenticated)


def management(request):
    return bool(request.user.groups.filter(name="Management").exists())


def read_member(user):
    return bool(authenticated(user) and 'staff.view_user' in user.get_group_permissions())


def write_member(user):
    return bool(authenticated(user) and 'staff.add_user' in user.get_group_permissions())


def read_client(user):
    return bool(authenticated(user) and 'clients.view_client' in user.get_group_permissions())


def modify_client(user):
    return bool(authenticated(user) and 'clients.change_client' in user.get_group_permissions())


def write_client(user):
    return bool(authenticated(user) and 'clients.add_client' in user.get_group_permissions())


def read_contract(user):
    return bool(authenticated(user) and 'contracts.view_contract' in user.get_group_permissions())


def modify_contract(user):
    return bool(authenticated(user) and 'contracts.change_contract' in user.get_group_permissions())


def write_contract(user):
    return bool(authenticated(user) and 'contracts.add_contract' in user.get_group_permissions())


def read_event(user):
    return bool(authenticated(user) and 'events.view_event' in user.get_group_permissions())


def modify_event(user):
    return bool(authenticated(user) and 'events.change_event' in user.get_group_permissions())


def write_event(user):
    return bool(authenticated(user) and 'events.add_event' in user.get_group_permissions())


class MemberPermission(BasePermission):

    edit_methods = ("GET", "POST", "PUT", "DELETE")

    def has_permission(self, request, view):
        user = request.user
        if request.method == "GET":
            return read_member(user)
        else:
            return write_member(user)

    def has_object_permission(self, request, view, obj):
        user = request.user

        return write_member(user)


class ClientPermission(BasePermission):

    edit_methods = ("GET", "POST", "PUT", "DELETE")

    def has_permission(self, request, view):
        user = request.user
        if request.method == "GET":
            return read_client(user)
        elif request.method == "PUT":
            return modify_client(user)
        else:
            return write_client(user)

    def has_object_permission(self, request, view, obj):
        user = request.user
        is_reponsible = bool(obj.sales_contact)

        return bool(is_reponsible or modify_client(user))


class ContractPermission(BasePermission):

    edit_methods = ("GET", "POST", "PUT", "DELETE")

    def has_permission(self, request, view):
        user = request.user
        if request.method == "GET":
            return read_contract(user)
        elif request.method == "PUT":
            return modify_client(user)
        else:
            return write_client(user)

    def has_object_permission(self, request, view, obj):
        user = request.user
        is_reponsible = bool(obj.sales_contact == user)

        return bool(is_reponsible or modify_contract(user))


class EventPermission(BasePermission):

    edit_methods = ("GET", "POST", "PUT", "DELETE")

    def has_permission(self, request, view):
        user = request.user
        if request.method == "GET":
            return read_event(user)
        elif request.method == "PUT":
            return modify_event(user)
        else:
            return write_event(user)

    def has_object_permission(self, request, view, obj):
        user = request.user
        is_reponsible = bool(obj.support_contact == request.user)

        return bool(is_reponsible or modify_event(user))
