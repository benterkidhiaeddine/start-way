from django import forms



role_choices =[('investor', 'Investor'), ('founder', 'Founder'), ('mentor', 'Mentor'), ('talent', 'Talent')]

class SignUpForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput())
    city = forms.CharField(max_length=255)
    role = forms.ChoiceField(choices=role_choices)

class SignInForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


