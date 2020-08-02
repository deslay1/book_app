import factory
from factory.django import DjangoModelFactory
from faker import Factory

from django.contrib.auth.models import User
from bookmarket.models import Post, Comment, Reply

faker = Factory.create()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "User %03d" % n)
    email = faker.email()
    password = faker.password()


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    #title = faker.word()
    title = factory.Sequence(lambda n: "Post %03d" % n)
    content = faker.text()
    author = factory.SubFactory(UserFactory)
    price = faker.pyint(min_value=0, max_value=3000)
    category = "All"

class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment

    post = factory.SubFactory(PostFactory)
    comuser = factory.SubFactory(UserFactory)
    content = faker.text()
