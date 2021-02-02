from rest_framework.permissions import BasePermission


class IsWaiter(BasePermission):
    message = 'you must be waiter user'

    def has_permission(self, request, view):
        return request.user.user_type == 'WAITER'


class IsAssitantOrChief(BasePermission):
    message = "you are not authorized to update at this status"

    def has_permission(self, request, view):
        self.message = 'you must be assisant or chief user'
        return request.user.user_type == 'ASSISTANT' or request.user.user_type == 'CHIEF'

    def has_object_permission(self, request, view, obj):
        if obj.assigned_to is not None and obj.assigned_to != request.user:
            self.message = 'this order assigned to anoter assisant user'
            return False
        if obj.status == 'New':
            obj.status = 'Preparing'
            return True
        elif obj.status == 'Preparing':
            obj.status = 'Waiting Review'
            return True
        elif obj.status == 'Waiting Review' and request.user.user_type == 'CHIEF':
            obj.status = 'Ready'
            return True
        return False


class IsChief(BasePermission):
    message = ""

    def has_permission(self, request, view):
        self.message = 'you must be Chief user'
        return request.user.user_type == 'CHIEF'

    def has_object_permission(self, request, view, obj):
        if obj.status == 'Waiting Review':
            obj.status = 'Ready'
            return True
        return False


class IsChiefAndAdmin(BasePermission):
    message = ''

    def has_permission(self, request, view):
        self.message = 'you must be chief and admin user'
        return request.user.user_type == "CHIEF" and request.user.chief.is_client_admin
