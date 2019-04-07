from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def index(request):
    langs = Language.objects.all()
    return render(request,'languages_home.html', {'title': 'Languages Home', 'langs': langs})

