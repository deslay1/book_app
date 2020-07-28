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
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail

from .groups import join_group
import pathlib


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            join_group(user)
            #username = form.cleaned_data.get('email')
            messages.success(
                request, f'Your account has been created! Please log in.'
            )
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def search(q, user_id):
    user = User.objects.get(**{User.USERNAME_FIELD: user_id})

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
    inte = int(username, 10)
    posts = Post.objects.all()
    authors = "hej"


    for post in posts:
        if post.id == inte:
            posts = Post.objects.filter(
                Q(author=post.author)).distinct().order_by('-date_posted')
            authors = post.author

    paginator = Paginator(posts, 2)

    page = request.GET.get('page')
    try:
        post_List = paginator.page(page)
    except PageNotAnInteger:
        post_List = paginator.page(1)
    except EmptyPage:
        post_List = paginator.page(paginator.num_pages)
    context = {
        'userPost': inte,
        'posts': posts,
        'authors': authors,
        'post_List': post_List
    }

    return render(request, 'users/profileUser.html', context)

def profileUserName(request, username, inos):
    
    posts = Post.objects.all()
    authors = search(request, username)

    for post in posts:
        if post.author.username == username:
            posts = Post.objects.filter(
                Q(author=post.author)).distinct().order_by('-date_posted')
            authors = post.author

    
    posts = Post.objects.filter(author__username=username).distinct().order_by('-date_posted')

    paginator = Paginator(posts, 2)

    page = request.GET.get('page')
    try:
        post_List = paginator.page(page)
    except PageNotAnInteger:
        post_List = paginator.page(1)
    except EmptyPage:
        post_List = paginator.page(paginator.num_pages)
    context = {
        'authors': authors,

        'post_List': post_List
    }

    href = 'users/profileUser.html'

    p = pathlib.Path(request.path)
    p.parts[2:]


    if len(posts) ==0:
        messages.success(
                request, f'This user does not have any posts'
            )
        if inos == 's':
            return redirect('postman:sent')
        if inos == 'in':
            return redirect('postman:inbox')

      

    return render(request,href, context)


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
