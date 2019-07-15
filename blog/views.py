from django.shortcuts import render

from .models import Entry


def homepage(request):
    entries = Entry.objects.all()
    return render(request, template_name='pages/home.html', context={'entries': entries})
