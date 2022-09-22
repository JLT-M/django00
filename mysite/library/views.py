from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Labas, pasauli! 'Library' Django appsas!")

# Create your views here.
