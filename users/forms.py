from .groups import join_group
from django.db import models
from phonenumber_field.formfields import PhoneNumberField
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q


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

    """ def getBasicUserPermissions():
        content_type = ContentType.objects.get(
            app_label="users", model="profile")

        # Find a better way to do this than filtering by "Get"
        # Maybe create another content_type somehow, call it "notifications" or something
        permissions = Permission.objects.filter(
            content_type=content_type, name__contains="Get").values_list('name', flat=True)
        return zip(permissions, permissions) """

    # permissions = forms.MultipleChoiceField(
    #    choices=getBasicUserPermissions(), label="What kind of notifications do you want to receive?", widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Profile
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['image'].label = self.initial['label']

        content_type = ContentType.objects.get(
            app_label="users", model="profile")
        # Find a better way to do this than filtering by "Get"
        # Maybe create another content_type somehow, call it "notifications" or something
        permissions_names = Permission.objects.filter(
            content_type=content_type, name__contains="Get").values_list('name', flat=True)
        choices = zip(permissions_names, permissions_names)

        self.fields['permissions'] = forms.MultipleChoiceField(required=False,
                                                               choices=choices, initial=self.initial['permissions'], label="What kind of notifications do you want to receive?", widget=forms.CheckboxSelectMultiple)

    def save(self, commit=True):
        permissions = self.cleaned_data["permissions"]
        return super(ProfileUpdateForm, self).save(commit=commit)
