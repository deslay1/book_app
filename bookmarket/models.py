from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(
        upload_to='post_pics', default='default.jpg', verbose_name="Image")
    image2 = models.ImageField(
        upload_to='post_pics', blank=True, verbose_name="Additional image 1 (optional)")
    image3 = models.ImageField(
        upload_to='post_pics', blank=True, verbose_name="Additional image 2 (optional)")
    price = models.DecimalField(max_digits=5, decimal_places=2, default="0.0")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(
        'bookmarket.Post', on_delete=models.CASCADE, related_name='comments')
    #author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comuser = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.content
