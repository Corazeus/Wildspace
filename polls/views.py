from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "wil/index.html", {})
def index(request):
    return render(request, "wil/base.html", {})


