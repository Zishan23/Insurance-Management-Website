from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    return render(request, 'beta/index.html')

def about(request):
    return HttpResponse('about')


def contact(request):
    return HttpResponse('contact')

