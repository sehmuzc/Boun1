from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# Check if the register and post entry page is successfully opened.
class UrlTests(TestCase):
    def test_view(self):
        response = self.client.get('/post/new/')
        self.assertEquals(response.status_code, 200)

    def test_viewregister(self):
        response = self.client.get('/register/')
        self.assertEquals(response.status_code, 200)
class DirecttoLogin(TestCase):
    # Check if the profile page for non-logged in user directs user to login page.
    def test_viewprofile(self):
        response = self.client.get('/profile/')
        self.assertEquals(response.status_code, 302)

class Test_Title(TestCase):
    def test_authors(self):
        user2 = User.objects.create_user(username='test2', password='pass2', email='test2@gmail.com')
        spost = Post.objects.create(title='title2', author=user2, content='content2')
        self.assertEquals(spost.title, "title2")
class ContentTest(TestCase):
    def test_content(self):
        user3 = User.objects.create_user(username='test3', password='pass3', email='test3@gmail.com')
        tpost = Post.objects.create(title='title3', author=user3, content='content3')
        self.assertEquals(tpost.content, 'content3')

class Test_Author(TestCase):
    def test_authors(self):
        user4 = User.objects.create_user(username='test4', password='pass4', email='test4@gmail.com')
        fpost = Post.objects.create(title='title4', author=user4, content='content4')
        self.assertEquals(fpost.author, user4)

