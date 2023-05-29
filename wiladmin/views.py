import csv
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from .models import WalkinBooking, Logs
from django.views import View
from datetime import datetime
    
class walkindashboard(View):
    
    def get(self, request):
        bookings = WalkinBooking.objects.all().order_by('-status')
        return render(request, "wiladmin/walkindashboard.html", {'bookings': bookings})
    
    def post(self, request, bookingid):
        
        cursor = connection.cursor()
        booking = WalkinBooking.objects.get(pk=int(bookingid))
        
        if(booking.status == "Pending"):
            booking.status = 'Booked'
            booking.save()
            
            cursor.execute("INSERT INTO wiladmin_logs (referenceid, userid, datetime, status) VALUES ('"+booking.referenceid+"', '"+booking.userid+"','"+booking.schedule+"', 'Booked');")
            return redirect('walkindashboard')
        else:
            booking.delete()
            
            date_time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            
            cursor.execute("INSERT INTO wiladmin_logs (referenceid, userid, datetime, status) VALUES ('"+booking.referenceid+"', '"+booking.userid+"','"+date_time+"', 'Logged Out');")
            return redirect('walkindashboard')
        
class reportlogs(View):
    
    def get(self, request):
        logs = Logs.objects.all().order_by('-logid')
        return render(request, "wiladmin/logs.html", {'logs': logs})
    
    
def exportlogs(request):
    
    request.session
    
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=WILReportLogs '+str(datetime.now().strftime("%d/%m/%Y"))+'.csv'
                
    writer = csv.writer(response)
    writer.writerow(['Log Number','Reference ID','User ID','Date and Time','Status'])
            
    logs = Logs.objects.all()
    for log in logs:
        writer.writerow([log.logid, log.referenceid, log.userid, log.datetime, log.status])
        
    cursor = connection.cursor()
    cursor.execute("DELETE FROM wiladmin_logs")
    
    return response

def admindashbaord(request):
    return render(request, "wiladmin/dashboard.html", {})

def adminlogin(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('admindashboard')
        else:
            messages.success(request, "Invalid Credentials")
            return redirect('adminlogin')
    
    else:
        return render (request, "wiladmin/login.html", {})
