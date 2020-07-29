from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register/<int:pk>/update/',
         views.RegisterUpdateView.as_view(), name='register-update'),
]
