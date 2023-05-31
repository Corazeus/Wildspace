from django.shortcuts import render
from .assigned_area_controller import AssignedAreaController
from polls.models import AssignedArea
from polls.time_monitoring import TimeMonitoringController
from wiladmin.models import WalkinBooking
from .facility_map_controller import FacilityMapController
from django.http import JsonResponse

facility_controller = FacilityMapController()
assigned_area_controller = AssignedAreaController()
time_monitoring_controller = TimeMonitoringController()


def show_message_view(request):
    message = facility_controller.showMessage(request)
    return JsonResponse({'message': message})

def index(request):
    return render(request, "wil/base.html", {})


def location(request):
    return assigned_area_controller.location(request)


def timer(request):
    context = time_monitoring_controller.timer(request)

    return render(request, "wil/timer.html", context)
    



area_button_click = facility_controller.areaButtonClick
insert_into_database = facility_controller.insertIntoDatabase
hideMessage = facility_controller.hideMessage
handleYesButtonClick = facility_controller.handleYesButtonClick






