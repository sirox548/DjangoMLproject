from django.shortcuts import render, redirect
from .models import Description
from .forms import JobForm

# ML Libraries
import numpy as np
# from django_pandas.managers import DataFrameManager


def home(request):
    Jobs = Description.objects.all()
    form = JobForm()

    context = {'Jobs': Jobs, 'form': form}
    return render(request, 'webapp/home.html', context)


def results(request):
    form = JobForm()
    context = {'form': form}
    return render(request, 'webapp/results.html', context)


def getPredictions():

    pass

