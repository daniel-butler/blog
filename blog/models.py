from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class EntryBody(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)


class Tag(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(unique=True, max_length=200)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)


class Entry(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=50)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Entries',
    )
    body = models.ForeignKey(to=EntryBody, on_delete=models.CASCADE, related_name='Entries')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'entries'


class TagToEntry(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    entry_id = models.ForeignKey(to=Entry, on_delete=models.CASCADE, related_name='entries')
    tag_id = models.ForeignKey(to=Tag, on_delete=models.CASCADE, related_name='tags')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

