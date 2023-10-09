from django.shortcuts import render
from polls.models import AssignedArea
from wiladmin.models import WalkinBookingModel


class TimeMonitoringController:
    def getTimer(self, request):
        walkinbooking = WalkinBookingModel.objects.get(userid=request.user.username)
        reference = walkinbooking.referenceid

        context = {
            'id_number': walkinbooking.userid if walkinbooking else 'N/A',
            'booking_reference_number': walkinbooking.referenceid if walkinbooking else 'N/A',
            'assigned_area': reference[:2] if reference else 'N/A',
            'date_of_use': walkinbooking.schedule if walkinbooking else 'N/A',
        }

        return context

    