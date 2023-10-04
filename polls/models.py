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

from django.db import models

class Timer(models.Model):
    userid = models.CharField(primary_key=True, max_length=20);
    minutes = models.IntegerField(default=30)
    seconds = models.IntegerField(default=0)
    session_ended = models.BooleanField(default=False)

    def update_timer(self):
        if not self.session_ended:
            if self.seconds > 0:
                self.seconds -= 1
            elif self.minutes > 0:
                self.minutes -= 1
                self.seconds = 59
            else:
                self.session_ended = True

    def reset_timer(self):
        self.minutes = 30
        self.seconds = 0
        self.session_ended = False








