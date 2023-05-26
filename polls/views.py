import random
from django.db import connection

from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from polls.models import Reference
from wiladmin.models import WalkinBooking
from datetime import datetime


def index(request):
    return render(request, "wil/base.html", {})


def area_button_click(request):
    
    cursor = connection.cursor()
    
    area_id = request.GET.get('area_id')

    # Generate the reference number here
    reference_number = generate_reference_number(area_id)

    # Insert the reference number and area ID into the database
    reference = Reference(reference_number=reference_number, area_id=area_id)
    reference.save()
    
    user_id = '18-0107-262'
    schedule = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    status = "Pending"
    
    cursor.execute("INSERT INTO wiladmin_walkinbooking (referenceid, userid, schedule, status) VALUES ('"+reference_number+"', '"+user_id+"','"+schedule+"','"+status+"');")

    # Return the response with the reference number
    return JsonResponse({'reference_number': reference_number})

def generate_reference_number(area_id):
    reference_number = area_id.upper() + str(random.randint(100, 999))
    return reference_number


def location(request):
    return render(request, "wil/location.html", {})


def timer(request):
    return render(request, "wil/timer.html", {})


def timer_view(request):
    return render(request, 'timer.html')


@csrf_exempt
def insert_into_database(request):
    if request.method == 'POST':
        area_id = request.POST.get('area_id')
        reference_number = request.POST.get('reference_number')

        # Insert the reference number and area ID into the database
        reference = Reference(reference_number=reference_number, area_id=area_id)
        reference.save()

        # Return the response
        return JsonResponse({'message': 'Data inserted into the database.'})

    # Return an error response for other request methods
    return JsonResponse({'error': 'Invalid request method.'}, status=400)












