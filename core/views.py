from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def home(request):
    return render(request, 'index.html')


def munecos(request):
    return render(request, 'munecos.html')


@login_required
def usuario_info(request):
    return render(request, 'registration/usuario_info.html')
