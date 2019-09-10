from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from .models import Post
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
     "form": form,
    }
    return render(request, "home.html", context)


def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
     "form": form,
    }
    return render(request, "home.html", context)


@login_required(login_url='login')
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.comuser = request.user
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'bookmarket/add_comment.html', {'form': form})


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
    template_name = 'bookmarket/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
    
    def get_queryset(self):
            
        query = self.request.GET.get('q')
        if query:
            queries = query.split(" ")
            for q in queries:
                object_list = self.model.objects.filter(
                    Q(title__icontains=q) |
                    Q(content__icontains=q)
                ).distinct().order_by('-date_posted')
        else:
            object_list = self.model.objects.all().order_by('-date_posted')
        return object_list


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image', 'price']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView, UserPassesTestMixin):
    model = Post
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)        

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False        


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'bookmarket/about.html', {'title': 'About'})
