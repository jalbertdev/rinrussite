from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Simulation
from django.urls import reverse
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from django.conf import settings


def index(request):
        if request.method == 'POST' and request.FILES['myfile']:
                myfile = request.FILES['myfile']
                fs = FileSystemStorage()
                try:
                        if myfile.content_type == 'application/octet-stream':
                                chainTemp=request.POST["row1"]+request.POST["row2"]+request.POST["row3"]+request.POST["row4"]+request.POST["row5"]
                                residueTemp=request.POST["text1"]+"|"+request.POST["text2"]+"|"+request.POST["text3"]+"|"+request.POST["text4"]+"|"+request.POST["text5"]+"|"
                                fileName=request.POST["jobName"]+".pdb"
                                filename = fs.save(fileName, myfile)
                                uploaded_file_url = fs.url(filename)
                                temp_obj=Simulation(unProcessedPDBURL=uploaded_file_url,residue=residueTemp,chain=chainTemp,simName=request.POST["jobName"])
                                temp_obj.save()
                                return render(request, 'rinrusmain/index.html', {'uploaded_file_url': uploaded_file_url})
                        else:   
                                return render(request, 'rinrusmain/index.html',{'uploaded_file_error': "Improper file type"})
                except:
                       return render(request, 'rinrusmain/index.html',{'uploaded_file_error': "Model failed to create"})
        return render(request,'rinrusmain/index.html')
	
def about(request):
        return render(request,'rinrusmain/about.html')


