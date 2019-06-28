from django.db import models
from django.utils import timezone


class Post(models.Model):
    """
    A single Post
    """
    TYPE_CHOICES = [
    ("Bug", "Bug"),
    ("Feature", "Feature"),
    ]
    STATUS_CHOICES = [
    ("To-Do", "To-Do"),
    ("Done", "Done"),
    ]
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50, default='')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=2.5)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='')
    answer = models.TextField(max_length=100000, default='')


    def __str__(self):
        return self.name
        

class Feat(models.Model):
    """
    A single Feature
    """
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=2.5)
    


    def __str__(self):
        return self.name

