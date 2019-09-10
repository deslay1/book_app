from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='app-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
<<<<<<< HEAD
    path('show_user_post', PostListView.as_view(), name='app-show_post'),
=======
>>>>>>> 7479bcc66ee53fe42546de241c622d8cd18823c4
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add-comment-to-post'),



    path('about/', views.about, name='app-about')


]
