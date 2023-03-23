from django.urls import path
from . import views #importing views from views module

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.aboutpage,name='aboutpage'),
    path('login/', views.loginpage, name='loginpage'),
    path('createaccount/', views.createaccountpage, name='createaccountpage'),
    path('admin_login', views.login_admin, name='login_admin'),
    path('adminhome', views.AdminHome, name='adminhome'),
    path('adminlogout', views.Logout_admin,name='adminlogout'),
    path('adminaddDoctor',views.adminaddDoctor, name='adminaddDoctor'),
    path('adminviewDoctor', views.adminviewDoctor,name = 'adminviewDoctor'),
    path('adminDeleteDoctor<int:pid><str:email>', views.admin_delete_doctor, name='admin_delete_doctor'),
    path('adminaddReceptionist', views.adminaddReceptionist, name='adminviewReceptionist'),
    path('adminDeleteReceptionist', views.adminviewReceptionist, name='adminaddReceptionist'),
    path('adminviewAppointment', views.adminviewAppointment, name='addviewAppointment'),
    path()
]