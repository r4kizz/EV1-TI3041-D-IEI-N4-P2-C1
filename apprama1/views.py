from django.shortcuts import render

def vista1(request):
    return render(request, "apprama1/vistarama1.html")

def vista2(request):
    return render(request, "apprama1/vistarama2.html")
