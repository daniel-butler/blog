from django.contrib.auth import get_user_model

import pytest

from ..models import Entry, EntryBody, Tag, TagToEntry


@pytest.fixture
def user_body_entry():
    user = get_user_model().objects.create(name='some_user')
    entry_body = EntryBody.objects.create(
        body="This is a test body that should be cut off but to make sure I am adding more"
    )
    entry = Entry.objects.create(title='1-title', body=entry_body, author=user)
    return user, entry_body, entry


@pytest.mark.django_db(transaction=False)
def test_string_representation():
    entry = Entry(title="Test Title")
    assert str(entry) == entry.title


def test_entry_verbose_name_plural_is_entries():
    assert str(Entry._meta.verbose_name_plural) == 'entries'


@pytest.mark.django_db(transaction=False)
def test_entry_body_string_representation():
    entry_body = EntryBody(body="This is a test body that should be cut off but to make sure I am adding more")
    assert str(entry_body) == entry_body.body[:50] + '...'


def test_entry_body_verbose_name_plural_is_entry_bodies():
    assert str(EntryBody._meta.verbose_name_plural) == 'entry bodies'


@pytest.mark.django_db(transaction=False)
def test_tag_string_representation():
    tag = Tag(name="Test Name")
    assert str(tag) == tag.name


def test_tag_verbose_name_plural_is_tags():
    assert str(Tag._meta.verbose_name_plural) == 'tags'


def test_tag_to_entry_verbose_name_plural_is_tags_to_entries():
    assert str(TagToEntry._meta.verbose_name_plural) == 'tags to entries'


@pytest.mark.django_db(transaction=True)
def test_tags_to_entries(user_body_entry):
    user, entry_body, entry = user_body_entry
    tag = Tag.objects.create(name="Django Test")

    tag_to_entry = TagToEntry.objects.create(tag_id=tag, entry_id=entry)

    assert tag_to_entry.tag_id.name == 'Django Test'
    assert tag_to_entry.entry_id.title == '1-title'

