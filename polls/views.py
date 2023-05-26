import random

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from polls.models import Reference


def index(request):
    return render(request, "wil/base.html", {})


def area_button_click(request):
    area_id = request.GET.get('area_id')

    # Generate the reference number here
    reference_number = generate_reference_number(area_id)

    # Insert the reference number and area ID into the database
    reference = Reference(reference_number=reference_number, area_id=area_id)
    reference.save()

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












