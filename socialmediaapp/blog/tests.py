from django.test import TestCase
from django.contrib.auth.models import User

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

# Check if the user can be created successfully
class UserTest(TestCase):
    def setUp(self):
        User.objects.create(username='TestUser1')
    def test_user_created(self):
        user = User.objects.filter(username='TestUser1')
        self.assertTrue(user.exists())
