from django import forms
from django.forms import RadioSelect
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template, render_to_string
from django.utils.html import strip_tags

from .models import Post, Comment, Reply
from django.contrib.auth.models import User


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


class ContactUsForm(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Your title'}))
    description = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Please write a short description...'}), max_length=400)
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(
        attrs={'placeholder': 'Your email address'}), help_text="Your email address will be used to contact you.")

    def send_email(self):
        title = self.cleaned_data['title']
        description = self.cleaned_data['description']
        email = self.cleaned_data['email']

        from_email = settings.EMAIL_HOST_USER
        admin_emails = User.objects.filter(
            is_superuser=True).values_list('email', flat=True)
        recipient_list = list(admin_emails)

        subject = title
        html_message = render_to_string(
            'email_templates/contact_us_message.html', {'description': description, 'email': email})
        plain_message = strip_tags(html_message)

        send_mail(subject, plain_message, from_email, recipient_list,
                  fail_silently=True, html_message=html_message)
