from django.db import models

# Create your models here.
class AdminAccount(models.Model):
    username = models.CharField(max_length=20);
    password = models.CharField(max_length=20);
        
    def __str__(self):
        return self.username;
    
class WalkinBooking(models.Model):
    bookingid = models.AutoField(primary_key=True);
    referenceid = models.CharField(max_length=20);
    userid = models.CharField(max_length=20);
    schedule = models.CharField(max_length=20);
    status = models.CharField(max_length=20);
        
    def __str__(self):
        return self.userid+"-"+self.referenceid;
    
class AdminReportLogs(models.Model):
    logid = models.AutoField(primary_key=True);
    referenceid = models.CharField(max_length=20);
    userid = models.CharField(max_length=20);
    datetime = models.CharField(max_length=20);
    status = models.CharField(max_length=20);
        
    def __str__(self):
        return self.userid+"-"+self.referenceid+"-"+self.status;
