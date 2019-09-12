from django.urls import path
from .views import PostListView, PostDetailView,PostListViewBuyer, PostCreateView, PostUpdateView, PostDeleteView
from users.views import profileUser
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='app-home'),
        path('b', PostListViewBuyer.as_view(), name='app-homeBuy'),

    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),


    path('post-user/<username>', profileUser, name='post-user'),

    path('show_user_post', PostListView.as_view(), name='app-show_post'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add-comment-to-post'),



    path('about/', views.about, name='app-about')


]
