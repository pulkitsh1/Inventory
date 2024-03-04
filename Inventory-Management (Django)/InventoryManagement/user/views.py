from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(name, email, password)
        user.save()

    return render(request, 'signup.html')

def loginUser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        user = authenticate(email=email, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            
            # need to redirect to the webpage(after login)
            return redirect('/') 
        else:
            # No backend authenticated the credentials
            # alert daena hai ki wrong email or password
            return render(request,'login.html')
        
    return render(request,'login.html')

def changePassword(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        
        user = request.user
        
        if not user.check_password(current_password):
            messages.error(request, 'Current password is incorrect.')
            return redirect('change_password')
        
        if new_password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('change_password')
        
        user.set_password(new_password)
        user.save()
        
        messages.success(request, 'Password changed successfully.')
        return redirect('/')  # Redirect to index
        
    return render(request, 'change_password.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')