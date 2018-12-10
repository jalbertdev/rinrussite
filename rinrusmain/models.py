from django.db import models
from django.contrib.auth.models import User
from datetime import datetime  

class Simulation(models.Model):
	unProcessedPDBURL = models.CharField(max_length=100)
	idNumber=models.IntegerField(default=0)
	valid=models.BooleanField(default=False) 
	dateRan=models.DateTimeField(default=datetime.now, blank=True)
	residue=models.CharField(max_length=100)
	chain=models.CharField(max_length=100)
	simName=models.CharField(max_length=100)
	
