from django.urls import path
from . import views #importing views from views module

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.aboutpage,name='aboutpage'),
    path('login/', views.loginpage, name='loginpage'),
    path('createaccount/', views.createaccountpage, name='createaccountpage'),
    path('admin_login', views.login_admin, name='login_admin')
]