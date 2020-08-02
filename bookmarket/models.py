from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from django.urls import reverse
from django.conf import settings

from django import forms
from users.models import Profile
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import filesizeformat


class Post(models.Model):
    Buy_Sell = [
        ("Buyer", "Buy"),
        ("Seller", "Sell"),
    ]

    conditions = [
        ('', 'Please choose if possible'),
        ('As New', 'As New'),
        ('Very Good', 'Very Good'),
        ('Acceptable', "Acceptable"),
        ('Mixed', 'Mixed'),
    ]

    def getGroupNames():
        return [("All", "All")]

    def validate_image(file):
        if file.size > settings.MAX_UPLOAD_SIZE:
            raise ValidationError(_('Filesize can be maximum %s. The file you uploaded was %s') % (
                filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(file.size)))

    title = models.CharField(max_length=50)
    content = models.TextField(verbose_name="Description", max_length=590)
    image = models.ImageField(
        upload_to='post_pics', default='default.jpg', blank=True, verbose_name="Image ", validators=[validate_image])
    image2 = models.ImageField(
        upload_to='post_pics', blank=True, verbose_name="Image 2 (optional) ", validators=[validate_image])
    image3 = models.ImageField(
        upload_to='post_pics', blank=True, verbose_name="Image 3 (optional) ", validators=[validate_image])
    price = models.DecimalField(
        max_digits=6, decimal_places=0, default="0", verbose_name="Price (kr)")
    likes = models.ManyToManyField(User, related_name="post_likes", blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    SellerOrBuyer = models.CharField(
        max_length=50, default=Buy_Sell[0], choices=Buy_Sell, verbose_name="Are you here to buy or sell? ")
    condition = models.CharField(
        max_length=50,
        blank=True,
        choices=conditions,
        verbose_name="Condition of book(s) (optional)")
    category = models.CharField(
        max_length=50, default=("All", "All"), choices=getGroupNames(), verbose_name='What group do you want to publish to?')
    # category = models.CharField(
    #    max_length=50, default=list(getGroupNames())[0], choices=getGroupNames(), verbose_name='What group do you want to publish to?')

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(
        'bookmarket.Post', on_delete=models.CASCADE, related_name='comments')
    #author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comuser = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name='comments')
    content = models.TextField(
        max_length=300, verbose_name="Enter below:")
    date_posted = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    likes = models.ManyToManyField(
        User, related_name="comment_likes", blank=True)
    dislikes = models.ManyToManyField(
        User, related_name="comment_dislikes", blank=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.post.pk})

    def __str__(self):
        return self.content


class Reply(models.Model):
    comment = models.ForeignKey(
        'bookmarket.Comment', on_delete=models.CASCADE, related_name='replies')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name='replies')
    content = models.CharField(
        max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(
        User, related_name="reply_likes", blank=True)
    dislikes = models.ManyToManyField(
        User, related_name="reply_dislikes", blank=True)

    def __str__(self):
        return self.content
