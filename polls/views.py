import random

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import polls
from polls.models import Reference
from wiladmin.models import WalkinBooking


def index(request):
    return render(request, "wil/base.html", {})


def area_button_click(request):
    area_id = request.GET.get('area_id')


    reference_number = generate_reference_number(area_id)


    reference = Reference(reference_number=reference_number, area_id=area_id)
    reference.save()


    return JsonResponse({'reference_number': reference_number})


def generate_reference_number(area_id):
    reference_number = area_id.upper() + str(random.randint(100, 999))
    return reference_number


def location(request):
    try:
        reference = Reference.objects.latest('id')
        area_id = reference.area_id
    except Reference.DoesNotExist:
        area_id = None

    context = {
        'area_id': area_id,
    }

    return render(request, "wil/location.html", context)


def timer(request):
    return render(request, "wil/timer.html", {})
def login(request):
    return render(request, "wil/login.html", {})


def timer_view(request):
    return render(request, 'timer.html')


@csrf_exempt
def insert_into_database(request):
    if request.method == 'POST':
        area_id = request.POST.get('area_id')
        reference_number = request.POST.get('reference_number')


        reference = Reference(reference_number=reference_number, area_id=area_id)
        reference.save()


        return JsonResponse({'message': 'Data inserted into the database.'})


    return JsonResponse({'error': 'Invalid request method.'}, status=400)


def timer(request):

    walkinbooking = WalkinBooking.objects.latest('bookingid')
    reference = Reference.objects.latest('id')


    context = {
        'id_number': walkinbooking.userid if walkinbooking else 'N/A',
        'booking_reference_number': walkinbooking.referenceid if walkinbooking else 'N/A',
        'assigned_area': reference.area_id if reference else 'N/A',
        'date_of_use': walkinbooking.schedule if walkinbooking else 'N/A',
    }

    return render(request, "wil/timer.html", context)












