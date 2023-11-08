
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
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from polls.models import Timer
from django.views import View
from django.http import JsonResponse
from polls.models import Timer 
from asgiref.sync import sync_to_async
from django.shortcuts import render
from .models import AssignedArea, Booking
from django.db import models
from django.http import JsonResponse
from .models import AssignedArea
from django.http import JsonResponse
from collections import defaultdict
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from django.shortcuts import render

from django.http import JsonResponse

facility_controller = FacilityMapController()
assigned_area_controller = AssignedAreaController()
time_monitoring_controller = TimeMonitoringController()
user_login_controller = UserLoginController()



def show_message_view(request):
    message = facility_controller.showMessage(request)
    return JsonResponse({'message': message})

@login_required(redirect_field_name="userlogin")
def map(request):

    username = request.user.username
    bookings = WalkinBookingModel.objects.all().count()
    userbooks = WalkinBookingModel.objects.filter(userid=username).count()
    area_bookings = AssignedArea.objects.values('area_id').annotate(booked_count=models.Count('area_id'))
    
    areas = []
    for area_id in ["A3", "A4", "A5", "A6", "A8", "A9", "A7"]:
            if area_id == "A7":
                total_count = 24 
            else:
                total_count = 6
            area_data = next((item for item in area_bookings if item['area_id'] == area_id), {'booked_count': 0})
            areas.append({'area_id': area_id, 'booked_count': area_data['booked_count'], 'total_count': total_count})

    
    if bookings != 0 and userbooks != 0:
        user = WalkinBookingModel.objects.get(userid=username)

        if user.status=="Booked":
            return redirect('timer')
        else:
            return render(request, 'wil/map.html', {'areas': areas})
        
    else:
        return render(request, 'wil/map.html', {'areas': areas})

@login_required(redirect_field_name="userlogin")
def location(request):
    return assigned_area_controller.getAssignedArea(request)
@login_required(redirect_field_name="userlogin")
def user_profile(request):
    return render(request, "wil/userprofile.html", {})
@login_required(redirect_field_name="userlogin")
def timer(request):
    try:
        context = time_monitoring_controller.getTimer(request)
        return render(request, "wil/timer.html", context)
    except WalkinBookingModel.DoesNotExist:
        return redirect('user_dashboard')
@login_required(redirect_field_name="userlogin")
def user_login(request):
    return user_login_controller.as_view()(request)

def user_logout(request):
    logout(request)
    return redirect('user_login')

@login_required(redirect_field_name="userlogin")
def user_dashboard(request):
    
    area_bookings = AssignedArea.objects.values('area_id').annotate(booked_count=models.Count('area_id'))
    
    areas = []
    for area_id in ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9"]:
        if area_id == "A1" or area_id == "A2":
            total_count = 1
        elif area_id == "A7":
            total_count = 24
        else:
            total_count = 6

        area_data = next((item for item in area_bookings if item['area_id'] == area_id), {'booked_count': 0})
        areas.append({'area_id': area_id, 'booked_count': area_data['booked_count'], 'total_count': total_count})



    
    try:
        reservedbookingcount = Booking.objects.filter(user_id=request.user.username).count()
        booking = Booking.objects.get(user_id=request.user.username)
        if(reservedbookingcount > 0):
            if(booking.status == "Pending"):
                area_id = booking.reference_number
                context = {
                    'area_id': area_id[:2],
                    'reference_number': booking.reference_number,
                    'date': booking.date,
                    }
                return render(request, "wil/activebooking.html", context)
            else:
                timer = Timer.objects.get(user_id=request.user.username)
                context = {
                    'id_number': booking.user_id,
                    'booking_reference_number': booking.reference_number,
                    'assigned_area': booking.area_id,
                    'date_of_use': booking.date,
                    'timer_data': {
                        'minutes': timer.minutes,
                        'seconds': timer.seconds,
                    }
                }
                
                return render(request, "wil/timer.html", context)
            
    except Booking.DoesNotExist:
        areas = []
        for area_id in ["A1", "A2", "A3", "A4", "A5","A6"]:
            area_data = next((item for item in area_bookings if item['area_id'] == area_id), {'booked_count': 0})
            total_count = 6
            areas.append({'area_id': area_id, 'booked_count': area_data['booked_count'], 'total_count': total_count})
        
    return render(request, "wil/userdashboard.html", {'areas': areas})



def get_timer_data(request):
    
    timers = Timer.objects.all().count()
    
    if timers == 0:
        return redirect(user_dashboard)
    else:
        usertimer = Timer.objects.get(user_id=request.user.username)
    
        if usertimer is not None and usertimer.session_ended != True:
            if not usertimer.session_ended:
                if usertimer.seconds > 0:
                    usertimer.seconds -= 1
                elif usertimer.minutes > 0:
                    usertimer.minutes -= 1
                    usertimer.seconds = 59
                else:
                    usertimer.session_ended = True
                
                usertimer.save()

            timer_data = {
                'minutes': usertimer.minutes,
                'seconds': usertimer.seconds,
                'session_ended': usertimer.session_ended,
            }

            return JsonResponse(timer_data)
        
        else:
            return render(request, "wil/userdashboard.html", {})

@login_required
def end_session_view(request):
    if request.method == 'POST':
        
        try:
            timer = Timer.objects.get(pk=str(request.user.username))
            timer.session_ended = True
            timer.save()

            return JsonResponse({'success': True})

        except Timer.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Timer not found for the user.'})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})



def get_booking_info(request):
    
    area_bookings = AssignedArea.objects.values('area_id').annotate(booked_count=models.Count('area_id'))
    
    
    data = {}
    for area_data in area_bookings:
        area_id = area_data['area_id']
        booked_count = area_data['booked_count']
        data[area_id] = booked_count
    
    return JsonResponse(data)



def get_reservebooking_info(request):
    
    try:
        booking = Booking.objects.get(reference_number='A2392')
        booking_info = {
            'reference_number': booking.reference_number,
            'area_id': booking.area_id,
            'date': booking.date.strftime('%Y-%m-%d'),
            'start_time': booking.start_time.strftime('%H:%M'),
            'end_time': booking.end_time.strftime('%H:%M'),
            
        }
        return JsonResponse(booking_info)
    except Booking.DoesNotExist:
        return JsonResponse({'error': 'Booking not found'}, status=404)




def get_calendar_data(request):
    area_data = Booking.objects.values('date', 'area_id', 'start_time', 'end_time')

    availability = defaultdict(lambda: defaultdict(int))

    events = []
    for booking in area_data:
        date = booking['date']
        area_id = booking['area_id']
        start_time = booking['start_time']
        end_time = booking['end_time']
        availability[date][area_id] += 1
        
        events = []
        for date, areas in availability.items():
         for area_id, booked_count in areas.items():
            events.append({
                'title': f'{area_id}({booked_count})',
                'start': date,
                'start_time': start_time,  
                'end_time': end_time,
            })

    return JsonResponse(events, safe=False)

class ActiveBookingController(LoginRequiredMixin, View):
    
    login_url = 'userlogin'
    
    def get(self, request):
        
        booking = Booking.objects.get(user_id=request.user.username)
        if(booking.status == "Pending"):
            area_id = booking.reference_number
            context = {
                'area_id': area_id[:2],
                'reference_number': booking.reference_number,
                'date': booking.date,
                }
            return render(request, "wil/activebooking.html", context)
        else:
            return render(request, "wil/location.html")


area_button_click = facility_controller.areaButtonClick
insert_into_database = facility_controller.insertIntoAssignedAreaModel
hideMessage = facility_controller.hideMessage
handleYesButtonClick = facility_controller.handleYesButtonClick






