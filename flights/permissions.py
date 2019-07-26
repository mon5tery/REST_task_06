from rest_framework.permissions import BasePermission
from datetime import date



class IsOwner(BasePermission):
	message = "only the owner of the booking can edit or cancel reservastions"
	
	def has_object_permission(self, request, view, obj):
		if request.user.is_staff or (obj.user == request.user):
			return True
		else:
			return False


class IsPast(BasePermission):
	message = "cant modify booking that's passed"

	def has_object_permission(self, request, view, obj):
		if  (obj.date - date.today()).days >=3:
			return True
		else:
			return False