from django.shortcuts import render


def index(request):
    return render(request, 'employment_home.html', {'title': 'Employment Home'})
