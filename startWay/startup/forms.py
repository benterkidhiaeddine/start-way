from django import forms
from .models import Founder, Employee,Skill




role_choices =[('investor', 'Investor'), ('founder', 'Founder'), ('mentor', 'Mentor'), ('talent', 'Talent')]

class SignUpForm(forms.Form):
    name = forms.CharField(max_length=255 ,widget=forms.TextInput(attrs={"class": "form-control"} ))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"} ))
    phone_number = forms.CharField(max_length=255, widget=forms.TextInput(attrs={"class": "form-control"} ))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    city = forms.CharField(max_length=255, widget=forms.TextInput(attrs={"class": "form-control"} ))
    role = forms.ChoiceField(choices=role_choices)

class SignInForm(forms.Form):

    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"} ))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

    



class FounderForm(forms.ModelForm):
    class Meta:
        model = Founder
        fields = ['startupName', 'websiteUrl', 'city', 'business', 'annualRevenue', 'productType', 'description', 'profile_image']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['user','speciality', 'city', 'hourlyRate', 'phone_number','description','profile_image']

        
class PitchDeckForm(forms.Form):
    file = forms.FileField()


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skillName']
    