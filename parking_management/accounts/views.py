from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.contrib.auth import logout
from django.contrib import auth

# Create your views here.
from django.contrib import auth

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print('Login is successful...!')
            return redirect('showvehicle')
        else:
            print('Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def log_out(request):
    logout(request)
    return redirect('login')




