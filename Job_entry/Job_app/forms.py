from .models import ContactMessage
from django import forms
from .models import CarInsurancePolicy
from django.contrib.auth.forms import UserCreationForm



# creating a form
class ContactForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = ContactMessage
 
        # specify fields to be used
        fields = [
            "name",
            "email",
            "subject",
            "message",
        ]

class CarInsurancePolicyForm(forms.ModelForm):
    agreement = forms.BooleanField(
        label='I agree to the terms and conditions',
        required=True,
        error_messages={'required': 'You must agree to the terms and conditions'}
    )

    class Meta:
        model = CarInsurancePolicy
        fields = '__all__'
        widgets = {
            'effective_date': forms.DateInput(attrs={'type': 'date'}),
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
        }

        
class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Your Email'
    }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Your Password'
    }))

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your First Name'
    }))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Last Name'
    }))
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Your Username',
        'autocomplete': 'off'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Your Email',
        'autocomplete': 'off'
    }))
    password1 = forms.CharField(max_length=40, label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Your Password',
        'autocomplete': 'off'
    }))
    password2 = forms.CharField(max_length=40, label='Confirm Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password',
        'autocomplete': 'off'
    }))

    class Meta:
       
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')