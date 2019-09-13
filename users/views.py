from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from bookmarket.models import Post
from .models import Profile
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
    

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! SellerOrBuyeru are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'posts': Post.objects.all()
    }

    return render(request, 'users/profile.html', context)


def profileUser(request, username):
    inte = int(username, 10)

    context = {
        'userPost': inte,
        'posts': Post.objects.all()
    }

    return render(request, 'users/profileUser.html', context)


def base(request):

    profile = Profile.objects.all().filter(user=request.user)

    context = {
        'profile': profile
    }
    return render(request, 'bookmarket/base.html', context)

