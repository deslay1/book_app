from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from .models import Post
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
        'posts': Post.objectsall(),
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
    paginate_by = 3
    

        # Detta är för paginator och sökfältet
    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)

        object_list1 = self.model.objects.filter(
                    Q(SellerOrBuyer__icontains="Seller")
                ).distinct().order_by('-date_posted')
       
        

        object_list2 = self.model.objects.filter(
                    Q(SellerOrBuyer__icontains="Buyer")
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


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image', 'price', 'SellerOrBuyer']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView, UserPassesTestMixin):
    model = Post
    fields = ['title', 'content', 'image', 'price','SellerOrBuyer']

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
