from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from .forms import FounderForm

def landing_page(request):
    return render(request, template_name="startup/landing_page.html")



#This route where all user get redirected to their respective profiles 
@login_required
def home(request):
    
    user = request.user
    
    if user.is_authenticated:
        if hasattr(user, 'founder'):
            return redirect(reverse('founder_detail', args = [user.founder.pk]))
        elif hasattr(user, 'employee'):
            return redirect(reverse('employee_detail', args = [user.employee.pk]))
        elif hasattr(user, 'investor'):
            return redirect('investor_feed')
    
    else:
        # If the user does not have a specific role, return a 401 error
        return HttpResponse("Unauthorized", status=401)



@login_required
def founder_update(request, id):
   
    #Prevent other types of user from access
    user = request.user
    if not hasattr(user, 'founder'):
        raise PermissionDenied
   
    
    founder = get_object_or_404(Founder, id=id)

    if request.method == 'POST':
        form = FounderForm(request.POST, request.FILES, instance=founder)
        if form.is_valid(): 
             founder.save()
             return redirect("home")
    else:
        form = FounderForm(instance=founder)
        return render(request, template_name='startup/founder_update.html', context= {'form' : form,'id' : id})


@login_required
def founder_detail(request, id):
        
    founder = get_object_or_404(Founder, id=id)

    return render(request, template_name='startup/founder_detail.html', context= {'founder' : founder})



@login_required
def founder_upload_pitch(request, id):
    user = request.user
    if not hasattr(user, "founder"):
        raise PermissionDenied

    founder = get_object_or_404(Founder, pk=id)
    if request.method == "POST":
        form = PitchDeckForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponseRedirect("/")
    else:
        form = PitchDeckForm()
    return render(request, "startup/founder_pitch_deck.html", {"form": form, "founder": founder })

@login_required  
def employee_update(request, id):
    user = request.user
    if not hasattr(user,'employee'):
        raise PermissionDenied
        
    
    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        form = EmployeeForm(request.POST,request.FILES, instance=employee)
        if form.is_valid(): 
             employee.save()
         
        return redirect("home")
    else:
        form = EmployeeForm(instance=employee)
        return render(request, template_name='startup/employee_update.html', context= {'form' : form,'id' : id})

@login_required
def employee_detail(request, id):
    user = request.user
        
    employee = get_object_or_404(Employee, id=id)

    return render(request, template_name='startup/employee_detail.html', context= {'employee' : employee})

@login_required
def investor_feed(request):
    
    user = request.user
    if not hasattr(user, 'investor'):
        raise PermissionDenied
    
    
    founders = Founder.objects.all()
    return  render(request , template_name="startup/investor_feed.html", context={"founders" : founders})



