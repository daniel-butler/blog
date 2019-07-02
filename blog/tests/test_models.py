import pytest

from ..models import Entry


@pytest.mark.django_db(transaction=False)
def test_string_representation():
    entry = Entry(title="Test Title")
    assert str(entry) == entry.title


def test_verbose_name_plural_is_entries():
    assert str(Entry._meta.verbose_name_plural) == 'entries'


