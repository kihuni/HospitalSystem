from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth, Group
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.utils import timezone
from .models import *

# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def aboutpage(request):
    return render(request, 'about.html')

def loginpage(request):
    return render(request, 'login.html')

def createaccountpage(request):
    return render(request, 'createaccount.html')

def login_admin(request):
    return render(request, 'admin_login')