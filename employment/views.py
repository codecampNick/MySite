from django.shortcuts import render
from .models import *


def index(request):
    employers = Company.objects.all().order_by('-start_date')
    accomplishments = Accomplishments.objects.all()
    return render(request, 'employment_home.html',
                  {'title': 'Employment Home',
                   'employers': employers,
                   'accomplishments': accomplishments})
