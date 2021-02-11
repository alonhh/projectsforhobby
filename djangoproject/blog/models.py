from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    CHOICES = [
        ('Programming', 'Programming'),
        ('Electronics', 'Electronics'),
        ('Tech', 'Tech'),
        ('Math', 'Math'),
    ]
    title = models.CharField(max_length=100)
    topic = models.CharField(max_length=12, choices=CHOICES)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
