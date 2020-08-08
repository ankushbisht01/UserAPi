from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """allow User to edit his/her own profile"""

    def has_object_permission(self, request, view, obj) :
        """check User is trying to edit its own Profile """

        if request.method in permissions.SAFE_METHODS:
            return True
        

        return obj.id == request.user.id