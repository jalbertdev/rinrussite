from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
#from .models import Choice, Question
from django.urls import reverse
from django.utils import timezone


def index(request):
	return render(request,'rinrusmain/index.html')

