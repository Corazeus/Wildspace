from django.db import models




class AssignedArea(models.Model):
    reference_number = models.CharField(max_length=100)
    area_id = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.reference_number+" - "+self.area_id

class UserAccountModel(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
        
    def __str__(self):
        return self.username









