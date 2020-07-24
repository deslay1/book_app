from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from phonenumber_field.formfields import PhoneNumberField
from django.db import models

from .groups import join_group


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        email = User.username
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']

    def getGroupNames():
        groups = Group.objects.order_by(
            "name").values_list('name', flat=True)
        return zip(groups, groups)

    category = forms.ChoiceField(
        choices=getGroupNames(), label="What group do you belong to?")

    def save(self, commit=True):
        chosen_group = self.cleaned_data["category"]
        return {'form': super(UserRegisterForm, self).save(commit=commit), 'chosen_group': chosen_group}


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
