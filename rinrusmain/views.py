from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Simulation
from django.urls import reverse
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.core.files import File
import datetime

from . import models

def index(request):
	if request.method == 'POST' and request.FILES['myfile']:
		myfile = request.FILES['myfile']
		folder='rinrusmain\\static\\files\\'+request.POST["jobName"] + '\\'
		fs = FileSystemStorage(location=folder) 
		try:
			if myfile.content_type == 'application/octet-stream':
					  chainTemp=request.POST["row1"]+request.POST["row2"]+request.POST["row3"]+request.POST["row4"]+request.POST["row5"]
					  residueTemp=request.POST["text1"]+"|"+request.POST["text2"]+"|"+request.POST["text3"]+"|"+request.POST["text4"]+"|"+request.POST["text5"]+"|"
					  fileName=request.POST["jobName"]+".pdb"
					  filename = fs.save(fileName, myfile)
					  uploaded_file_url = '\\'+request.POST["jobName"] + '\\'+fs.url(filename)
					  temp_obj=Simulation(unProcessedPDBURL=uploaded_file_url,residue=residueTemp.split('|'),chain=[str(i) for i in chainTemp],simName=request.POST["jobName"])
					  temp_obj.save()
					  return render(request, 'rinrusmain/index.html', {'uploaded_file_url': uploaded_file_url})
			else:   
					  return render(request, 'rinrusmain/index.html',{'uploaded_file_error': "Improper file type"})
		except:
			return render(request, 'rinrusmain/index.html',{'uploaded_file_error': "Model failed to create"})
	return render(request,'rinrusmain/index.html')

	
def search(request):
	return render(request,'rinrusmain/search.html')

	
def results(request):
	if request.method == 'GET':
		text=request.GET.get('textField', None)
		type=request.GET.get('searchType', None)
		date=request.GET.get('date',None)
		print(text)
		print(type)
		simulations=[]
		if(type=="Show All"):
			print("did it")
			simulations = list(models.Simulation.objects.all())
		print(simulations)
		return render(request,'rinrusmain/results.html',{'simulations' : simulations})
		
def sim_page(request,sim_ID):
	print("dog")
	model=Simulation.objects.filter(idNumber=sim_ID).first()
	
	unProcFile  = open(settings.MEDIA_ROOT+ model.unProcessedPDBURL, "r") 
	unProcFile = File(unProcFile)

	
	print("DOG HERE")
	return render(request,'rinrusmain/sim_page.html',{'simulation' : model}) 

		
def about(request):
        return render(request,'rinrusmain/about.html')


