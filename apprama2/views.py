import re

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def vista1(request):
    return render(request, "apprama2/vistarama1.html")

def vista2(request):
    return render(request, "apprama2/vistarama2.html")