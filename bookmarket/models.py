from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from django.urls import reverse
from django.conf import settings
from PIL import Image
from django import forms
from users.models import Profile


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

    #authorName = Profile

    def getGroupNames():
        groups = Group.objects.order_by(
            "name").values_list('name', flat=True)
        if groups:
            return zip(groups, groups)
        else:
            return [('All', 'All')]

    title = models.CharField(max_length=50)
    content = models.TextField(verbose_name="Description", max_length=590)
    image = models.ImageField(
        upload_to='post_pics', default='default.jpg', blank=True, verbose_name="Image ")
    image2 = models.ImageField(
        upload_to='post_pics', blank=True, verbose_name="Image 2 (optional) ")
    image3 = models.ImageField(
        upload_to='post_pics', blank=True, verbose_name="Image 3 (optional) ")
    price = models.DecimalField(
        max_digits=6, decimal_places=0, default="0.0", verbose_name="Price (kr)")
    likes = models.ManyToManyField(User, related_name="post_likes", blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    SellerOrBuyer = models.CharField(
        max_length=50, default=Buy_Sell[0], choices=Buy_Sell, verbose_name="Are you here to buy or sell? ")
    Condition = models.CharField(
        max_length=50,
        blank=True,
        choices=conditions,
        verbose_name="Condition of book(s) (optional)")
    category = models.CharField(
        max_length=50, default=list(getGroupNames())[0], choices=getGroupNames(), verbose_name='What group do you want to publish to?')

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
    comuser = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField(
        max_length=300, verbose_name="Type in your comment")
    date_posted = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.content


class Message(models.Model):
    post = models.ForeignKey(
        'bookmarket.Post', on_delete=models.CASCADE, related_name='messages')
    comuser = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    models.ForeignObject
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.content
