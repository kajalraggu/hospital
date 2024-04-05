from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def check(request):
    return render(request, 'check.html')
