from django.shortcuts import render
from polls.models import AssignedArea

class AssignedAreaController:
    def getAssignedArea(self, request):
        try:
            reference = AssignedArea.objects.latest('id')
            area_id = reference.area_id
        except AssignedArea.DoesNotExist:
            area_id = None

        context = {
            'area_id': area_id,
        }

        return render(request, "wil/location.html", context)
