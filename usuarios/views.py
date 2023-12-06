from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm


def registro(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'registration/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Credenciales inválidas. Por favor, inténtalo de nuevo.')
        else:
            messages.error(request, 'Corrige los errores del formulario.')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})

def exit(request):
    logout(request)
    return redirect('home')
