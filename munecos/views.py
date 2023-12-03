from django.shortcuts import render

def presentacion(request):
    return render(request, 'index.html')