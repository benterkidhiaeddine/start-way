from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request, template_name='startup/LandingPage.html')



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
            role = form.cleaned_data["role"]

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

# login page
def user_login(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user:
                print("this runs")
                login(request, user)
                return redirect('home')
    else:
        form = SignInForm()
    return render(request, 'startup/login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')