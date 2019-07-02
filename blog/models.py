from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Entry(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Entries',
    )
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title
