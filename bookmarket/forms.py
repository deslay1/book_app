from django import forms
from django.forms import RadioSelect

from .models import Post, Comment, Message


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image",
            "image2",
            "image3",
            "price",
            "SellerOrBuyer",
            'Condition',
        ]
        widgets = {
            'Condition': forms.RadioSelect,
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content"
        ]


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            "content"
        ]
