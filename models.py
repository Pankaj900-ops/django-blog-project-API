from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class BlogPost(models.Model):
    STATUS_CHOICES = [('draft','Draft'), ('published','Published')]
    title = models.CharField(max_length=255)
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    likes = models.ManyToManyField(User, related_name="liked_posts", blank=True)

    class Meta:
        ordering = ['-timestamp']

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title


