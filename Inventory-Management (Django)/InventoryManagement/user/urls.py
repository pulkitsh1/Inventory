from django.contrib import admin
from django.urls import path, include
from user import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('changepassword', views.changePassword, name='changepassword'),
]