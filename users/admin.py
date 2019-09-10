from django.contrib import admin
from .models import Profile
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(Profile)
