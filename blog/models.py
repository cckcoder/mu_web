from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=120)
    short_description = models.TextField(max_length=160, null=True, blank=True)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.title 