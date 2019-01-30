from django.urls import path
from accounts import views

urlpatterns = [
    path('login', views.LoginView, name='login'),                     
    path('register', views.RegisterView, name='register'),   
    path('logout', views.LogoutView, name='logout'),  
    path('dashboard', views.DashboardView, name='dashboard'),               
] 
 