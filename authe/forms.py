from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class BootstrapAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(label=("Password"), widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}))


class BootstrapUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password1 = forms.CharField(label=("password1"), widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(label=("password2"), widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Enter the same password as before.'}))
    # email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    first_name = forms.CharField(label=("first_name"), max_length=30, required=True, help_text='Required.', 
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    
    last_name = forms.CharField(label=("last_name"), max_length=30, required=True, help_text='Required.',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    
    email = forms.EmailField(label=("email"), max_length=254, required=True, help_text='Required. Enter a valid email address.',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'username', 'password1', 'password2')