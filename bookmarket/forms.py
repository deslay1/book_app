from django import forms
from django.forms import RadioSelect
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from .models import Post, Comment, Reply


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


class ReplyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReplyForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['style'] = "width: 100%;"
        self.fields['content'].widget.attrs.update(
            {'autofocus': 'autofocus', 'placeholder': 'Write a reply'})

    class Meta:
        model = Reply
        fields = [
            "content"
        ]
