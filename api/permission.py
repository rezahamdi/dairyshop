from rest_framework import permissions



class IsAdminOrReadOnly(permissions.BasePermission):
    """
     With This permission only the staff can be 
     create , update , and delete the object
     Other users only can read the data
    """
    def has_permission(self,request,view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)