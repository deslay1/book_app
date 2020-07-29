from django.contrib import admin
from .models import Profile
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib.auth.models import Permission

admin.site.register(Permission)
admin.site.register(Profile)
