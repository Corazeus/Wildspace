from django.shortcuts import render
from polls.models import AssignedArea
from wiladmin.models import WalkinBookingModel


class TimeMonitoringController:
    def getTimer(self, request):
        walkinbooking = WalkinBookingModel.objects.latest('bookingid')
        reference = AssignedArea.objects.latest('id')

        context = {
            'id_number': walkinbooking.userid if walkinbooking else 'N/A',
            'booking_reference_number': walkinbooking.referenceid if walkinbooking else 'N/A',
            'assigned_area': reference.area_id if reference else 'N/A',
            'date_of_use': walkinbooking.schedule if walkinbooking else 'N/A',
        }

        return context

    