from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "wil/index.html", {})
def index(request):
    return render(request, "wil/base.html", {})

def adminlogin(request):
    return render(request, "wiladmin/login.html", {})
def admindashbaord(request):
    return render(request, "wiladmin/dashboard.html", {})
def walkindashboard(request):
    return render(request, "wiladmin/walkindashboard.html", {})


