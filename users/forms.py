from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from phonenumber_field.formfields import PhoneNumberField
class UserRegisterForm(UserCreationForm):
    username = forms.EmailField()
    username.label = "Email adress"
    first_name = PhoneNumberField()
    first_name.required = False
    first_name.label= "Phone number"
    

    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    first_name = PhoneNumberField()
    first_name.required = False
    first_name.label= "Phone number"

    class Meta:
        model = User


        fields = ['first_name','last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']