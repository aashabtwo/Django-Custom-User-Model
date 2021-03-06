from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

def home(request):
    return render(request, 'users/home.html')
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}')
            return redirect(request, 'user-home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def loginUser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'LOGGED IN!')
            return redirect('user-home')
        else:
            messages.success(request, 'Username or password did not match')
    return render(request, 'users/login.html')
def logoutUser(request):
    logout(request)
    messages.success(request, 'Logged Out')
    return redirect('user-login')
    #return render(request, 'users/register.html')

@login_required
def profile(request):
    return render(request, 'users/profile.html')