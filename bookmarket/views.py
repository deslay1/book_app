from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm, MessageForm
from .models import Post, Message, Comment
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q, Case, When
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
# from django.forms.models import model_to_dict
from django.core.mail import send_mail
from django.conf import settings
from .filters import PostFilter
from django.forms.models import model_to_dict
from django.contrib.auth.models import Group


""" def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "home.html", context) """


def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None,
                    request.FILES or None, instance=instance)
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
                'You just got a comment on one of your posts, check it out!' "\n" 'http://djangobookmarket.herokuapp.com/post/'+str(post.id)+'/')
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [post.author.email, ]
            send_mail(subject, message, email_from, recipient_list)
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'bookmarket/add_comment.html', {'form': form, 'post': post})


@login_required(login_url='login')
def update_comment(request, pk, id):
    post = get_object_or_404(Post, pk=pk)
    post_comment = get_object_or_404(Comment, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=post_comment)
        if form.is_valid():
            form.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm(instance=post_comment)
    return render(request, 'bookmarket/update_comment.html', {'form': form})


@login_required(login_url='login')
def delete_comment(request, pk, id):
    post = get_object_or_404(Post, pk=pk)
    post_comment = get_object_or_404(Comment, id=id)
    post_comment.delete()
    return redirect('post-detail', pk=post.pk)
    # Useful....
    # return redirect(request.META['HTTP_REFERER'])


@login_required(login_url='login')
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    posts = post.comments.all().order_by('-date_posted')
    paginator = Paginator(posts, 5)

    page = request.GET.get('page')
    try:
        post_List = paginator.page(page)
    except PageNotAnInteger:
        post_List = paginator.page(1)
    except EmptyPage:
        post_List = paginator.page(paginator.num_pages)

    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True

    context = {
        'comments': post_List,
        'post': post,
        'is_liked': is_liked,
        'total_likes': post.total_likes()
    }

    return render(request, 'bookmarket/post_detail.html', context)


@login_required(login_url='login')
def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    # Another redirections method...
    return HttpResponseRedirect(post.get_absolute_url())


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
        'query': str(query),
    }
    return render(request, 'bookmarket/home.html', context)


def message(request):

    return render(request, 'postman/add_message.html')


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
    paginate_by = 5
    tab = "Sell"
    category = "All"
    price_order = "All"
    condition = "All"

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)

        user_groups = self.request.user.groups.values_list(
            'name', flat=True)
        groups = Group.objects.distinct().order_by("name")
        user_group_name = "All"

        # When djang groups are empty this needs to be done
        # in order not tor return any errors
        if user_groups:
            user_groups_list = list(user_groups)
            user_group_name = user_groups_list[0]
            # Placing a user's group first in list.
            groups = Group.objects.distinct().order_by(
                Case(When(name=user_group_name, then=0), default=1), 'name')

        # Initial group activation on first render
            if PostListView.category == "All":
                PostListView.category = user_groups_list[0]

        # To see model structure
        # print(model_to_dict(groups[0]))

        category = self.request.GET.get("group/category")
        tab = self.request.GET.get("tab")

        if category is not None:
            PostListView.category = category

        if tab is not None:
            PostListView.tab = tab

        object_list = self.model.objects.distinct().order_by(
            '-date_posted').filter(Q(category__exact=self.category)).filter(
            Q(SellerOrBuyer__icontains=PostListView.tab)
        )

        condition = self.request.GET.get("condition")
        if condition is not None:
            PostListView.condition = condition

        price_order = self.request.GET.get("price_order")
        if price_order is not None:
            PostListView.price_order = price_order

        reset = self.request.GET.get("reset")
        if reset is not None:
            PostListView.condition = "All"
            PostListView.price_order = "All"

        if PostListView.condition != "All":
            object_list = object_list.filter(
                Q(Condition__exact=PostListView.condition))
        if PostListView.price_order != "All":
            object_list = object_list.order_by(PostListView.price_order)

        query = self.request.GET.get('q')
        if query:
            queries = query.split(" ")
            for q in queries:
                object_list = object_list.filter(
                    Q(title__icontains=q) |
                    Q(content__icontains=q)
                )

        paginator = Paginator(object_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        context = {'posts': object_list, 'groups': groups, 'user_group_name': user_group_name, 'filter': PostFilter(
            self.request.GET, queryset=self.get_queryset()), 'condition': PostListView.condition, 'price_order': PostListView.price_order, "category": PostListView.category, 'tab': PostListView.tab}
        # Add any other variables to the context here
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'bookmarket/post_detail.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        comments = Comment.objects.all().filter(
            Q(comuser=self.request.user)).order_by('-date_posted')

        paginator = Paginator(posts, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            comments = paginator.page(page)
        except PageNotAnInteger:
            comments = paginator.page(1)
        except EmptyPage:
            comments = paginator.page(paginator.num_pages)

        context = {'comments': comments, 'post': post}
        # Add any other variables to the context here
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image', 'image2',
              'image3', 'price', 'SellerOrBuyer', 'Condition', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView, UserPassesTestMixin):
    model = Post
    fields = ['title', 'content', 'image', 'image2',
              'image3', 'price', 'SellerOrBuyer', 'Condition', 'category']

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
    return render(request, 'bookmarket/about.html', {})
