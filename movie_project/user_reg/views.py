from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from movies_app.models import Movie,Category

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if first_name=="" or last_name=="" or username=="" or email=="" or password=="" or cpassword=="" :
            messages.warning(request,"There is one or more fields are empty!")
            return redirect('/user_reg/register')
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('/user_reg/register')
            elif User.objects.filter(email=email).exists():

                messages.info(request, "Email already exists")
                return redirect('/user_reg/register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save();

                messages.success(request, "Successfully Registered")
                return redirect('/user_reg/login')
        else:
            messages.info(request, "Password not matching....")

            return redirect('/user_reg/register')
        return redirect('/movies_app')
    else:
        return render(request, 'register.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/movies_app')
        else:
            messages.error(request, "Username and Password doesn't match")
            return redirect('/user_reg/login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/movies_app')