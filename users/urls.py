from django.urls import path, include
from book_app import urls
from . import views

urlpatterns = [
    path('', views.index),

]
