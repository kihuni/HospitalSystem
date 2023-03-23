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
    page = ''
    if request.method == 'POST':
         u = request.POST['email']
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
                   elif g == 'Patient':
                        page = 'patient'
                        d = {'error': error, 'page':page}
                        return render(request, 'patienthome.html',d)
              else:
                   error ='yes'
         except Exception as e:
              error = 'yes'
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
                       pat_group = Group.objects.get(name='Patient')
                       pat_group.user_set.add(user)
                       user.save()
                       error = 'no'
                  else:
                       error = 'yes'
             except:
                  error = 'yes'
             d = {'error': error}
        return render(request, 'createaccount.html',d)

## logic for Doctor
def adminaddDoctor(request):
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
                       pat_group = Group.objects.get(name='Doctor')
                       pat_group.user_set.add(user)
                       user.save()
                       error = 'no'
                  else:
                       error = 'yes'
             except:
                  error = 'yes'
             d = {'error': error}
        return render(request, 'adminadddoctor.html',d)

def adminviewDoctor(request):
     if not request.user.is_staff:
          return redirect('login_admin') 
     doc = Doctor.objects.all()
     d = {'doc':doc}
     return render(request, 'adminviewDoctors.html',d)

def admin_delete_doctor(request,pid,email):
     if not request.user.is_staff:
          return redirect('login_admin')
     doctor = Receptionist.objects.get(id=pid)
     doctor.delete()
     users = User.objects.filter(username=email)
     users.delete()
     return redirect('adminviewDoctor')

## logic for receptionist

def adminaddReceptionist(request):
        error = ''
        if not request.user.is_staff:
             return redirect('login_admin')
        
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
                       pat_group = Group.objects.get(name='Receptionist')
                       pat_group.user_set.add(user)
                       user.save()
                       error = 'no'
                  else:
                       error = 'yes'
             except:
                  error = 'yes'
             d = {'error': error}
        return render(request, 'adminaddreceptionist.html',d)

def adminviewReceptionist(request):
     if not request.user.is_staff:
          return redirect('login_admin') 
     rec = Receptionist.objects.all()
     r = {'rec':rec}
     return render(request, 'adminviewreceptionists.html',r)

def admin_delete_receptionist(request,pid,email):
     if not request.user.is_staff:
          return redirect('login_admin')
     reception = Receptionist.objects.get(id=pid)
     reception.delete()
     users = User.objects.filter(username=email)
     users.delete()
     return redirect('adminviewReceptionist')


def adminviewAppointment(request):
     if not request.user.is_staff:
          return redirect('login_admin')
     return render(request, 'adminviewappointments.html')

def Logout(request):
     if not request.user.is_active:
          return redirect('loginpage')
     logout(request)
     return redirect('loginpage')

def Logout_admin(request):
     if not request.user.is_staff:
          return redirect('login_admin')
     logout(request)
     return redirect('login_admin')

def AdminHome(request):
     if not request.user.is_staff:
          return redirect('login_admin')
     return render(request, 'adminhome.html')

def Home(request):
     if not request.user.is_active:
          return redirect('loginpage')
     g = request.user.groups.all()[0].name
     if g == 'Doctor':
        return render(request, 'doctorhome.html')
     elif g == 'Receptionist':
          return render(request, 'receptionhome.html')
     elif g == 'Patient':
          return render(request, 'patienthome.html')


def profile(request):
     if not request.user.is_active:
          return redirect('loginpage')
     g = request.user.groups.all()[0].name
     if g == 'Patient':
          Patient_details = Patient.objects.all().filter(email = request.user)
          d = {'patient_details': Patient_details}
          return render(request, 'patientprofile.html',d)
     elif g == 'Doctor':
          doctor_details = Doctor.objects.all().filter(email = request.user)
          d = {'doctor_details' : doctor_details}
          return render(request, 'doctorprofile.html', d)
     elif g == 'Receptionist':
          receptionist_details = Receptionist.objects.all().filter(email = request.user)
          d = {'receptionist_details': receptionist_details}
          return render(request, 'receptionistprofile.html',d)
     
     def MakeAppoitments(request):
          error = ''
          if not request.user.is_active:
               return redirect('loginpage')
          alldoctors = Doctor.objects.all()
          d = { 'alldoctors': alldoctors}
          g = request.user.groups.all()[0].name