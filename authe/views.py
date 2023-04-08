from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import BootstrapAuthenticationForm, BootstrapUserCreationForm


def signup(request):
    if request.method == 'POST':
        form = BootstrapUserCreationForm(request.POST)
        # form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Save personal information to user profile
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.save()
            return redirect('login')
    else:
        form = BootstrapUserCreationForm()
        # form = UserCreationForm()
    return render(request, 'authe/signup.html', {
        'form' : form
    })


def login(request):
    if request.method == 'POST':
        form = BootstrapAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('base')
    else:
        form = BootstrapAuthenticationForm()
    return render(request, 'authe/login.html', {
        'form': form
    })


def logout(request):
    auth_logout(request)
    return redirect('login')


