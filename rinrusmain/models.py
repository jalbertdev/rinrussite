from django.db import models
from django.contrib.auth.models import User

class Simulation(models.Model):
	unProcessedPDB = models.CharField(max_length=100)
	idNumber=models.IntegerField(default=0)
	valid=models.BooleanField() #add default to false
	dateRan=models.DateTimeField()
	simValues=models.CharField(max_length=100)
	simName=models.CharField(max_length=100)
	
