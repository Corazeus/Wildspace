import csv
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import WalkinBooking, AdminReportLogs
from django.views import View
from datetime import datetime

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

class AdminDashboardController(View):
    def get(self, request):
        return render(request, "wiladmin/dashboard.html", {})

class AdminWalkinDashboardController(View):
    
    def updateBookingStatus(self, bookingid):
        booking = WalkinBooking.objects.get(pk=int(bookingid))
        
        if(booking.status == "Pending"):
            booking.status = 'Booked'
            booking.save()
            log = AdminReportLogs(referenceid = booking.referenceid, userid = booking.userid, datetime = booking.schedule, status = booking.status)
            log.save()
        
        else:
            booking.delete()
            log = AdminReportLogs(referenceid = booking.referenceid, userid = booking.userid, datetime = booking.schedule, status = 'Logged Out')
            log.save()
            
    def get(self, request):
        bookings = WalkinBooking.objects.all().order_by('-status','-bookingid')
        return render(request, "wiladmin/walkindashboard.html", {'bookings': bookings})
    
    def post(self, request, bookingid):

        self.updateBookingStatus(bookingid)
        
        return redirect('walkindashboard')
        
class AdminReportLogsController(View):

    def exportlogs(self, request):
        
        logs = AdminReportLogs.objects.all()
        
        if logs.count() == 0:
            
            messages.error(request, "No Logs Found")
            return render(request, "wiladmin/logs.html", {'logs': logs})
            
        else:
            response = HttpResponse(content_type="text/csv")
            response['Content-Disposition'] = 'attachment; filename=WILReportLogs '+str(datetime.now().strftime("%d/%m/%Y"))+'.csv'

            writer = csv.writer(response)
            writer.writerow(['Log Number','Reference ID','User ID','Date and Time','Status'])

            for log in logs:
                writer.writerow([log.logid, log.referenceid, log.userid, log.datetime, log.status])

            cursor = connection.cursor()
            cursor.execute("DELETE FROM wiladmin_AdminReportLogs")

            return response
    
    def getAllReportLogs(self):
        logs = AdminReportLogs.objects.all().order_by('-logid')
        return logs
    
    def get(self, request):
        logs = self.getAllReportLogs
        return render(request, "wiladmin/logs.html", {'logs': logs})
    
    def post(self, request):
        return self.exportlogs(request)
        
class BookGuestController(View):
    
    def CreateNewBooking(self):
        referenceid = 'GUEST'
        userid = '18-0107-262'
        schedule = str(datetime.now().strftime("%d/%m/%Y, %H:%M"))
        status = 'Pending'
        booking = WalkinBooking(referenceid = referenceid, userid = userid, schedule = schedule, status = status)
        booking.save()
    
    def get(self, request):
        return render(request, 'wiladmin/bookguest.html',{})
    
    def post(self, rquest):
        self.CreateNewBooking()
        return redirect('bookguest')