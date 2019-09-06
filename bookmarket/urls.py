from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostListView2
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='app-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
     path('post/new/', PostCreateView.as_view(), name='post-create'),
         path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
                  path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
                      path('show_user_post', PostListView2.as_view(), name='app-show_post'),



    path('about/', views.about, name='app-about'),


]
