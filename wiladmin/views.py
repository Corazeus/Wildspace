from django.shortcuts import render

# Create your views here.
def adminlogin(request):
    return render(request, "wiladmin/login.html", {})
def admindashbaord(request):
    return render(request, "wiladmin/dashboard.html", {})
def walkindashboard(request):
    return render(request, "wiladmin/walkindashboard.html", {})