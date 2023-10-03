from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from polls.user_login_controller import UserLoginController
from .assigned_area_controller import AssignedAreaController
from polls.models import AssignedArea
from polls.time_monitoring import TimeMonitoringController
from wiladmin.models import WalkinBookingModel
from .facility_map_controller import FacilityMapController
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .user_login_controller import UserLoginController
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from polls.user_login_controller import UserLoginController, user_logout

facility_controller = FacilityMapController()
assigned_area_controller = AssignedAreaController()
time_monitoring_controller = TimeMonitoringController()
user_login_controller = UserLoginController()



def show_message_view(request):
    message = facility_controller.showMessage(request)
    return JsonResponse({'message': message})

def map(request):

    username = request.user.username
    bookings = WalkinBookingModel.objects.all().count()
    userbooks = WalkinBookingModel.objects.filter(userid=username).count()
    
    if bookings != 0 and userbooks != 0:
        user = WalkinBookingModel.objects.get(userid=username)

        if user.status=="Booked":
            return redirect('location')
        else:
            return render(request, "wil/map.html", {})
        
    else:
        return render(request, "wil/map.html", {})


def location(request):
    return assigned_area_controller.getAssignedArea(request)

def user_profile(request):
    return render(request, "wil/userprofile.html", {})
def timer(request):
    context = time_monitoring_controller.getTimer(request)

    return render(request, "wil/timer.html", context)

def user_login(request):
    return user_login_controller.as_view()(request)

def user_logout(request):
    logout(request)
    return redirect('user_login')


def user_dashboard(request):
    return render(request, "wil/userdashboard.html", {})
    



area_button_click = facility_controller.areaButtonClick
insert_into_database = facility_controller.insertIntoAssignedAreaModel
hideMessage = facility_controller.hideMessage
handleYesButtonClick = facility_controller.handleYesButtonClick






