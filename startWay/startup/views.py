from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth.models import User

from .forms import FounderForm


# Create your views here.
def home(request):
    return render(request, template_name='startup/LandingPage.html')




def founder_update(request, id):
    
    founder = get_object_or_404(Founder, id=id)

    if request.method == 'POST':
        form = FounderForm(request.POST, request.FILES, instance=founder)
        if form.is_valid(): 
             founder.save()
             return redirect("home")
    else:
        form = FounderForm(instance=founder)
        return render(request, template_name='startup/founder_update.html', context= {'form' : form,'id' : id})



def founder_detail(request, id):
    founder = get_object_or_404(Founder, id=id)

    return render(request, template_name='startup/founder_detail.html', context= {'founder' : founder})
    
def employee_update(request, id):
    
    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid(): 
             employee.save()
         
        return redirect("home")
    else:
        form = EmployeeForm(instance=employee)
        return render(request, template_name='startup/employee_update.html', context= {'form' : form,'id' : id})


def employee_detail(request, id):
    employee = get_object_or_404(Employee, id=id)

    return render(request, template_name='startup/employee_detail.html', context= {'employee' : employee})


def investor_feed(request):
    
    founders = Founder.objects.all()
    return  render(request , template_name="startup/investor_feed.html", context={"founders" : founders})


