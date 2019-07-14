from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Tag(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(unique=True, max_length=200)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'tags'


class Entry(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=50)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Entries',
    )
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'entries'


class EntryBody(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    entry = models.ForeignKey(to=Entry, on_delete=models.CASCADE, related_name='Entries')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.body[:50] + '...'

    class Meta:
        verbose_name_plural = 'entry bodies'


class TagToEntry(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    entry = models.ForeignKey(to=Entry, on_delete=models.CASCADE, related_name='tagged_entries')
    tag = models.ForeignKey(to=Tag, on_delete=models.CASCADE, related_name='tagged_to_entries')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name_plural = 'tags to entries'

