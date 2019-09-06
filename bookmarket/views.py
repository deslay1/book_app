from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import PostForm
from .models import Post
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from .models import Post


def home(request):

    query = request.GET['q']

    context = {
        'posts': Post.objects.all(),
        # 'posts': get_queryset(query),
        # 'query': str(query)
        'query': str(query)
    }
    return render(request, 'bookmarket/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'bookmarket/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

    def get_queryset(self):

        query = self.request.GET.get('q')
        if query:
            queries = query.split(" ")
            for q in queries:
                object_list = self.model.objects.filter(
                    Q(title__icontains=q) |
                    Q(content__icontains=q)
                ).distinct()
        else:
            object_list = self.model.objects.all()
        return object_list


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.authour = self.request.user
        return super().form_valid(form)
        """ SuccessUrl to home?"""


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.authour = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.authour:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.authour:
            return True
        return False


def about(request):
    return render(request, 'bookmarket/about.html', {'title': 'About'})
