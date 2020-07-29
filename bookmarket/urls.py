from django.urls import path
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView, UserActivityView
from users.views import profileUser, profileUserName
from . import views
from django.urls import path, include
from book_app import urls

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from book_app import urls
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
    path('post/<int:pk>/comment/<int:id>/delete', views.delete_comment,
         name='delete-comment'),
    path('post/<int:pk>/reply/<int:id>/', views.update_reply,
         name='update-reply'),
    path('post/<int:pk>/reply/<int:id>/delete', views.delete_reply,
         name='delete-reply'),
    path('post/<int:pk>/comment/<int:id>/reply', views.add_reply_to_comment,
         name='add-reply-to-comment'),
    path('post/<int:pk>/message/', views.add_message_to_post,
         name='send_message_to_user'),
    path('show_message/', views.show_message, name='show_message'),
    path('post-user/<username>', profileUser, name='post-user'),
    path('show_user_post', PostListView.as_view(), name='app-show_post'),
    path('condition-guide/', views.condition_guide, name='condition-guide'),
    path('like', views.like_post, name="like_post"),
    path('update_comment_likes/<int:id>/',
         views.update_comment_likes, name="update-comment-likes"),
    path('update_reply_likes/<int:id>/', views.update_reply_likes,
         name='update-reply-likes'),
    path('message/', views.message, name="messageSend"),
    path('activity/', UserActivityView.as_view(), name="user-activity"),
    path('privacy-policy/', views.privacy_policy, name="privacy-policy"),







    path('post-user/<username>', profileUserName, name='post-username'),

]
