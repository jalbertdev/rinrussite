from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
#from .models import Choice, Question
from django.urls import reverse
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from django.conf import settings


def index(request):
        if request.method == 'POST' and request.FILES['myfile']:
                myfile = request.FILES['myfile']
                fs = FileSystemStorage()
                if myfile.content_type == 'application/octet-stream':
                        fileName=request.POST["jobName"]+"'"+request.POST["row1"]+".pdb"
                        filename = fs.save(fileName, myfile)
                        uploaded_file_url = fs.url(filename)
                        return render(request, 'rinrusmain/index.html', {'uploaded_file_url': uploaded_file_url})
                else:
                        return render(request, 'rinrusmain/index.html',{'uploaded_file_error': True})
        return render(request,'rinrusmain/index.html')
	
def about(request):
        return render(request,'rinrusmain/about.html')


