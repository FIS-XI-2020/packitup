from django.db import models

# Create your models here.
class FlightDetails(models.Model):
    From=models.CharField(max_length=50)
    To=models.CharField(max_length=50)
    FlightNo=models.CharField(max_length=50)
    FlightName=models.CharField(max_length=50)
    NoOfSeats=models.IntegerField()
    Class=models.CharField(max_length=50)
    Time=models.TimeField(max_length=50)
    
    
