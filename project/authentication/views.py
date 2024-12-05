from .models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def register(request):
    if request.method == "POST":
        email = request.POST.get('email') 
        name = request.POST.get('name') 
        password = request.POST.get('password') 
        password_confirm = request.POST.get('password_confirm') 

        if password == password_confirm:
            try:  
                user = User.objects.create_user(email=email, password=password)
                user.save()
                login(request, user)
                return redirect('home')
            except:
                messages.error(request, "User Alreacdy exists.")
        else:
            messages.error(request, 'password did not match')
    return render(request, 'authentication/register.html')
    

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password= password)
        if user is not None:
            login(request, user)
            return redirect('')
        
        else:
            messages.error(request, 'User does not exist.')
    return render(request, 'authentication/login.html')

def logout(request):
    logout(request)
    return redirect('login')

def profile(request):
    pass