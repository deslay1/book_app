from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm, MessageForm
from .models import Post, Message, Comment
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.core.mail import send_mail
from django.conf import settings


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
            subject = 'Comment recieved in Bookmarket'
            message = (
                'You just got a comment on one of your posts, check it out!' "\n" 'http://localhost:8000/post/'+str(post.id)+'/')
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [post.author.email, ]
            send_mail(subject, message, email_from, recipient_list)
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'bookmarket/add_comment.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    posts = Comment.objects.all().filter(
        Q(comuser=request.user)).order_by('-date_posted')

    paginator = Paginator(posts, 5)

    page = request.GET.get('page')
    try:
        post_List = paginator.page(page)
    except PageNotAnInteger:
        post_List = paginator.page(1)
    except EmptyPage:
        post_List = paginator.page(paginator.num_pages)
    context = {

        'post_List': post_List
    }

    return render(request, 'bookmarket/post_detail.html', {'comments': post_List,
                                                           'post': post})


@login_required(login_url='login')
def add_message_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.post = post
            message.comuser = request.user
            message.save()
            subject = 'Message recieved in Bookmarket'
            message = (
                'You just got a message regarding one of your posts, check it out!' "\n" 'http://localhost:8000/show_message/')
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [post.author.email, ]
            send_mail(subject, message, email_from, recipient_list)
            return redirect('post-detail', pk=post.pk)
    else:
        form = MessageForm()
    return render(request, 'bookmarket/add_message.html', {'form': form, 'userAu': post.author})


def home(request):
    query = request.GET['q']

    context = {
        'posts': Post.objects.all(),
        # 'posts': get_queryset(query),
        # 'query': str(query)
        'query': str(query)
    }
    return render(request, 'bookmarket/home.html', context)


@login_required(login_url='login')
def show_message(request):
    posts = Message.objects.all().filter(
        Q(comuser=request.user)).order_by('-date_posted')

    paginator = Paginator(posts, 5)

    page = request.GET.get('page')
    try:
        post_List = paginator.page(page)
    except PageNotAnInteger:
        post_List = paginator.page(1)
    except EmptyPage:
        post_List = paginator.page(paginator.num_pages)
    context = {

        'post_List': post_List
    }

    return render(request, 'bookmarket/show_messages.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'bookmarket/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2

    # Detta är för paginator och sökfältet

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)

        object_list1 = self.model.objects.filter(
            Q(SellerOrBuyer__icontains="Sell")
        ).distinct().order_by('-date_posted')

        object_list2 = self.model.objects.filter(
            Q(SellerOrBuyer__icontains="Buy")
        ).distinct().order_by('-date_posted')

        query = self.request.GET.get('q')
        if query:
            queries = query.split(" ")
            for q in queries:
                object_list1 = object_list1.filter(
                    Q(title__icontains=q) |
                    Q(content__icontains=q)
                ).distinct().order_by('-date_posted')

                object_list2 = object_list2.filter(
                    Q(title__icontains=q) |
                    Q(content__icontains=q)
                ).distinct().order_by('-date_posted')

        paginator = Paginator(object_list1, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            object_list1 = paginator.page(page)
        except PageNotAnInteger:
            object_list1 = paginator.page(1)
        except EmptyPage:
            object_list1 = paginator.page(paginator.num_pages)

        paginator = Paginator(object_list2, self.paginate_by)
        page = self.request.GET.get('page2')

        try:
            object_list2 = paginator.page(page)
        except PageNotAnInteger:
            object_list2 = paginator.page(1)
        except EmptyPage:
            object_list2 = paginator.page(paginator.num_pages)

        context = {'buyers': object_list2, 'sellers': object_list1}
        # Add any other variables to the context here
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'bookmarket/post_detail.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        posts = Comment.objects.all().filter(
            Q(comuser=self.request.user)).order_by('-date_posted')

        paginator = Paginator(posts, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context = {'comments': posts, 'post': post}
        # Add any other variables to the context here
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image', 'image2',
              'image3', 'price', 'SellerOrBuyer']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView, UserPassesTestMixin):
    model = Post
    fields = ['title', 'content', 'image', 'image2',
              'image3', 'price', 'SellerOrBuyer']

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
