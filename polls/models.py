from django.db import models



class AssignedArea(models.Model):
    reference_number = models.CharField(max_length=100)
    area_id = models.CharField(max_length=100)













