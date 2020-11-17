from django.shortcuts import render


def home(request):
    return render(request, 'webapp/home.html')


def results(request):
    return render(request, 'webapp/results.html')