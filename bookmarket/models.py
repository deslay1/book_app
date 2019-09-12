from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from PIL import Image
from django import forms



class Post(models.Model):
    TIPOLOGIA_CHOICES = [
    ("Buyer", "Buyer"),
    ("Seller", "Seller"),
]
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    
    
    price = models.DecimalField(max_digits=5, decimal_places=2, default="0.0",blank=True,null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    SellerOrBuyer = models.CharField(max_length=50,default=TIPOLOGIA_CHOICES[0], choices=TIPOLOGIA_CHOICES,verbose_name="Buyer or Seller?")
                                   
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey('bookmarket.Post', on_delete=models.CASCADE, related_name='comments')
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
