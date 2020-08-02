from django.test import TestCase
from bookmarket.models import Post, Comment, Reply
from django.contrib.auth.models import User
from bookmarket.factories import UserFactory, PostFactory

from django.utils import timezone
from io import StringIO

# For more information, use verbosity. For example:
# python manage.py test --verbosity 2


class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(self):
        self.post = PostFactory()

    def test_content_label(self):
        field_label = self.post._meta.get_field('content').verbose_name
        self.assertEquals(field_label, 'Description')

    def test_title_max_length(self):
        max_length = self.post._meta.get_field('title').max_length
        self.assertEquals(max_length, 50)

    def test_content_max_length(self):
        max_length = self.post._meta.get_field('content').max_length
        self.assertEquals(max_length, 590)

    """ def test_image_field(self):
        with open('bookmarket/static/bookmarket/images/good_book.jpg', encoding='utf8') as test:
            imgStringIO = StringIO(test.read())
            self.post.update(image=imgStringIO)
            file = self.post._meta.get_field('image')
            self.assertEquals(imgStringIO, file) """

    def test_object_name_is_title(self):
        expected_object_name = f'{self.post.title}'
        self.assertEquals(expected_object_name, str(self.post))

    def test_get_absolute_url(self):
        self.assertEquals(self.post.get_absolute_url(), '/post/1/')

    def test_update_price(self):
        self.post.price = 400.3
        self.post.save(update_fields=["price"])
        price = getattr(self.post, 'price')
        self.assertEquals(price, 400.3)

    def test_update_price(self):
        self.post.condition = "As New"
        self.post.save(update_fields=["condition"])
        condition = getattr(self.post, 'condition')
        self.assertEquals(condition, "As New")
