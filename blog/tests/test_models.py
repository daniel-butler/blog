import pytest

from ..models import Entry, EntryBody, Tag, TagToEntry


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
