from django.shortcuts import render
from .models import Description


def home(request):
    Jobs = Description.objects.all()
    context = {'Jobs': Jobs}
    return render(request, 'webapp/home.html', context)


def results(request):
    return render(request, 'webapp/results.html')