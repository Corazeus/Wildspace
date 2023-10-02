from datetime import datetime
import random
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from polls.models import AssignedArea
from wiladmin.models import WalkinBookingModel

class FacilityMapController:
    @csrf_exempt
    def showMessage(self, request):
        request.POST.get('popupMessage')
        request.POST.get('popupText')
        request.POST.get('buttonContainer')
        request.POST.get('referenceContainer')

    
        return JsonResponse({'message': 'Show message operation completed.'})

    def areaButtonClick(self, request):

        area_id = request.GET.get('area_id')

        reference_number = self.generateReferenceNumber(area_id)

        reference = AssignedArea(reference_number=reference_number, area_id=area_id)
        reference.save()

        user_id = request.user.username
        schedule = datetime.now().strftime("%d/%m/%Y, %H:%M")
        status = "Pending"
        
        booking = WalkinBookingModel(referenceid = reference_number, userid=user_id, schedule=schedule, status=status)
        booking.save()

        return JsonResponse({'reference_number': reference_number})

    def generateReferenceNumber(self, area_id):
        reference_number = area_id.upper() + str(random.randint(100, 999))
        return reference_number

    @csrf_exempt
    def insertIntoAssignedAreaModel(self, request):
        if request.method == 'POST':
            area_id = request.POST.get('area_id')
            reference_number = self.generateReferenceNumber(area_id)

            reference = AssignedArea(reference_number=reference_number, area_id=area_id)
            reference.save()

            return JsonResponse({'message': 'Data inserted into the database.'})

        return JsonResponse({'error': 'Invalid request method.'}, status=400)

    @csrf_exempt
    def hideMessage(self, request):
        request.POST.get('popupMessage')

        
        return JsonResponse({'message': 'Hide message operation completed.'})

    @csrf_exempt
    def handleYesButtonClick(self, request):
        request.POST.get('referenceContainer')
        request.POST.get('referenceNumber')
        areaId = request.POST.get('areaId')
        selectedAreaId = request.POST.get('selectedAreaId')

        if selectedAreaId == areaId:
            request.POST.get('buttonContainer')
            request.POST.get('yesButton')
            request.POST.get('noButton')

            

            return JsonResponse({'message': 'Handle yes button click operation completed.'})

        return JsonResponse({'message': 'Handle yes button click operation failed.'})
