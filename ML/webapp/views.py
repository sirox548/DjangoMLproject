from django.shortcuts import render, redirect
from .models import Description
from .forms import JobForm


def home(request):
    Jobs = Description.objects.all()
    form = JobForm()

    context = {'Jobs': Jobs, 'form': form}
    return render(request, 'webapp/home.html', context)


def results(request):
    return render(request, 'webapp/results.html')


def predict():
    qs = Description.objects.all()
    df = qs.to_dataframe()
    df = qs.to_dataframe(fieldnames=['description'])
    return df
