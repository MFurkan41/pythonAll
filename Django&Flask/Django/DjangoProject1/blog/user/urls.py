from django.contrib import admin
from django.urls import path

app_name = "user"

from . import views

urlpatterns = [
    path('login/', views.loginUser,name = "login"),
    path('register/', views.register,name = "register"),
    path('logout/', views.logoutUser,name = "logout"),
]