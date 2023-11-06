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


class Timer(models.Model):
    minutes = models.IntegerField(default=30)
    seconds = models.IntegerField(default=0)
    session_ended = models.BooleanField(default=False)
    user_id = models.CharField(primary_key=True, max_length=20)

    def __str__(self):
        return "Timer for User ID {self.user_id}"


class Booking(models.Model):
    reserved_id = models.AutoField(primary_key=True)
    reference_number = models.CharField(max_length=10)
    area_id = models.CharField(max_length=5)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    user_id = models.CharField(max_length=20)
    status = models.CharField(max_length=20)








