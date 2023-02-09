from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
