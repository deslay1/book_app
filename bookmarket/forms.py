from django import forms
from django.forms import RadioSelect
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

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
            'category'
        ]
        widgets = {
            # If we want to make the condition field with radio buttons
            # 'Condition': forms.RadioSelect,
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
