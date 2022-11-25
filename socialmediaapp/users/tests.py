from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
class SigninTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='btctrader1', email='test@gmail.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='test', password='btctrader1')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='yetkisiz', password='btctrader1')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        user = authenticate(username='test', password='wrongpassword')
        self.assertFalse(user is not None and user.is_authenticated)

class UserTest(TestCase):
    def setUp(self):
        User.objects.create(username='TestUser1')

    def test_user_created(self):
        user = User.objects.filter(username='TestUser1')
        self.assertTrue(user.exists())