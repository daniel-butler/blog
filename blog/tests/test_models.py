import pytest

from ..models import Entry


@pytest.mark.django_db(transaction=False)
def test_string_representation():
    entry = Entry(title="Test Title")
    assert str(entry) == entry.title
