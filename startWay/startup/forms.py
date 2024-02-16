from django import forms



class SignUpForm(forms.Form):
    name = forms.CharField(max_length=255, label='Name')
    email = forms.EmailField(label='Email')
    phone_number = forms.CharField(max_length=255, label='Phone Number')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')
    city = forms.CharField(max_length=255, label='City')
    role = forms.ChoiceField(choices=[('investor', 'Investor'), ('founder', 'Founder'), ('mentor', 'Mentor'), ('talent', 'Talent')], label='Role')

