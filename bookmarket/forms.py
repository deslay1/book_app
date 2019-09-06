from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
<<<<<<< HEAD
                "title",
                "content",
                 "image",
=======
                "title", 
                "content",
                 "image",   
>>>>>>> 0f9077f38802f78a41dc078229c62b46fbfb716b
                  ]
        