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
from django.forms.models import model_to_dict
from django.contrib.auth.models import User, Group
from django.contrib import messages
from .session_calc import check_session_item
from django.template.loader import get_template, render_to_string
from django.utils.html import strip_tags


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

            if comment.comuser != post.author and post.author.has_perm(
                    'users.email_on_post_comment'):

                url = f'http://127.0.0.1:8000/post/{post.id}/'
                if settings.DEBUG == True:
                    url = f'https://bookmarket-app.herokuapp.com/post/{post.id}/'

                from_email = settings.EMAIL_HOST_USER
                recipient_list = [post.author.email, ]

                subject = f'Comment recieved in your post: {comment.post.title}'
                html_message = render_to_string(
                    'email_templates/receive_comment.html', {'comment': comment, 'post': comment.post, 'url': url})
                plain_message = strip_tags(html_message)

                send_mail(subject, plain_message, from_email, recipient_list,
                          fail_silently=True, html_message=html_message)

            # Removed saved active page in session
            if 'comment_page' in request.session:
                del request.session['comment_page']
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

    # User's comments first
    comments = post.comments.distinct().order_by(
        Case(When(comuser=request.user, then=0), default=1), '-date_posted')

    paginator = Paginator(comments, 5)

    page = request.GET.get('page')
    page = check_session_item(request, page, 'comment_page')

    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    post_is_liked = post.likes.filter(id=request.user.id).exists()
    liked_comments = Comment.objects.filter(
        likes__id=request.user.id)
    disliked_comments = Comment.objects.filter(
        dislikes__id=request.user.id)

    context = {
        'comments': comments,
        'post': post,
        'post_is_liked': post_is_liked,
        'total_likes': post.total_likes(),
        'liked_comments': liked_comments,
        'disliked_comments': disliked_comments
    }

    return render(request, 'bookmarket/post_detail.html', context)


@login_required(login_url='login')
def like_post(request):
    liked_post_id = request.POST.get('like')
    post = get_object_or_404(Post, id=liked_post_id)

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    # Another redirections method...
    return HttpResponseRedirect(post.get_absolute_url())


@login_required(login_url='login')
def update_comment_likes(request, id):
    comment = get_object_or_404(Comment, id=id)

    if comment.comuser != request.user:
        likes_or_dislikes = request.POST.get('comment-like')

        liked = comment.likes.filter(id=request.user.id).exists()
        disliked = comment.dislikes.filter(id=request.user.id).exists()

        if likes_or_dislikes == "comment-like":
            if liked:
                comment.likes.remove(request.user)
            else:
                comment.likes.add(request.user)

            if disliked:
                comment.dislikes.remove(request.user)
        else:
            if disliked:
                comment.dislikes.remove(request.user)
            else:
                comment.dislikes.add(request.user)

            if liked:
                comment.likes.remove(request.user)
    else:
        messages.info(
            request, "You can not like or dislike your own comment!")

    # Another redirections method...
    return HttpResponseRedirect(comment.get_absolute_url())


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
            if 'category' not in self.request.session:
                self.request.session['category'] = user_groups_list[0]
        else:
            # Initial activation if not logged in
            if 'category' not in self.request.session:
                self.request.session['category'] = "All"

        # To see model structure
        # print(model_to_dict(groups[0]))

        category = self.request.GET.get("group/category")
        category = check_session_item(self.request, category, "category")

        # Initial tab activation
        self.request.session['active_tab'] = "Sell"
        tab = self.request.GET.get("tab")
        tab = check_session_item(self.request, tab, "active_tab")

        object_list = self.model.objects.distinct().order_by(
            '-date_posted').filter(Q(category__exact=category)).filter(
            Q(SellerOrBuyer__icontains=tab)
        )

        condition = self.request.GET.get("condition")
        condition = check_session_item(self.request, condition, "condition")

        price_order = self.request.GET.get("price_order")
        price_order = check_session_item(
            self.request, price_order, "price_order")

        reset = self.request.GET.get("reset")
        if reset is not None:
            self.request.session['condition'] = "All"
            self.request.session['price_order'] = "All"

        if self.request.session['condition'] != "All" and condition is not None:
            object_list = object_list.filter(
                Q(Condition__exact=condition))
        if self.request.session['price_order'] != "All" and price_order is not None:
            object_list = object_list.order_by(price_order)

        query = self.request.GET.get('q')
        query = check_session_item(self.request, query, "search_query")

        if query:
            queries = query.split(" ")
            for q in queries:
                object_list = object_list.filter(
                    Q(title__icontains=q) |
                    Q(content__icontains=q)
                )

        paginator = Paginator(object_list, self.paginate_by)
        page = self.request.GET.get('page')
        """ if page is None:
            print(self.request.session['post_page'])
            if 'post-page' in self.request.session:
                page = self.request.session['post_page']
            else:
                self.request.session['post_page'] = page """
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        context = {'posts': object_list, 'groups': groups, 'user_group_name': user_group_name, 'query': query, 'condition': condition,
                   'price_order': price_order, "category": category, 'tab': tab}
        return context


""" class PostDetailView(DetailView):
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
        return context """


class PostCreateView(LoginRequiredMixin, CreateView):
    #template_name = "bookmarket/post_form.html"
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView, UserPassesTestMixin):
    model = Post
    form_class = PostForm

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
    return render(request, 'bookmarket/about.html', {'test': "test"})


class UserActivityView(ListView):
    context_object_name = 'comments'
    template_name = 'bookmarket/user_activity.html'
    queryset = Comment.objects.distinct().order_by('-date_posted')

    def get_context_data(self, **kwargs):
        context = super(UserActivityView, self).get_context_data(**kwargs)

        user = self.request.user
        context['comments'] = self.queryset.filter(
            Q(comuser__exact=user))
        # Official way is to have the likes field be a ManytoMany(User, through= "Liker") where Liker is a model
        # that you can add whatever fields to, such as a created at and updated_field: see
        # https://stackoverflow.com/questions/31776586/how-to-add-a-timestamp-to-a-manytomany-record
        # This works for now...
        context['liked_posts'] = reversed(Post.objects.filter(
            likes__id=user.id))
        # And so on for more models
        return context
