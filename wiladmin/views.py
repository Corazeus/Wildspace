from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
#def adminlogin(request):
#    return render(request, "wiladmin/login.html", {})

def admindashbaord(request):
    return render(request, "wiladmin/dashboard.html", {})

def walkindashboard(request):
    return render(request, "wiladmin/walkindashboard.html", {})

def adminlogin(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, "Invalid Username or Password")
            return redirect('adminlogin')
    
    else:
        return render (request, "wiladmin/login.html", {})