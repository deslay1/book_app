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
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail

from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from .groups import join_group


def register(request):
    if request.method == 'POST':
        u_form = UserRegisterForm(request.POST)

        if u_form.is_valid():
            u_form_with_extra_category = u_form.save(commit=False)
            user = u_form_with_extra_category['form']
            chosen_group = u_form_with_extra_category['chosen_group']
            print(model_to_dict(user))
            user.save()
            join_group(chosen_group, user)
            # username = form.cleaned_data.get('email')
            messages.success(
                request, f'Your account has been created! Please log in.'
            )
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':

        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    posts = Post.objects.filter(
        Q(author=request.user)).distinct().order_by('-date_posted')
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        post_List = paginator.page(page)
    except PageNotAnInteger:
        post_List = paginator.page(1)
    except EmptyPage:
        post_List = paginator.page(paginator.num_pages)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'post_List': post_List
    }
    return render(request, 'users/profile.html', context)


def profileUser(request, username):
    post_id = username

    from_post = get_object_or_404(Post, id=post_id)

    user_posts = Post.objects.filter(
        Q(author=from_post.author)).order_by('-date_posted')

    paginator = Paginator(user_posts, 2)

    page = request.GET.get('page')

    try:
        user_posts = paginator.page(page)
    except PageNotAnInteger:
        user_posts = paginator.page(1)
    except EmptyPage:
        user_posts = paginator.page(paginator.num_pages)
    context = {
        'profile_user': from_post.author,
        'post_List': user_posts
    }

    return render(request, 'users/profileUser.html', context)


def base(request):
    profile = Profile.objects.all().filter(user=request.user)
    context = {
        'profile': profile,
    }
    return render(request, 'bookmarket/base.html', context)


def index(request):
    send_mail('Hello from me',
              'Hello there. this is an automated message.',
              'book.market.bm@gmail.com',
              ['book.market.bm@gmail.com'],
              fail_silently=False)
    return render(request, 'users/index.html')
