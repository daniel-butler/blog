from django.test.testcases import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

import pytest

from ..models import Entry, EntryBody


@pytest.mark.django_db(transaction=False)
def test_homepage(client):
    response = client.get(reverse('home'))
    assert response.status_code == 200


@pytest.mark.django_db(transaction=True)
class HomePageTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(name='some_user')

    def test_one_entry(self):
        body = EntryBody.objects.create(body='1-body')
        Entry.objects.create(title='1-title', body=body, author=self.user)
        response = self.client.get(reverse('home'))
        self.assertContains(response, '1-title')
        self.assertContains(response, '1-body')

    def test_two_entries(self):
        body1 = EntryBody.objects.create(body='1-body')
        body2 = EntryBody.objects.create(body='2-body')
        Entry.objects.create(title='1-title', body=body1, author=self.user)
        Entry.objects.create(title='2-title', body=body2, author=self.user)
        response = self.client.get(reverse('home'))
        self.assertContains(response, '1-title')
        self.assertContains(response, '1-body')
        self.assertContains(response, '2-title')
        self.assertContains(response, '2-body')


