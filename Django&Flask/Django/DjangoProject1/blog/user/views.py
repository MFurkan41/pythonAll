from django.shortcuts import render,redirect
from .forms import RegisterForm
# Create your views here.

from django.contrib.auth.models import User
from django.contrib.auth import login
from django.template import RequestContext

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
    
            newUser = User(username = username)
            newUser.set_password(password)

            newUser.save()
            login(request,newUser)
            return redirect("index")
        context = {
            "form" : form
        }
        return render(request,"register.html",context)
def loginUser(request):
    return render(request,"login.html")
def logoutUser(request):
    return render(request,"logout.html")