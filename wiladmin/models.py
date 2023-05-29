from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20);
    password = models.CharField(max_length=20);
    type = models.CharField(max_length=10);
        
    def __str__(self):
        return self.username;
    
    def getUserDetails(self):
        return self.username, self.password, self.type;
    
    def createUser(self):
        self.save();
        
    def deleteUser(self):
        self.delete();
    
class WalkinBooking(models.Model):
    bookingid = models.AutoField(primary_key=True);
    referenceid = models.CharField(max_length=20);
    userid = models.CharField(max_length=20);
    schedule = models.CharField(max_length=20);
    status = models.CharField(max_length=20);
        
    def __str__(self):
        return self.userid+"-"+self.referenceid;

    def getWalkinBookingDetails(self):
        return self.bookingid, self.referenceid, self.userid, self.schedule, self.status;
    
    def getWalkingBookings(self):
        return self.bookingid, self.referenceid, self.userid, self.schedule, self.status;
    
    def createWalkinBooking(self):
        self.save();
        
    def deleteWalkinBooking(self):
        self.delete();
    
class Logs(models.Model):
    logid = models.AutoField(primary_key=True);
    referenceid = models.CharField(max_length=20);
    userid = models.CharField(max_length=20);
    datetime = models.CharField(max_length=20);
    status = models.CharField(max_length=20);
        
    def __str__(self):
        return self.userid+"-"+self.referenceid+"-"+self.status;
    
    def getLogDetails(self):
        return self.logid, self.referenceid, self.userid, self.datetime, self.status;
    
    def deleteLogs(self):
        self.delete();