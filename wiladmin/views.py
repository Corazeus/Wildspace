import csv
import random
from django.db import connection
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import WalkinBookingModel, AdminReportLogsModel
from polls.models import Timer, AssignedArea, Booking
from django.views import View
from datetime import datetime
from .forms import BookGuest

class AdminLoginController(View):
    
    def handleLogin(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admindashboard')
        else:
            messages.error(request, 'Invalid Username or Password')
            return redirect('adminlogin')
        
    def get(self, request):
        return render(request, "wiladmin/login.html", {})
    
    def post(self, request):
        return self.handleLogin(request)

class AdminDashboardController(LoginRequiredMixin, View):
    
    login_url = 'adminlogin'
    
    def get(self, request):
        return render(request, "wiladmin/admindashboard.html", {})

class AdminWalkinDashboardController(LoginRequiredMixin, View):
    
    login_url = 'adminlogin'
    
    def updateBookingStatus(self, bookingid):
        booking = WalkinBookingModel.objects.get(pk=int(bookingid))
        try:
            if booking.status == "Pending":
                booking.status = 'Booked'
                booking.save()
                
                timer = Timer(user_id=booking.userid, minutes=30, seconds=0)
                timer.save()
                
                log = AdminReportLogsModel(referenceid=booking.referenceid, userid=booking.userid, starttime=booking.schedule, endtime="", status='Booked')
                log.save()
            
            else:
                booking.delete()
                
                usertimer = Timer.objects.get(pk=str(booking.userid))
                usertimer.delete()
                
                assignedarea = AssignedArea.objects.all().filter(reference_number=booking.referenceid)
                assignedarea.delete()
                
                log = AdminReportLogsModel(referenceid=booking.referenceid, userid=booking.userid, starttime=booking.schedule,endtime=str(datetime.now().strftime("%d/%m/%Y, %H:%M")), status='Logged Out')
                log.save()
                
        except Timer.DoesNotExist:
            assignedarea = AssignedArea.objects.all().filter(reference_number=booking.referenceid)
            assignedarea.delete()
            log = AdminReportLogsModel(referenceid=booking.referenceid, userid=booking.userid, starttime=booking.schedule,endtime=str(datetime.now().strftime("%d/%m/%Y, %H:%M")), status='Logged Out')
            log.save()
            return redirect('walkindashboard')
        
    def get(self, request):
        bookings = WalkinBookingModel.objects.all().order_by('-status', '-bookingid')
        return render(request, "wiladmin/walkindashboard.html", {'bookings': bookings})
    
    def post(self, request, bookingid):
        self.updateBookingStatus(bookingid)
        return redirect('walkindashboard')
    

class AdminReservedDashboardController(LoginRequiredMixin, View):
    
    login_url = 'adminlogin'
    
    def updateBookingStatus(self, reserved_id):
        booking = Booking.objects.get(pk=int(reserved_id))
        
        if booking.status == "Pending":
            booking.status = 'Booked'
            booking.save()
            
            timer = Timer(user_id=booking.user_id, minutes=60, seconds=0)
            timer.save()
            
            log = AdminReportLogsModel(referenceid=booking.reference_number, userid=booking.user_id, starttime=booking.start_time, endtime="", status='Booked')
            log.save()
        
        else:
            booking.delete()
            
            usertimer = Timer.objects.get(pk=str(booking.user_id))
            usertimer.delete()
            
            assignedarea = AssignedArea.objects.all().filter(reference_number=booking.reference_number)
            assignedarea.delete()
            
            log = AdminReportLogsModel(referenceid=booking.reference_number, userid=booking.user_id, starttime=booking.start_time, endtime=str(datetime.now().strftime("%d/%m/%Y, %H:%M")), status='Logged Out')
            log.save()
    
    def get(self, request):
        bookings = Booking.objects.all().order_by('-status')
        return render(request, "wiladmin/reserveddashboard.html", {'bookings': bookings})
    
    def post(self, request, reserved_id):
        self.updateBookingStatus(reserved_id)
        return redirect('reserveddashboard')
    
        
class AdminReportLogsController(LoginRequiredMixin,View):
    
    login_url = 'adminlogin'

    def exportlogs(self, request):
        
        logs = AdminReportLogsModel.objects.all()
        
        if logs.count() == 0:
            
            messages.error(request, "No Logs Found")
            return render(request, "wiladmin/logs.html", {'logs': logs})
            
        else:
            response = HttpResponse(content_type="text/csv")
            response['Content-Disposition'] = 'attachment; filename=WILReportLogs '+str(datetime.now().strftime("%d/%m/%Y"))+'.csv'

            writer = csv.writer(response)
            writer.writerow(['Log Number','Reference ID','User ID','Date and Time','Status'])

            for log in logs:
                writer.writerow([log.logid, log.referenceid, log.userid, log.starttime, log.status])

            cursor = connection.cursor()
            cursor.execute("DELETE FROM wiladmin_AdminReportLogsModel")

            return response
    
    def getAllReportLogs(self):
        logs = AdminReportLogsModel.objects.all().order_by('-logid')
        return logs
    
    def get(self, request):
        logs = self.getAllReportLogs
        return render(request, "wiladmin/logs.html", {'logs': logs})
    
    def post(self, request):
        return self.exportlogs(request)
        
class BookGuestController(LoginRequiredMixin, View):
    
    login_url = 'adminlogin'
    
    def CreateNewBooking(self):
        referenceid = 'GUEST'
        userid = '18-0107-262'
        schedule = str(datetime.now().strftime("%d/%m/%Y, %H:%M"))
        status = 'Pending'
        booking = WalkinBookingModel(referenceid = referenceid, userid = userid, schedule = schedule, status = status)
        booking.save()
    
    def get(self, request):
        return render(request, 'wiladmin/bookguest.html',{})
    
    def post(self, request):
        form = BookGuest(request.POST)
        
        if form.is_valid():
            referenceid = 'A'+str(random.randint(3, 9))+'GUEST'.upper()
            userid = request.POST.get('userid')
            schedule = str(datetime.now().strftime("%d/%m/%Y, %H:%M"))
            status = 'Booked'
            booking = WalkinBookingModel(referenceid = referenceid, userid = userid, schedule = schedule, status = status)
            booking.save()
            
            reference = AssignedArea(reference_number=referenceid, area_id=referenceid[:2])
            reference.save()
            
            log = AdminReportLogsModel(referenceid=booking.referenceid, userid=booking.userid, starttime=booking.schedule, endtime="", status='Booked')
            log.save()
        return redirect('bookguest')
    
class ViewWorkspacesController(LoginRequiredMixin, View):
    
    login_url = 'adminlogin'
    
    #Thsi will GET current count
    def GetAreaCount(self):
        countA1 = AssignedArea.objects.filter(area_id='A1').count()
        countA2 = AssignedArea.objects.filter(area_id='A2').count()
        countA3 = AssignedArea.objects.filter(area_id='A3').count()
        countA4 = AssignedArea.objects.filter(area_id='A4').count()
        countA5 = AssignedArea.objects.filter(area_id='A5').count()
        countA6 = AssignedArea.objects.filter(area_id='A6').count()
        countA7 = AssignedArea.objects.filter(area_id='A7').count()
        countA8 = AssignedArea.objects.filter(area_id='A8').count()
        countA9 = AssignedArea.objects.filter(area_id='A9').count()
        
        area_count = [{
            'countA1':countA1, 
            'countA2':countA2, 
            'countA3':countA3, 
            'countA4':countA4, 
            'countA5':countA5,
            'countA6':countA6,
            'countA7':countA7,
            'countA8':countA8,
            'countA9':countA9,
            }]
        
        return area_count
    
    #This will JSON response the area count
    #This function will be called in urls.py (url: wiladmin/updateworkspaces)
    #Using the refresh.js this will be called in interval of 2 seconds
    #The refresh.js ajax will then replace the value with the new value
    #P.S. made it not nested array for easy access in ajax
    def update_workspaces(request):
        countA1 = AssignedArea.objects.filter(area_id='A1').count()
        countA2 = AssignedArea.objects.filter(area_id='A2').count()
        countA3 = AssignedArea.objects.filter(area_id='A3').count()
        countA4 = AssignedArea.objects.filter(area_id='A4').count()
        countA5 = AssignedArea.objects.filter(area_id='A5').count()
        countA6 = AssignedArea.objects.filter(area_id='A6').count()
        countA7 = AssignedArea.objects.filter(area_id='A7').count()
        countA8 = AssignedArea.objects.filter(area_id='A8').count()
        countA9 = AssignedArea.objects.filter(area_id='A9').count()
            
        area_count = {
            'countA1':countA1, 
            'countA2':countA2, 
            'countA3':countA3, 
            'countA4':countA4, 
            'countA5':countA5,
            'countA6':countA6,
            'countA7':countA7,
            'countA8':countA8,
            'countA9':countA9,
            }
        return JsonResponse({'area_count':area_count})
     
    def get(self, request):
        
        area_count = self.GetAreaCount

        return render(request, 'wiladmin/workspaces.html', {'area_count': area_count})
    
    def post(self, request, areaid):
        area_count = self.GetAreaCount
        area = WalkinBookingModel.objects.filter(referenceid__contains=areaid) #and Booking.objects.filter(reference_number__contains=areaid)
        return render(request, 'wiladmin/workspaces.html', {'area':area, 'area_count':area_count, 'area_id':areaid})

class TestController(View):
    
    def get(self, request):
        return render(request, 'wiladmin/test.html')
    
def handleLogout(request):
        logout(request)
        return redirect('adminlogin')
