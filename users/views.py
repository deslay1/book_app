from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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

from django.forms.models import model_to_dict
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from .groups import join_group
import pathlib


def register(request):
    if request.method == 'POST':
        u_form = UserRegisterForm(request.POST)

        if u_form.is_valid():
            u_form_with_extra_category = u_form.save(commit=False)
            user = u_form_with_extra_category['form']
            chosen_group = u_form_with_extra_category['chosen_group']
            user.save()
            join_group(chosen_group, user)
            messages.success(
                request, f'Your account has been created!'
            )
            return redirect('register-update', pk=user.id)
    else:
        u_form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': u_form})


class RegisterUpdateView(UpdateView, UserPassesTestMixin):
    model = Profile
    template_name = "users/permissions/register.html"
    success_url = '/login/'
    form_class = ProfileUpdateForm

    def get_initial(self):
        # See profile view below for more details
        label = "Choose a profile image for your newly made account:"
        permissions = Permission.objects.filter(
            user=self.get_object().user).values_list('name', flat=True)
        return {
            'permissions': permissions[::1], 'label': label}

    def form_valid(self, form):
        # user_id = self.kwargs['pk']
        # Below is easier
        profile_user = self.get_object()
        user = profile_user.user

        permissions = form.cleaned_data["permissions"]
        for perm_name in permissions:
            permission = Permission.objects.get(name=perm_name)
            user.user_permissions.add(permission)

        messages.success(
            self.request, f'Your profile has been updated! Please log in.'
        )
        return super().form_valid(form)

    def test_func(self):
        profile = self.get_object()
        if self.request.user == profile.user:
            return True
        return False


@ login_required
def profile(request):

    def getAllUserPermissions():
        permissions = Permission.objects.filter(
            user=request.user).values_list('name', flat=True)
        # return zip(permissions, permissions)
        # Return as list. Why? --> In order for MultipleChoiceField to validate which ones are already checked
        return permissions[::1]

    if request.method == 'POST':
        label = "Update your profile image:"
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile, initial={
                'permissions': getAllUserPermissions(), 'label': label})

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()

            permissions = p_form.cleaned_data["permissions"]
            request.user.user_permissions.clear()
            for perm_name in permissions:
                permission = Permission.objects.get(name=perm_name)
                request.user.user_permissions.add(permission)
            p_form.save()

            messages.success(request, f'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        label = "Update your profile image:"
        p_form = ProfileUpdateForm(instance=request.user.profile, initial={
                                   'permissions': getAllUserPermissions(), 'label': label})

    posts = Post.objects.filter(
        Q(author=request.user)).distinct().order_by('-date_posted')
    paginator = Paginator(posts, 5)
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


def profileUserName(request, username, inos):

    posts = Post.objects.all()
    authors = "hej"

    for post in posts:
        if post.author.username == username:
            posts = Post.objects.filter(
                Q(author=post.author)).distinct().order_by('-date_posted')
            authors = post.author

    posts = Post.objects.filter(
        author__username=username).distinct().order_by('-date_posted')

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

    if len(posts) == 0:
        messages.success(
            request, f'This user does not have any posts'
        )
        if inos == 's':
            return redirect('postman:sent')
        if inos == 'in':
            return redirect('postman:inbox')

    return render(request, href, context)


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
