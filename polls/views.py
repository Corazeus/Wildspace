from django.shortcuts import render

from polls.user_login_controller import UserLoginController
from .assigned_area_controller import AssignedAreaController
from polls.models import AssignedArea
from polls.time_monitoring import TimeMonitoringController
from wiladmin.models import WalkinBookingModel
from .facility_map_controller import FacilityMapController
from django.http import JsonResponse
from django.shortcuts import render
from .user_login_controller import UserLoginController
from django.contrib.auth.forms import AuthenticationForm

facility_controller = FacilityMapController()
assigned_area_controller = AssignedAreaController()
time_monitoring_controller = TimeMonitoringController()
user_login_controller = UserLoginController()



def show_message_view(request):
    message = facility_controller.showMessage(request)
    return JsonResponse({'message': message})

def map(request):
    return render(request, "wil/map.html", {})


def location(request):
    return assigned_area_controller.getAssignedArea(request)


def timer(request):
    context = time_monitoring_controller.getTimer(request)

    return render(request, "wil/timer.html", context)

def user_login(request):
    form = AuthenticationForm()
    return render(request, "wil/userlogin.html", {'form': form})

def user_dashboard(request):
    return render(request, "wil/userdashboard.html", {})




area_button_click = facility_controller.areaButtonClick
insert_into_database = facility_controller.insertIntoAssignedAreaModel
hideMessage = facility_controller.hideMessage
handleYesButtonClick = facility_controller.handleYesButtonClick






