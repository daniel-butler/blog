from django.contrib.auth import get_user_model
from django.db import models

from blog.models import Entry

User = get_user_model()


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='users')
    entry = models.ForeignKey(to=Entry, on_delete=models.CASCADE, related_name='entires')
    reply_to = models.ForeignKey(to=Comment, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)


class CommentBody(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)
    body = models.TextField()
    comment = models.ForeignKey(to=Comment, on_delete=models.CASCADE, related_name='comments')
