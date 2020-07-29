from django.contrib import admin
from .models import Post, Comment, Reply

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reply)
