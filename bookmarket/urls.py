from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from users.views import profileUser
from . import views
from django.urls import path, include


urlpatterns = [
    path('', PostListView.as_view(), name='app-home'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comment/', views.add_comment_to_post,
         name='add-comment-to-post'),
    path('post/<int:pk>/comment/<int:id>/', views.update_comment,
         name='update-comment'),
    path('post/<int:pk>/message/', views.add_message_to_post,
         name='send_message_to_user'),
    path('show_message/', views.show_message, name='show_message'),
    path('post-user/<username>', profileUser, name='post-user'),
    path('show_user_post', PostListView.as_view(), name='app-show_post'),
    path('about/', views.about, name='app-about'),
    path('like', views.like_post, name="like_post"),
]
