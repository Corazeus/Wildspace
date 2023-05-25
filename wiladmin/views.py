from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User, WalkinBooking
from django.views import View

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
    
class walkindashboard(View):
    
    def get(self, request):
        bookinglist = WalkinBooking.objects.all().order_by('-status')
        return render(request, "wiladmin/walkindashboard.html", {'bookinglist': bookinglist})