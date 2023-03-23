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

def login_admin(request):
    error = ''
    if request.method == 'POST':
         u = request.POST['username']
         p = request.POST['password']
         user = authenticate(username=u,password=p)
         try:
              if user.is_staff:
                   login(request,user)
                   error = 'no'
              else:
                   error ='yes' 
         except:
              error = 'yes'
    d = {'error' : error}
    return render(request, 'adminlogin.html', d)
    

def loginpage(request):
    error = ''
    if request.method == 'POST':
         u = request.POST['username']
         p = request.POST['password']
         user = authenticate(username=u,password=p)
         try:
              if user is not None:
                   login(request,user)
                   error = 'no'
                   g = request.user.groups.all()[0].name
                   if g == 'Doctor':
                        page = 'doctor'
                        d = {'error': error,'page':page}
                        return render(request,'doctorhome.html',d)
                   elif g == 'Receptionist':
                        page = "reception"
                        d = {'error': error, 'page': page}
                        return render(request,'patienthome.html',d)
              else:
                   error ='yes'
         except:
              error = 'yes'
    d = {'error' : error}
    return render(request, 'login.html')

def createaccountpage(request):
        error = ''
        user ='none'
        if request.method == 'POST':
             name = request.POST['name']
             email = request.POST['email']
             password = request.POST['password']
             repeatpassword = request.POST['repeatpassword']
             gender = request.POST['gender']
             phonenumber = request.POST['phonenumber']
             address = request.POST['address']
             birthdate = request.POST['dateofbirth']
             bloodgroup =request.POST['bloodgroup']
             try:
                  if password == repeatpassword:
                       Patient.objects.create(name = name, email=email, password=password,gender=gender,phonenumber=phonenumber,address=address,birthdate=birthdate,bloodgroup=bloodgroup)
                       user = User.objects.create_user(first_name=name,email=email,password=password,gender=gender,phonenumber=phonenumber,address=address,birthdate=birthdate,bloodgroup=bloodgroup)


