
from django.test import TestCase
from django.contrib.auth.models import User
from .models import BlogPost

class SimpleTest(TestCase):
    def test_create_post(self):
        u = User.objects.create_user('tester','test@example.com','pass')
        p = BlogPost.objects.create(title='t', content='c', author=u, status='published')
        self.assertEqual(BlogPost.objects.count(), 1)
