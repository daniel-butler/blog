import pytest

from ..models import Entry, EntryBody


@pytest.mark.django_db(transaction=False)
def test_string_representation():
    entry = Entry(title="Test Title")
    assert str(entry) == entry.title


def test_entry_verbose_name_plural_is_entries():
    assert str(Entry._meta.verbose_name_plural) == 'entries'


@pytest.mark.django_db(transaction=False)
def test_string_representation():
    entry_body = EntryBody(body="This is a test body that should be cut off but to make sure I am adding more")
    assert str(entry_body) == entry_body.body[:50] + '...'


def test_entry_body_verbose_name_plural_is_entry_bodies():
    assert str(EntryBody._meta.verbose_name_plural) == 'entry bodies'

