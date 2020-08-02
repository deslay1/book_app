from django.test import TestCase
from django.urls import reverse

from bookmarket.models import Post, Comment, Reply
from bookmarket.factories import UserFactory, PostFactory, CommentFactory

class PostListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_posts = 24

        for post in range(number_of_posts):
            PostFactory()
           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class PostDetailViewTest(TestCase):
    def setUp(self):
        
        user = UserFactory(username="testingtesting12")
        user.set_password('!0sfmfgre+LL')
        user.save()
        self.post = PostFactory()
        comment_init = CommentFactory(post = self.post)

        # Create 24 comments
        number_of_comments = 24
        for comment_number in range(number_of_comments):
            comment = CommentFactory(post = self.post)
            comment.comuser = self.post.author if comment_number % 2 else comment.comuser
            comment.save()
        
    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('post-detail', args=(1,)))
        self.assertRedirects(response, '/login/?next=/post/1/')

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username="testingtesting12", password="!0sfmfgre+LL")
        response = self.client.get(reverse('post-detail', args=(1,)))
        
        # Check user is logged in
        self.assertEqual(str(response.context['user']), 'testingtesting12')
        # Check that the post we created in setUp is the same one viewed in url.
        self.assertEqual(str(response.context['post']), self.post.title)
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
        # Check we used correct template
        self.assertTemplateUsed(response, 'bookmarket/post_detail.html')
    
    def test_pagination_is_5(self):
        login = self.client.login(username="testingtesting12", password="!0sfmfgre+LL")
        response = self.client.get(reverse('post-detail', args=(1,)))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('post' in response.context)
        self.assertTrue(len(response.context['comments']) == 5)
    
    def test_post_is_liked(self):
        login = self.client.login(username="testingtesting12", password="!0sfmfgre+LL")
        response = self.client.get(reverse('post-detail', args=(1,)))
        post = response.context['post']
        user = response.context['user']
        post.likes.add(user)
        post.save()
        refreshed = self.client.get(reverse('post-detail', args=(1,)))
        self.assertTrue(refreshed.context['post_is_liked'])