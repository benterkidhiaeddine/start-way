from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .models import Investor, Founder , Employee
from .forms import SignInForm, SignUpForm
from django.http import HttpResponseNotFound



# login page
def user_login(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            
            if user is None:
                return HttpResponseNotFound("User not found")
            
            #User is found
            if user:
                login(request, user)
                return redirect('home')

                
    else:
        form = SignInForm()
    return render(request, 'startup/login.html', {'form': form})


# signup page
def user_signup(request):
    if request.method == 'POST':

        form = SignUpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone_number = form.cleaned_data["phone_number"]
            password = form.cleaned_data["password"]
            city = form.cleaned_data["city"]
            role = request.POST["role"] 
            user = User(username = email)
            
            user.set_password(password)
            user.save()
            
            match role:
                case "investor":
                    investor = Investor(user=user,phone_number=phone_number,city=city)
                    investor.save()
                case "founder":
                    founder = Founder(user=user,phone_number=phone_number,city=city)
                    founder.save()
                case "mentor":
                    mentor = Employee(user=user,phone_number=phone_number,city=city,role=role)
                    mentor.save()
                case "talent":
                    talent = Employee(user=user,phone_number=phone_number,city=city,role=role)
                    talent.save()
                    
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'startup/signup.html', {'form': form})


# logout page
def user_logout(request):
    logout(request)
    return redirect('login')