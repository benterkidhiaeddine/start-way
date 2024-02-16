from django import forms
from .models import Founder, Employee




role_choices =[('investor', 'Investor'), ('founder', 'Founder'), ('mentor', 'Mentor'), ('talent', 'Talent')]

class SignUpForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput())
    city = forms.CharField(max_length=255)
    role = forms.ChoiceField(choices=role_choices)

class SignInForm(forms.Form):

    userna = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())



class FounderForm(forms.ModelForm):
    class Meta:
        model = Founder
        fields = ['startupName', 'websiteUrl', 'city', 'business', 'annualRevenue', 'productType', 'description']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['user','speciality', 'city', 'hourlyRate', 'phone_number']