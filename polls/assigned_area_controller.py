from django.shortcuts import render
from polls.models import AssignedArea
from wiladmin.models import WalkinBookingModel

class AssignedAreaController:
    def getAssignedArea(self, request):
        
        walkinbooking = WalkinBookingModel.objects.get(userid=request.user.username)
        area_id = walkinbooking.referenceid

        context = {
            'area_id': area_id[:2],
        }

        return render(request, "wil/location.html", context)
